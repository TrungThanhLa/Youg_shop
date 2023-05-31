from odoo import api, fields, models

class ShopCategory(models.Model):
    _name = "shop.category"
    _description = "Shop Category 2nd"

    name = fields.Char(string="Tên của danh mục")