from odoo import api, fields, models


class OdooPopup(models.TransientModel):
    _name = 'odoo.popup'
    _rec_name = 'new_date'
    _description = 'Class Management'


    new_date = fields.Date(string='New date')


    def set_new_date(self):
        active_id = self.env.context.get('active_id')
        student = self.env['odoo.student'].browse(active_id)
        student.write({
            'date_of_birth': self.new_date
            })
        print('Acive id =======================================')