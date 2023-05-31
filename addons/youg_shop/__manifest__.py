{
    'name': 'Youg Clothing Store',
    'version': '1.0.0',
    'category': 'Shop',
    'author': 'La Thanh',
    # 'website': 'Thereisnooneatall',
    'summary': 'Online clothing and accessories store',
    'sequence': -100,
    'description': """Youg Clothing Store- Created at 18:00 8/5/2023""",
    'depends': ['sale', 'product', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'view/new_view.xml',
        'view/menu_action.xml',
        'view/product_view.xml',
        'view/cart_view.xml',
        'view/user_view.xml',
        'view/user_customer_view.xml',
        'view/user_admin_view.xml',
        'view/category.xml',
        'view/template_product_view.xml',
        'view/template_new_view.xml',
        'view/template_cart_view.xml',
        'view/template_cart_checkout.xml',
        'view/template_home_view.xml',
        'view/template_category_view.xml',
        'view/shop_category.xml',
        'view/special_products_view.xml',
    ],
    'demo': [],
    'assets': {
        'mail.assets_discuss_public': [
        ],
        'web.assets_frontend': [
            'youg_shop/static/src/js/script.js',
            'youg_shop/static/src/css/style.css',
            'youg_shop/static/src/css/style.scss',

        ],
        'web.assets_backend': [
            'youg_shop/static/src/js/script.js',

        ],
        'web.report_assets_common': [
        ],
        'web.assets_qweb': [

        ],
        # 'youg_shop.products_assets_frontend': [
        #     'youg_shop/static/src/js/script.js'

        # ]
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'lincense': 'LGPL Version 3'
}
