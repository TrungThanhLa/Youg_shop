from odoo import fields, api, models


class ShopProductsCategory(models.Model):
    _name = "shop.products.category"
    _description = 'Shop Category'
    _rec_name = 'name'

    name = fields.Char(string="Tên danh mục", required=True)
    status = fields.Selection([
        ('hidden', 'Ẩn'),
        ('show', 'Hiện'),
    ], string="Trạng thái", default='show', required=True)

    def show(self):
        for rec in self:
            rec.status = 'show'

    def hidden(self):
        for rec in self:
            rec.status = 'hidden'
