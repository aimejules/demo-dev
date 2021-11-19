from odoo import api, fields, models


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    nif = fields.Char(string='NIF')
    stat = fields.Char(string='STAT')
    rcs = fields.Char(string='RCS')