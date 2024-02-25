# -*- coding: utf-8 -*-
{
    'name': "Game Tournament",

    'summary': """
        Torneos de videojuegos""",

    'description': """
        Módulo para poder crear torneos de videojuegos.
    """,

    'author': "Ruben M",
    'website': "https://www.TheGamesTournament.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Torneo',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/gametournament.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': 1
}
