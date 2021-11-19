# -*- coding: utf-8 -*-
{
    'name': "KASIA DEMO",

    'summary': """
        Résumé de mon module Odoo spécifique

        """,

    'description': """
        Description détaillée de mon module Odoo spécifique
    """,

    'author': "KASIA SARL",
    'website': "https://kasia.mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        'data/odoo_student_data.xml',
        # views
        'views/odoo_student_views.xml',
        'views/odoo_class_views.xml',
        'views/res_partner_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
        # wizard
        'wizard/odoo_popup_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
