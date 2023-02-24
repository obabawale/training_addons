# -*- coding: utf-8 -*-
{
    'name': "Blog App Reviewer",

    'summary': """
        Extend blog app with reviewer implementation and mailing / social features""",

    'description': """
        Extend blog app with reviewer implementation and mailing / social features
    """,

    'author': "Olalekan Babawale",
    'website': "http://obabawale.github.io",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'web',
        'blog_app'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/blog_views.xml',
        'reports/blog_reports.xml',
    ],
}
