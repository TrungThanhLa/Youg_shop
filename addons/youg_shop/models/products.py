from odoo import fields, api, models
import logging

_logger = logging.getLogger(__name__)

class ShopProducts(models.Model):
    _name = "shop.products"
    _description = "All the products in the shop"
    
    name = fields.Char(string="Tên sản phẩm", tracking=True, required="1")
    # name = fields.Many2one('product.product')
    ref = fields.Char(string="Mã sản phẩm", tracking=True, required="1")
    image = fields.Image(string="Ảnh sản phẩm", required="1")
    category_id = fields.Many2one('shop.products.category', string="Danh mục", required=True)
    description = fields.Html(string="Mô tả sản phẩm")
    price = fields.Float(string="Giá", required="1")
    season = fields.Selection([('spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn'),
                               ('winter', 'Winter'), ('all', 'All')], string="Đồ mùa", required=True)
