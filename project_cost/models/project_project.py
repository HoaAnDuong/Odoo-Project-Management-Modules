from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_total_cost = fields.Float(
        string='Project Total Cost',
        compute='_compute_project_total_cost',
        store=True
    )

    @api.depends('task_ids.cost')
    def _compute_project_total_cost(self):
        for project in self:
            project.project_total_cost = sum(task.cost for task in project.task_ids)
