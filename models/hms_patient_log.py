from odoo import models , fields

class HMSPatientLog(models.Model):
    _name = 'hms.patient.log'

    description=fields.Char()

    patient_id=fields.Many2one('hms.patient')





