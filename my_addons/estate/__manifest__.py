# -*- coding: utf-8 -*-
{
    'name': "房地产广告",

    'summary': """real estate""",

    'description': """
        Real Estate
    """,

    'author': "LeeMoonge",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
