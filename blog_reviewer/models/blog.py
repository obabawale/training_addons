# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Blog(models.Model):
    _inherit = 'blog_app.blog'

    #  Row-level access and Model-level access

    reviewer_id = fields.Many2one('res.partner', string='Reviewer')
