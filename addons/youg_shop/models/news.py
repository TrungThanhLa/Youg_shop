from odoo import fields, api, models

class ShopsNews(models.Model):
    _name = "shop.new"
    _description = "Shop's news"
    _rec_name = 'title'

    title = fields.Char(string="Tiêu đề", required="1")
    image = fields.Image(string="Ảnh bài viết", required="1")
    description = fields.Text(string="Mô tả bài viết", required="1")
    post = fields.Html(string="Bài viết", required="1")