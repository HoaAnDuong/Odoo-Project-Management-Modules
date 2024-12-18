# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectResource(http.Controller):
#     @http.route('/project_resource/project_resource', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_resource/project_resource/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_resource.listing', {
#             'root': '/project_resource/project_resource',
#             'objects': http.request.env['project_resource.project_resource'].search([]),
#         })

#     @http.route('/project_resource/project_resource/objects/<model("project_resource.project_resource"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_resource.object', {
#             'object': obj
#         })

# from odoo import http
# from odoo.http import request

# class ProjectResourceController(http.Controller):

#     @http.route('/project/resource/<int:project_id>', type='http', auth='user', website=True)
#     def view_project_resources(self, project_id):
#         project = request.env['project.project'].browse(project_id)
#         resources = request.env['project.resource'].search([('project_id', '=', project_id)])
#         return request.render('project_resource.project_resource_template', {
#             'project': project,
#             'resources': resources
#         })

#     @http.route('/project/resource/add', type='http', auth='user', methods=['POST'], website=True)
#     def add_project_resource(self, **kwargs):
#         request.env['project.resource'].create({
#             'project_id': int(kwargs.get('project_id')),
#             'name': kwargs.get('name'),
#             'type': kwargs.get('type'),
#             'status': kwargs.get('status'),
#             'cost': float(kwargs.get('cost')),
#             'owner_id': int(kwargs.get('owner_id')),
#         })
#         return request.redirect('/project/resource/%s' % kwargs.get('project_id'))
