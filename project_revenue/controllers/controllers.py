# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectRevenue(http.Controller):
#     @http.route('/project_revenue/project_revenue', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_revenue/project_revenue/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_revenue.listing', {
#             'root': '/project_revenue/project_revenue',
#             'objects': http.request.env['project_revenue.project_revenue'].search([]),
#         })

#     @http.route('/project_revenue/project_revenue/objects/<model("project_revenue.project_revenue"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_revenue.object', {
#             'object': obj
#         })

