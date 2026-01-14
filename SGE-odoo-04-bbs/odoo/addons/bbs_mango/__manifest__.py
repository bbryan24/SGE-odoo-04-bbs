# -*- coding: utf-8 -*-
{
    'name': "Mango",

    'summary': "Tienda de manga japones",

    'description': """
Aplicacion para la gestion de la tienda de manga y su inventario
    """,

    'author': "Bryan Biezma Sousa",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/bbs_autor_views.xml',
        'views/bbs_cliente_views.xml',
        'views/bbs_editorial_views.xml',
        'views/bbs_manga_views.xml',
        'views/bbs_pedido_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/bbs_autor_demo.xml',
        'demo/bbs_cliente_demo.xml',
        'demo/bbs_editorial_demo.xml',
        'demo/bbs_manga_demo.xml',
        'demo/bbs_pedido_demo.xml',
    ],
}

