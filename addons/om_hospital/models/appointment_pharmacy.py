from odoo import api, fields, models

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"
    
    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string="Price", related='product_id.list_price')
    quantity = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")