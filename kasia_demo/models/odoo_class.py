from odoo import api, fields, models


class OdooClass(models.Model):
    _name = 'odoo.class'
    _rec_name = 'name'
    _description = 'Class Management'

    name = fields.Char(string='Name', required=True)
    nb_student = fields.Integer(string="Nb student", compute='_compute_nb_student')
    partner_id = fields.Many2one('res.partner', string="Responsible", required=True)



    def _compute_nb_student(self):
    	for item in self:
    		item.nb_student = len(self.env['odoo.student'].search([('student_class_id','=',item.id)]))
