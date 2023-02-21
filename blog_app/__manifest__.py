# -*- coding: utf-8 -*-
{
    'name': "Blog app for training",

    'summary': """
        app for training""",

    'description': """
        app for training
    """,

    'author': "Olalekan Babawale",
    'website': "http://obabawale.github.io.",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/blog_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
