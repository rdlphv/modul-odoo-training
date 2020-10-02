# -*- coding: utf-8 -*-
# from odoo import http


# class Rodolphe-chabi-module-odoo-training(http.Controller):
#     @http.route('/rodolphe-chabi-module-odoo-training/rodolphe-chabi-module-odoo-training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rodolphe-chabi-module-odoo-training/rodolphe-chabi-module-odoo-training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rodolphe-chabi-module-odoo-training.listing', {
#             'root': '/rodolphe-chabi-module-odoo-training/rodolphe-chabi-module-odoo-training',
#             'objects': http.request.env['rodolphe-chabi-module-odoo-training.rodolphe-chabi-module-odoo-training'].search([]),
#         })

#     @http.route('/rodolphe-chabi-module-odoo-training/rodolphe-chabi-module-odoo-training/objects/<model("rodolphe-chabi-module-odoo-training.rodolphe-chabi-module-odoo-training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rodolphe-chabi-module-odoo-training.object', {
#             'object': obj
#         })
