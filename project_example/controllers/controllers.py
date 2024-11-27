# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectInvoice(http.Controller):
#     @http.route('/project_invoice/project_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_invoice/project_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_invoice.listing', {
#             'root': '/project_invoice/project_invoice',
#             'objects': http.request.env['project_invoice.project_invoice'].search([]),
#         })

#     @http.route('/project_invoice/project_invoice/objects/<model("project_invoice.project_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_invoice.object', {
#             'object': obj
#         })

