from odoo import api, fields, models

class ProductsColor(models.Model):
    _name = "products.color"
    _description = "Products color"
    _rec_name = 'name'

    name = fields.Char(string="Tên màu sản phẩm")
    ref = fields.Char(string="Mã màu phụ", default="color_2")
    color = fields.Integer(string="Màu 1", required=True)
    color_2 = fields.Char(string="Màu 2")
    active = fields.Boolean(string="Active", default=True)