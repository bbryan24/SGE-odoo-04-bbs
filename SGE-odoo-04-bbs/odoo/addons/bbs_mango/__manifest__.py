# -*- coding: utf-8 -*-
{
    'name': "Mang@",

    'summary': "Tienda de manga japones",

    'description': """
Una tienda de manga japones donde podras encontrar tus titulos favoritos y nuevas recomendaciones.
    """,

    'author': "BBS Company",
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
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bbs_autor_views.xml',
        'views/bbs_editorial_views.xml',
        'views/bbs_genero_views.xml',
        'views/bbs_manga_views.xml',
        'views/bbs_menus_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'icon': 'static/description/icon.png',

}

