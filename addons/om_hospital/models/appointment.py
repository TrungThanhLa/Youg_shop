from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'


    name = fields.Char(string="Name", tracking=True)
    patient_id = fields.Many2one('hospital.patient',string="Patient")
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference", tracking=True, help="Reference from patient records")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string="Priority")
    state  = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status", default="draft", required=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=True)
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string="Pharmacy Lines")
    #One2many ('model', 'many2one relation')
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    # image_id = fields.Image(related='patient_id.image', string="Image")
    

    @api.onchange('patient_id')    
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
        
    def action_test(self):
        print("Button Clicked")    
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successful',
                'type': 'rainbow_man',
            }
        }
        
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
            
    def action_done(self):
        for rec in self:
            rec.state = 'done'
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Done',
                'type': 'rainbow_man',
            }
        }    
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'   
            
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'                     