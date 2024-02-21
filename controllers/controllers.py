# -*- coding: utf-8 -*-
# from odoo import http


# class Gametournament(http.Controller):
#     @http.route('/gametournament/gametournament', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gametournament/gametournament/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gametournament.listing', {
#             'root': '/gametournament/gametournament',
#             'objects': http.request.env['gametournament.gametournament'].search([]),
#         })

#     @http.route('/gametournament/gametournament/objects/<model("gametournament.gametournament"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gametournament.object', {
#             'object': obj
#         })
