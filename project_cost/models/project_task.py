from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    cost = fields.Float(string='Task Cost', help="Cost associated with this task")
    total_cost = fields.Float(string='Total Task Cost', compute='_compute_total_cost', store=True)

    @api.depends('cost')
    def _compute_total_cost(self):
        for task in self:
            task.total_cost = task.cost
