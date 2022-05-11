# -*- coding: utf-8 -*-
# from odoo import http


# class Zestate(http.Controller):
#     @http.route('/zestate/zestate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zestate/zestate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zestate.listing', {
#             'root': '/zestate/zestate',
#             'objects': http.request.env['zestate.zestate'].search([]),
#         })

#     @http.route('/zestate/zestate/objects/<model("zestate.zestate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zestate.object', {
#             'object': obj
#         })
