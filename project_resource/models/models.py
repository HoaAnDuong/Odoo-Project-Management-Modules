from odoo import models, fields, api

class ProjectResource(models.Model):
    _name = 'project.resource'
    _description = 'Project Resource'

    project_id = fields.Many2one('project.project', string='Project', required=True)
    name = fields.Char(string='Resource Name', required=True)
    type = fields.Selection([
        ('human', 'Human'),
        ('equipment', 'Equipment'),
        ('material', 'Material')
    ], string='Type', required=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('under_maintenance', 'Under Maintenance'),
        ('retired', 'Retired')
    ], string='Status', default='available')
    cost = fields.Monetary(string='Cost',default=0.0)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id.id
    )
    owner_id = fields.Many2one('res.partner', string='Owner')
    payment_ids = fields.Many2many('account.payment', string='Payments')

    @api.depends('payment_ids.amount', 'payment_ids.currency_id')
    def _compute_cost(self):
        """Tính tổng chi phí từ các khoản thanh toán liên kết."""
        for resource in self:
            total = 0.0
            for payment in resource.payment_ids:
                if payment.currency_id and payment.currency_id != resource.currency_id:
                    total += payment.currency_id._convert(payment.amount, resource.currency_id, self.env.company, fields.Date.today())
                else:
                    total += payment.amount
            resource.cost = total

    @api.onchange('payment_ids')
    def _onchange_payment_ids(self):
        """Sự kiện onchange để tính lại cost khi payment_ids thay đổi."""
        self._compute_cost()


class Project(models.Model):
    _inherit = 'project.project'

    resource_ids = fields.One2many('project.resource', 'project_id', string='Resources')
    total_resource_cost = fields.Monetary(
        string='Total Resource Cost',
        compute='_compute_total_resource_cost',
        store=True,
        currency_field='currency_id',
        default=0.0
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id.id
    )

    @api.depends('resource_ids.cost', 'resource_ids.currency_id')
    def _compute_total_resource_cost(self):
        for project in self:
            total = 0.0
            for resource in project.resource_ids:
                
                if resource.currency_id and resource.currency_id != project.currency_id:
                    total += resource.currency_id._convert(resource.cost, project.currency_id, self.env.company_id, fields.Date.today())
                else:
                    total += resource.cost
                    
            project.total_resource_cost = total

# class AccountPayment(models.Model):
#     _inherit = 'account.payment'

#     resource_id = fields.Many2one('project.resource', string='Resource')
