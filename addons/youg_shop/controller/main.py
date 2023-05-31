from odoo import http
from odoo.http import request
import logging


_logger = logging.getLogger(__name__)

class YougShop(http.Controller):

    @http.route('/products', website=True, auth='public', type='http', method=['GET'])
    def shop_products(self, **kwargs):
        # rec = http.request.env['shop.products'].search([])
        products = http.request.env['shop.products'].sudo().search([], order='create_date DESC')
        value = str(kwargs.get('value'))
        category = http.request.env['shop.products.category'].sudo().search([('status', '=', 'show')])
        shop_cart_details = http.request.env['shop.cart.detail'].sudo().search([])
        return request.render('youg_shop.shop_products', {
            'products': products,
            'category': category,
            'shop_cart_details': shop_cart_details,
            'value': value
        })

    @http.route(['/products/<int:category_id>'], website=True, auth='public', type='http')
    def shop_category(self, category_id):
        products = http.request.env['shop.products'].sudo().search([('category_id', '=', category_id)])
        category = http.request.env['shop.products.category'].sudo().search([('status', '=', 'show')])
        return request.render('youg_shop.shop_category', {
            'products': products,
            'category': category,
        })

    @http.route(['/product/detail/<int:product_id>'], website=True, auth='public', type='http')
    def shop_detail_products(self, product_id):
        detail_products = http.request.env['shop.products'].sudo().search([('id', '=', product_id)])
        return request.render('youg_shop.detail_products', {
            'detail_products': detail_products,
        })

    @http.route('/news', website=True, auth='public', type='http')
    def shop_news(self):
        news = http.request.env['shop.new'].sudo().search([], order='create_date DESC')
        return request.render('youg_shop.shop_news', {
            'news': news,
        })

    @http.route(['/news/new_detail/<int:new_id>'], website=True, auth="public", type="http")
    def shop_new_detail(self, new_id):
        new_detail = http.request.env['shop.new'].sudo().search([('id', '=', new_id)])
        return request.render('youg_shop.detail_news', {
            'new_detail': new_detail,
        })

    @http.route('/cart', website=True, auth='public', type='http')
    def shop_cart(self):
        cart = http.request.env['shop.cart'].sudo().search([])
        return request.render('youg_shop.shop_cart', {
            'cart': cart,
        })

    @http.route('/home', website=True, auth='public', type='http')
    def home(self):
        news = http.request.env['shop.new'].sudo().search([], order='create_date DESC', limit=3)
        products = http.request.env['shop.products'].sudo().search([], order='create_date DESC')
        special = http.request.env['shop.special.products'].sudo().search([], order='create_date DESC', limit=1)
        return request.render('youg_shop.shop_home', {
            'news': news,
            'products': products,
            'special': special,
        })

    @http.route('/checkout', website=True, auth='public', type='http')
    def cart_checkout(self):
        cart_checkout = http.request.env['shop.cart'].sudo().search([])
        # user = http.request.env['user.management'].sudo().search([])
        return request.render('youg_shop.shop_checkout_cart', {
            'cart_checkout': cart_checkout,
            # 'user': user,
        })
