import re
from odoo import models , fields , api
from odoo.exceptions import ValidationError
from datetime import date

class HMSPatient(models.Model):
    _name = 'hms.patient'

    _rec_name="fName"

    fName = fields.Char()

    lName = fields.Char()

    age= fields.Integer(compute='compute_age',store=True)

    CR=fields.Float()

    bloodType=fields.Selection([('a','+A'),('b','+B'),('c','+C')])

    birthDate=fields.Date()

    history=fields.Html()

    address=fields.Text()
    
    PCR=fields.Selection([('n','Negative'),('p','Positive')])

    image=fields.Binary(string="Image", store=True, attachment=False)

    state=fields.Selection([('undetermined','undetermined'),('good','good'),('fair','fair'),('serious','serious')])

    department_id=fields.Many2one('hms.department')

    department_capacity=fields.Integer(related='department_id.capacity')

    doctor_ids=fields.Many2many(comodel_name="hms.doctor")

    state_log=fields.One2many('hms.patient.log','patient_id')

    email=fields.Char()

    _sql_constraints=[
        ('age_constrain','CHECK(age > 0)','Age can not be negative number.'),
        ('unique_email' , 'UNIQUE(email)' , 'This Email is already exist.')
    ]



    #@api.constrains('age')
    #def check_age(self):
     #   if self.age<=0:
      #      raise ValidationError("Age can not be negative number.")


    @api.onchange('state')
    def create_log_state(self):
        for rec in self:
            changeState = {
             'description':'state chenged to %s' %(rec.state),
             'patient_id':rec.id
            }
            rec.env['hms.patient.log'].create(changeState)


    @api.onchange('age')
    def cheked_pcr(self):
        if self.age<30 and self.age >0:
            self.PCR="p" 
            return {
                'warning' : {
                    'message' :'PCR has been checked'
                }
              }
        

    @api.depends('birthDate')
    def  compute_age(self):
        for rec in self:
            if rec.birthDate:
                today = date.today()
                rec.age =(today.year-rec.birthDate.year)
            else:
                rec.age = 0
 

    @api.onchange('email')
    def validate_email(self):
       if self.email:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
        if match == None:
            raise ValidationError('Not a valid email.')