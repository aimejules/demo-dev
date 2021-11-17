# -*- coding: utf-8 -*-
# from odoo import http


# class KasiaDemo(http.Controller):
#     @http.route('/kasia_demo/kasia_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kasia_demo/kasia_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kasia_demo.listing', {
#             'root': '/kasia_demo/kasia_demo',
#             'objects': http.request.env['kasia_demo.kasia_demo'].search([]),
#         })

#     @http.route('/kasia_demo/kasia_demo/objects/<model("kasia_demo.kasia_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kasia_demo.object', {
#             'object': obj
#         })
