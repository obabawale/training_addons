# -*- coding: utf-8 -*-
# from odoo import http


# class BlogApp(http.Controller):
#     @http.route('/blog_app/blog_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blog_app/blog_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('blog_app.listing', {
#             'root': '/blog_app/blog_app',
#             'objects': http.request.env['blog_app.blog_app'].search([]),
#         })

#     @http.route('/blog_app/blog_app/objects/<model("blog_app.blog_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blog_app.object', {
#             'object': obj
#         })
