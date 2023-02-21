# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields


class Blog(models.Model):
    _name = 'blog_app.blog'
    _description = 'Blog'
    _order = "name desc"

    # Char, Integer, Float, Many2one, One2many, Many2many, Html, Boolean, Monetary
    name = fields.Char(string="Title", help="This is the blog title")
    content = fields.Text(
        string='Content', help="This is where you put your blog contents")
    author_id = fields.Many2one(comodel_name='res.partner', string='Author',
                                default=lambda self: self.env.user.partner_id.id)
    date = fields.Date(string='Date', default=date.today())
    published = fields.Boolean(string='Published')
    state = fields.Selection([
        ('draft', 'New'),
        ('confirm', 'Open'),
        ('approve', 'Approved'),
    ], string='State', default="draft", help="""
    When record is newly created, it is in 'New' state
    When record is confirmed ok, it is in 'Open' state
    When record is approved for publishing by a manager, it is moved to 'Approved' state
    """)

    def action_confirm(self):
        self.state = 'confirm'

    def action_approve(self):
        self.state = 'approve'
