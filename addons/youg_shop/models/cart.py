from odoo import fields, api, models
import logging


_logger = logging.getLogger(__name__)

class ShoppingCart(models.Model):
    _name = "shop.cart"
    _description = 'Shopping Cart'
    _rec_name = 'user_id'

    # name = fields.Char(string="Tên khách hàng", required=True)
    # address = fields.Text(string="Địa chỉ", required=True)
    note = fields.Text(string="Ghi chú")
    # phone = fields.Integer(string="Số điện thoại", required=True)
    # email = fields.Char(string="Email", required=True)
    user_id = fields.Many2one('res.users', string="User")
    address = fields.Text(string="Address", required=True)

    state = fields.Selection([
        ('0', 'Đang khởi tạo'),
        ('1', 'Đang xử lý'),
        ('2', 'Đã giao cho đơn vị vận chuyển'),
        ('3', 'Đang giao hàng'),
        ('4', 'Đã giao hàng'),
        ('5', 'Giao hàng thất bại'),
        ('6', 'Hủy đơn hàng'),
    ], string="Trạng thái đơn hàng", default='0', required=True)

    cart_detail = fields.One2many('shop.cart.detail', 'cart_id', string="Cart Detail")
    # product_id = fields.Many2many('shop.products', string="Product")

    def action_in_process(self):
        for rec in self:
            rec.state = '1'

    def action_to_deliver(self):
        for rec in self:
            rec.state = '2'

    def action_delivery(self):
        for rec in self:
            rec.state = '3'

    def action_delivery_success(self):
        for rec in self:
            rec.state = '4'

    def action_cancel(self):
        for rec in self:
            rec.state = '6'

    def action_fail(self):
        for rec in self:
            rec.state = '5'

    @api.model
    def pay_cart(self, **kwargs):
        # _logger.info(kwargs.get('product_id'))
        # _logger.info(kwargs.get('quantity'))
        # _logger.info(kwargs.get('price'))
        # _logger.info(self.id)
        # _logger.info(kwargs.get('products'))
        # _logger.info(kwargs.get('customer'))
        self.env['shop.cart'].create({
            'user_id': self.env.user.id,
            'address': kwargs.get('address'),
            'note': kwargs.get('note'),
        }),
        #_logger.info(self.env.user.id)  #res.users(2)
        products = []
        for p in kwargs.get('products'):
            products.append({
                'product_id': p['product_id'],
                'quantity': p['quantity'],
                'price_unit': p['price_unit'],
                'cart_id': self.env['shop.cart'].search([('user_id', '=', self.env.user.id)], order='create_date DESC', limit=1).id
            })
        _logger.info(products)
        self.env['shop.cart.detail'].create(products),
        # _logger.info(kwargs.get('customer').id)


        # self.env['shop.cart'].create({
        #     # 'id': 5,
        #     'name': kwargs.get('name'),
        #     'phone': kwargs.get('phone'),
        #     'email': kwargs.get('email'),
        #     'address': kwargs.get('address'),
        #     'note': kwargs.get('note'),
        #     'state': '0',
        # }),
        #
        #




