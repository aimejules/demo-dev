# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Receipt(http.Controller):
    @http.route('/receipt/', auth='public',website=True,  type='http')
    def receipt(self, **kw):
        student_ids = request.env['odoo.student'].sudo().search([])
        return request.render("kasia_demo.student_list", {'student': student_ids})