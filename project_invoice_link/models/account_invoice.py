from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    task_id = fields.Many2one('project.task', string='Task')
    phase_id = fields.Many2one('project.task.type', string='Phase')
    project_id = fields.Many2one('project.project', string='Project')

    @api.constrains('task_id', 'phase_id', 'project_id')
    def _check_single_assignment(self):
        for record in self:
            if sum(bool(field) for field in [record.task_id, record.phase_id, record.project_id]) > 1:
                raise ValidationError("An invoice can only be linked to one Task, Phase, or Project.")
