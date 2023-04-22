from odoo import models , fields

class HMSDoctor(models.Model):
    _name = 'hms.doctor'

    _rec_name="fName"

    fName=fields.Char()

    lName=fields.Char()

    image=fields.Binary(string="Image", store=True, attachment=False)



