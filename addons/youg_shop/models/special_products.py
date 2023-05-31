from odoo import api, fields, models

class SpecialProducts(models.Model):
    _name = "shop.special.products"
    _description = "Special Products on Homepage"
    _rec_name = "name"

    name = fields.Char(string="Tên sản phẩm", required=True)
    image = fields.Image(string="Ảnh sản phẩm", required=True)
    description = fields.Text(string="Mô tả sản phẩm", required=True)
    date = fields.Date(string="Thời gian ra mắt", required=True)
    ref = fields.Char(string="Mã sản phẩm", required=True)
    price = fields.Float(string="Giá", required=True)
    category_id = fields.Many2one('shop.products.category', string="Danh mục sản phẩm", required=True)
    active = fields.Boolean(string="Active")

