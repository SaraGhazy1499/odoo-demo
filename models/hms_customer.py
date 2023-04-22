from odoo import models , fields , api
from odoo.exceptions import UserError, ValidationError

class HMSCustomer(models.Model):
    _inherit = 'res.partner'
    
    related_patient_id=fields.Many2one('hms.patient')

    _sql_constraints=[
        ('unique_patient' , 'UNIQUE(related_patient_id)' , 'This Paitent is already selected.')
    ]



  
    #@api.multi
    #def unlink(self):
    # for rec in self:
      #if rec.related_patient_id:
      #   raise UserError('You shall not unlink!!')
      #return super(HMSCustomer, self).unlink()




