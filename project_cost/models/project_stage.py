from odoo import models, fields, api

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    stage_total_cost = fields.Float(
        string='Stage Total Cost',
        compute='_compute_stage_total_cost',
        store=False  # Không cần lưu trữ, vì tính toán động
    )

    def _compute_stage_total_cost(self):
        for stage in self:
            # Tìm tất cả các task thuộc giai đoạn này
            tasks = self.env['project.task'].search([('stage_id', '=', stage.id)])
            stage.stage_total_cost = sum(task.cost for task in tasks)
