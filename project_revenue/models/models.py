# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# project_revenue/models/project_revenue.py

from odoo import models, fields, api

class ProjectRevenue(models.Model):
    _name = 'project.revenue'
    _description = 'Project Revenue'

    project_id = fields.Many2one('project.project', string='Project', required=True)
    name = fields.Char(string='Revenue Name', required=True)
    type = fields.Selection([
        ('service', 'Service'),
        ('product', 'Product'),
        ('subscription', 'Subscription'),
        ('contract', 'Contract'),
        ('investment', 'Investment'),
        ('other', 'Other')
    ], string='Revenue Type', required=True)
    invoice_ids = fields.Many2many('account.move', string='Invoices', domain=[('move_type', '=', 'out_invoice')])
    total = fields.Monetary(string='Total Revenue', compute='_compute_total', store=True)
    currency_id = fields.Many2one('res.currency', related='project_id.company_id.currency_id', readonly=True)

    @api.depends('invoice_ids.amount_total')
    def _compute_total(self):
        for record in self:
            record.total = sum(record.invoice_ids.mapped('amount_total'))


class Project(models.Model):
    _inherit = 'project.project'

    revenue_ids = fields.One2many('project.revenue', 'project_id', string='Revenues')
    total_revenue = fields.Monetary(string='Total Revenue', compute='_compute_total_revenue', store=True)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)

    @api.depends('revenue_ids.total')
    def _compute_total_revenue(self):
        for project in self:
            project.total_revenue = sum(project.revenue_ids.mapped('total'))
