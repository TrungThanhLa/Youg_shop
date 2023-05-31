from odoo import fields, api, models


class CartDetail(models.Model):
    _name = "shop.cart.detail"
    _description = "Cart Details"
    
    product_id = fields.Many2one('shop.products', required=True)
    quantity = fields.Integer(string="Số lượng", required=True, default="1")
    price_unit = fields.Float(string="Price")
    cart_id = fields.Many2one('shop.cart', string="Cart")
