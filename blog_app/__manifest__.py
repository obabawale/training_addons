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

    'depends': ['base'],

    'data': [
        'security/blog_app_groups.xml',
        'security/ir.model.access.csv',
        'views/blog_views.xml',
        'data/blog_app.blog.csv',
        'data/blog_app_data.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
