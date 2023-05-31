from datetime import date
from odoo import fields, api, models
import logging
_logger = logging.getLogger(__name__)


class UserManagement(models.Model):
    _name = "user.management"
    _description = "User Management"
    
    name = fields.Char(string="Tên người dùng", required="1")
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string="Giới tính", required="1")
    date_of_birth = fields.Date(string="Ngày sinh")
    age = fields.Integer(string="Tuổi", compute="_compute_age", store=True)
    role = fields.Selection([('admin', 'Admin'), ('customer', 'Customer')],  string="Vai trò", required="1", default="customer")
    image = fields.Image(string="Ảnh người dùng")
    address = fields.Text(string="Địa chỉ")
    # user_id = fields.Integer(value="user_id_now")

    state = fields.Selection([
        ('activate', 'Kích hoạt'), 
        ('not_activate', 'Chưa kích hoạt'), 
        ('disable', 'Hủy kích hoạt'), 
    ], string="Trạng thái", default='not_activate', required=True)
    
     
    @api.depends('date_of_birth')
    # Define compute_age function
    def _compute_age(self):
        for record in self:
            today = date.today()
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year
            else:
                record.age = 1    
                
    def action_activate(self):
        for rec in self:
            rec.state = 'activate'
            
    def action_disable(self):
        for rec in self:
            rec.state = 'disable'
            
    def action_not_activate(self):
        for rec in self:
            rec.state = 'not_activate'

    # def user_id_now(self):
    #     user_id = self.env.user.id
    #     return user_id
    #
    # _logger.info(user_id)
