from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    invoice_ids = fields.Many2many(
        'account.move', 
        string='Invoices',
        domain=[('move_type', '=', 'in_invoice')]
    )

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    invoice_ids = fields.Many2many(
        'account.move',
        string='Invoices',
        domain=[('move_type', '=', 'in_invoice')]
    )

class ProjectProject(models.Model):
    _inherit = 'project.project'

    invoice_ids = fields.Many2many(
        'account.move',
        string='Invoices',
        domain=[('move_type', '=', 'in_invoice')]
    )

    total_cost = fields.Float(
        string='Total Cost',
        compute='_compute_total_cost'
    )

    @api.depends('invoice_ids')
    def _compute_total_cost(self):
        for project in self:
            invoices = project.invoice_ids.filtered(lambda inv: inv.state == 'posted')
            project.total_cost = sum(invoices.mapped('amount_total'))
