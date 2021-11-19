# -*- coding: utf-8 -*-

from odoo import models, fields


class OdooStudent(models.Model):
    _name = 'odoo.student'
    _description = 'Student Management System'

    name = fields.Char(string='Name',required=True)
    matricule = fields.Integer(string='Matricule',required=True)
    student_class_id = fields.Many2one('odoo.class',string='Class')
    date_of_birth = fields.Date(string='Date of birth')
    sexe = fields.Selection([('m','M'),('f','F')],string='Sexe')
    photo = fields.Image(string='Photo')
    state = fields.Selection([('new','New'),('classified','Classified'),('done','Done')], default='new')

    def set_classified(self):
        self.state = 'classified'

    def set_done(self):
        self.state = 'done'

    def open_wizard(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            # 'view_id': self.env.ref('kasia_demo.odoo_popup_form'),
            'res_model':'odoo.popup',
            'target': 'new',
            'type': 'ir.actions.act_window',
           
        }

