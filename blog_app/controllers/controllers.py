# -*- coding: utf-8 -*-
from odoo import http, SUPERUSER_ID
from odoo.http import request, Response
import json


class BlogApp(http.Controller):

    @http.route('/api/blogs/test', auth='public', methods=['GET'], cors="*", csrf=False)
    def index(self, **kw):
        return "Hello, world"

    def _serialize_blog(self, blogs):
        return blogs.read(['id', 'name', 'content', 'state'])

    @http.route('/api/blogs', type='http', auth="none", methods=['POST', 'GET'], cors="*", csrf=False)
    def blog_list(self, *args, **kwargs):
        Blog = request.env['blog_app.blog'].with_user(
            SUPERUSER_ID)
        blogs = []
        errors = []
        if request.httprequest.method == "GET":
            blogs_data = request.env['blog_app.blog'].with_user(
                SUPERUSER_ID).search([])
            blogs = self._serialize_blog(blogs_data)
        if request.httprequest.method == "POST":
            print("------------- args ---------", args)
            print("--------- kwargs ----", kwargs)
            print("--------- request data ----", request.httprequest.data)
            title = kwargs.get("title")
            content = kwargs.get("content")
            blog_vals = {'name': title, "content": content}
            try:
                blog = Blog.create(blog_vals)
                blogs = self._serialize_blog(blog)
            except Exception as e:
                errors.append("Error creating content %s" % e)
            if errors:
                error_message = (",").join(errors)
                return Response(str(error_message), status=500)

        return http.request.make_response(
            data=json.dumps({"blogs": blogs}),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/api/blogs/<model("blog_app.blog"):blog>', type='http', auth="none", methods=['UPDATE', 'PATCH', 'DELETE'], cors="*", csrf=False)
    def blog_detail(self, blog, *args, **kwargs):
        print("=======blog=======", blog)
        return http.request.make_response(
            data=json.dumps({"result": "sucess"}),
            headers=[('Content-Type', 'application/json')]
        )
