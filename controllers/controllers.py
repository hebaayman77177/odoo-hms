# -*- coding: utf-8 -*-
# from odoo import http


# class HotelManagmentSystem(http.Controller):
#     @http.route('/hotel_managment_system/hotel_managment_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_managment_system/hotel_managment_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_managment_system.listing', {
#             'root': '/hotel_managment_system/hotel_managment_system',
#             'objects': http.request.env['hotel_managment_system.hotel_managment_system'].search([]),
#         })

#     @http.route('/hotel_managment_system/hotel_managment_system/objects/<model("hotel_managment_system.hotel_managment_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_managment_system.object', {
#             'object': obj
#         })
