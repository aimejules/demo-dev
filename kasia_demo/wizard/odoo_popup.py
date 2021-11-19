from odoo import api, fields, models


class OdooPopup(models.TransientModel):
    _name = 'odoo.popup'
    _rec_name = 'new_date'
    _description = 'Class Management'


    new_date = fields.Date(string='New date')