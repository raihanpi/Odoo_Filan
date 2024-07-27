from odoo import models, api, fields

class Provinsi(models.Model):
    _name = 'cnt_backup.provinsi'
    _rec_name= 'provinsi'



    provinsi = fields.Char()
    kota = fields.One2many(comodel_name='cnt_backup.kota', inverse_name='provinsi') # kalo One2many belakangnya ids
    