/** @odoo-module **/
// console.log('1,2,3')

import publicWidget from 'web.public.widget';
import {session} from '@web/session';
rpc
let rpc = require('web.rpc');

publicWidget.registry.yougShopProductDetailWidget = publicWidget.Widget.extend({
    selector: '#product_detail',
    events: {
        'click #addToCart': 'addToCart',
    },
    start: function () {
        let self = this;
        // self.upperCase();
    },
    addToCart: function (event) {
        // console.log(event.target.dataset)
        let self = this;
        let product_data = self.$el;
        let cart = [];
        let get_cart = JSON.parse(localStorage.getItem("cart")) ? JSON.parse(localStorage.getItem("cart")) : [];
        // console.log(get_cart);
        let quantity = document.getElementById("quantity_value");
        // // console.log(quantity);
        cart = get_cart;
        let checkCart = cart.find((ele) => ele.id == product_data.data('id'));
        if (checkCart) {
            cart = JSON.parse(localStorage.getItem("cart")).map((e) => {
                if (e.id == product_data.data('id')) {
                    // console.log(cart[i].id, product_data.data('id'));
                    let newQuantity = parseInt(e.quantity) + parseInt(quantity.value);
                    console.log(newQuantity);
                    return {
                        ...e,
                        quantity: newQuantity,
                    }
                }
                return e;
            })
            localStorage.setItem("cart", JSON.stringify(cart));
        } else {
            // console.log('run')
            let product = {
                "id": product_data.data('id'),
                "name": product_data.data('name'),
                "price": product_data.data('price'),
                "image": product_data.data('image'),
                "quantity": quantity.value,
            }
            cart.push(product);
            localStorage.setItem("cart", JSON.stringify(cart));
        }
    },

})

publicWidget.registry.yougShopCartWidget = publicWidget.Widget.extend({
    selector: '#my_cart',
    events: {
        'click .delete_button': 'deleteCart',
        'click .plus': 'plusQuantity',
        'click .minus': 'minusQuantity',
    },

    start: function () {
        let self = this;
        self.showHideButton();
        self.renderCart();
        self.lengthCart();
        self.allTotal();
        // self.scrollWindows();
    },

    showHideButton() {
        let shopping = document.getElementById("shopping");
        let checkout = document.getElementById("checkout");
        let get_cart = JSON.parse(localStorage.getItem("cart"))
        if (get_cart == null) {
            checkout.style.display = "none";
            shopping.style.display = "none";
        } else {
            checkout.style.display = "block";
            shopping.style.display = "block";
        }
    },

    renderCart() {
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        if (get_cart != null) {
            let cart_information = ``;
            get_cart.map((value, index) => {
                let self = this;
                cart_information +=
                    '<tr>' +
                    '<td>' + '<img src="http://localhost:8069//web/image?model=shop.products&id=' + value.id + '&field=image&unique=1684229924000" alt="" style="width: 100%; height: 100%;"  />' + '</td>' +
                    '<td>' + value.name + '</td>' +
                    '<td>' + '$ ' + value.price + '</td>' +
                    '<td>' + '<button data-id="' + index + '" id="minus_button" class="minus quantity_button">-</button>' + '<input data-id="' + index + '" type="number" class="value_quantity" min="1" value="' + value.quantity + '" />' + '<button id="plus_button" data-id="' + index + '" class="plus quantity_button">+</button>' + '</td>' +
                    '<td>' +
                    '<button class="delete_button" data-id="' + index + '" id="deleteItem">' + 'Xóa' + '</button>' +
                    // '<button class="update_button" id="updateItem">' + 'Cập nhật' + '</button>' +
                    '</td>'
            })
            document.getElementById("cart_info").innerHTML = cart_information

        } else {
            let cart = [];
        }
    },

    // Length Cart Function
    lengthCart() {
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        let length = document.getElementById('lengthCart');
        if (get_cart != null) {
            length.innerHTML = get_cart.length;
        } else {
            length.innerHTML = '0';
        }
    },

    // Delete Cart
    deleteCart: function (ev) {
        let self = this;
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        let index = ev.target.dataset.id;
        console.log(ev.target.dataset.id);
        get_cart.splice(index, 1);
        localStorage.setItem("cart", JSON.stringify(get_cart));
        self.renderCart();
        self.lengthCart();
        self.allTotal();

    },

    // Total Function
    allTotal() {
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        // subTotal
        if (get_cart != null) {
            let total = 0;
            for (let i = 0; i < get_cart.length; i++) {
                let price = get_cart[i].price;
                let quantity = get_cart[i].quantity;
                let subTotal = parseInt(price * quantity);
                total += subTotal;
                // console.log(total);
                document.getElementById('subTotal').innerHTML = total;
            }
            // Taxes
            let taxes = total * (1 / 100);
            // console.log((taxes));
            document.getElementById('taxes').innerHTML = taxes;
            // Total
            let totalAll = total + taxes;
            document.getElementById('total').innerHTML = totalAll;
        } else {
            let cart = [];
        }
    },

    plusQuantity: function (event) {
        let self = this;
        // console.log(event.target.dataset.id)
        let value_quantity_index = event.target.dataset.id
        let value_quantity_value = parseInt($('.value_quantity[data-id=' + value_quantity_index + ']').val()) + 1;
        $('.value_quantity[data-id=' + value_quantity_index + ']').val(value_quantity_value);
        let get_cart = JSON.parse(localStorage.getItem("cart")).map((ele, index) => {
            if (value_quantity_index == index) {
                return {
                    ...ele,
                    quantity: value_quantity_value
                }
            }
            return ele;
        });
        localStorage.setItem('cart', JSON.stringify((get_cart)))
        self.renderCart();
        self.lengthCart();
        self.allTotal();
    },

    minusQuantity: function (event) {
        let self = this;
        let value_quantity_index = event.target.dataset.id;
        let value_quantity_value = parseInt($('.value_quantity[data-id=' + value_quantity_index + ']').val() - 1)
        if (value_quantity_value >= 1) {
            $('.value_quantity[data-id=' + value_quantity_index + ']').val(value_quantity_value);
            console.log(value_quantity_value)
        } else {
            alert('Số lượng sản phẩm không được nhỏ hơn 1');
        }
        let get_cart = JSON.parse(localStorage.getItem("cart")).map((value, index) => {
            if (value_quantity_index == index) {
                return {
                    ...value,
                    quantity: value_quantity_value
                }
            }
            return value;
        });
        localStorage.setItem('cart', JSON.stringify((get_cart)))
        self.renderCart();
        self.lengthCart();
        self.allTotal();
    },
})

publicWidget.registry.yougShopProductWidget = publicWidget.Widget.extend({
    selector: '#product_page',
    events: {
        'click .addCart_Button': 'addProductToCart',
        'click .filter_click': 'filterProduct',
        'click #delete_filter': 'deleteFilter',
        // 'click #filter_apply': 'applyFilter'
    },

    start: function () {
        let self = this;
        self.applyFilter()
    },

    addProductToCart: function (ev) {
        let self = this;
        let product_data = ev.target.dataset;
        let product_data_id = ev.target.dataset.id;
        // console.log(product_data_id)
        let cart = [];
        let get_cart = JSON.parse(localStorage.getItem("cart")) ? JSON.parse(localStorage.getItem("cart")) : [];
        // console.log(get_cart);
        // let quantity = document.getElementById("quantity_value");
        // // console.log(quantity);
        cart = get_cart;
        const checkCart = cart.find((ele) => ele.id == product_data_id);
        if (checkCart) {
            cart = JSON.parse(localStorage.getItem("cart")).map((e) => {
                if (e.id == product_data_id) {
                    // console.log(cart[i].id, product_data.data('id'));
                    let newQuantity = parseInt(e.quantity) + 1;
                    console.log(newQuantity);
                    return {
                        ...e,
                        quantity: newQuantity,
                    }
                }
                return e;
            })
            localStorage.setItem("cart", JSON.stringify(cart));
        } else {
            // console.log('run')
            let product = {
                "id": product_data_id,
                "name": product_data.name,
                "price": product_data.price,
                "image": product_data.image,
                "quantity": 1,
            }
            cart.push(product);
            localStorage.setItem("cart", JSON.stringify(cart));
        }
    },

    filterProduct: function (event) {
        let self = this;
        // let filter_apply = document.getElementById('filter_apply')
        let filter_data_id = event.target.dataset.id
        let filter_data_name = event.target.dataset.name;
        let filter_target = event.target;
        // console.log(filter_target)
        let get_filter = JSON.parse(localStorage.getItem("filter"));
        // console.log(get_filter)
        let filter = [];
        if (get_filter != null) {
            filter = get_filter
        } else {
            filter = []
        }
        if (filter_target.checked) {
            let check = filter.find((ele) => ele.name === filter_data_name)
            // console.log(check)
            if (check) {
                console.log('Hello', filter)
            } else {
                let season = {
                    'id': filter_data_id,
                    'name': filter_data_name,
                }
                filter.push(season)
                // console.log('xam')
                // console.log(filter)
                localStorage.setItem("filter", JSON.stringify(filter))
            }
        } else {
            let newFilter = filter.filter(ele => ele.name !== filter_data_name)
            console.log(newFilter)
            localStorage.setItem("filter", JSON.stringify(newFilter))
            // console.log()
            // console.log(filter)
        }
    },

    applyFilter() {
        let filter = [];
        let get_filter = JSON.parse(localStorage.getItem("filter"));
        let filter_click = document.getElementsByClassName('filter_click')
        // console.log(filter_click[0].value)
        if (get_filter != null) {
            filter = get_filter
            for (let i = 0; i < filter_click.length; i++) {
                let check = get_filter.find(ele => ele.name == filter_click[i].value)
                if (check) {
                    // filter_click[i].
                    filter_click[i].parentElement.children[0].checked = 'checked'
                    console.log(filter_click[i].parentElement.children[0])
                }
            }

        }
    },

    deleteFilter: function() {
        localStorage.removeItem("filter");
        window.location = '/products';
    }

})

publicWidget.registry.yougShopCartCheckoutWidget = publicWidget.Widget.extend({
    selector: '#cart_checkout',
    events: {
        'click #payButton': 'payCart',
    },
    start: function () {
        let self = this;
        self.renderCart();
        // self.checkValidate();
        self.allTotal();
        // console.log(session.user_id);

    },

    // Render Cart Table
    renderCart() {
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        if (get_cart != null) {
            let cart_information = ``;
            get_cart.map((value, index) => {
                let self = this;
                cart_information +=
                    '<tr>' +
                    '<td>' + '<img src="/web/image?model=shop.products&id=' + value.id + '&field=image&unique=1684229924000" alt="" style="width: 100%; height: 100%;"  />' + '</td>' +
                    '<td>' + value.name + '</td>' +
                    '<td>' + '$ ' + value.price + '</td>' +
                    '<td>' + '<span>' + value.quantity + '</span>' + '</td>' +
                    '</tr>'
            })
            document.getElementById("cart_info").innerHTML = cart_information

        } else {
            let cart = [];
        }
    },

    // Pay Cart and Insert to Database
    redirectPage() {
        window.location = "/";
        localStorage.removeItem("cart");
        alert('Thanks for your buying')
        let a = true
        return a;
    },

    // Redirect Page
    payCart: function (ev) {
        let self = this;
        // self.checkValidate();
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        // console.log(get_cart)
        let name = document.getElementById("name").value;
        let phone = document.getElementById("phone").value;
        let email = document.getElementById("email").value;
        let address = document.getElementById("address").value;
        let note = document.getElementById("note").value;
        let arrProductCart = [];
        // let customerInfo = [];
        // Push get_cart items into arrProductCart
        if (address == '') {
            alert('Vui lòng điền đầy đủ thông tin');
        } else {
            for (let i = 0; i < get_cart.length; i++) {
                arrProductCart.push({
                    'product_id': get_cart[i].id,
                    'quantity': get_cart[i].quantity,
                    'price_unit': get_cart[i].price,
                    // 'state': '0',
                })
            }
            rpc.query(
                {
                    model: 'shop.cart',
                    method: 'pay_cart',
                    kwargs: {
                        address: address,
                        note: note,
                        user_id: session.user_id,
                        products: arrProductCart,
                    }
                }
            ).then(function () {
                console.log('Đã insert cart');
                self.redirectPage()
            })
        }
    },

    // Total Function
    allTotal() {
        let get_cart = JSON.parse(localStorage.getItem("cart"));
        // subTotal
        if (get_cart != null) {
            let total = 0;
            for (let i = 0; i < get_cart.length; i++) {
                let price = get_cart[i].price;
                let quantity = get_cart[i].quantity;
                let subTotal = parseInt(price * quantity);
                total += subTotal;
                // console.log(total);
                // document.getElementById('subTotal').innerHTML = total;
            }
            // Taxes
            let taxes = total * (1 / 100);
            // console.log((taxes));
            // document.getElementById('taxes').innerHTML = taxes;
            // Total
            let totalAll = total + taxes;
            document.getElementById('total_price').innerHTML = totalAll;
        } else {
            let cart = [];
        }
    },


    // Validate Form

    // checkValidate() {
    //     let name = document.getElementById("name").value;
    //     let phone = document.getElementById("phone").value;
    //     let email = document.getElementById("email").value;
    //     let address = document.getElementById("address").value;
    //     let note = document.getElementById("note").value;
    //     let error = document.getElementById("error");
    //
    //     // Name
    //     if (name == '' || name == null) {
    //         error.innerHTML = "Vui lòng nhập đầy đủ họ tên";
    //     }
    //     else if (name == '')
    // },

})

