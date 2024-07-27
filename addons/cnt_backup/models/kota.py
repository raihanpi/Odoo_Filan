from odoo import models, api, fields

class Kota(models.Model):
    _name = 'cnt_backup.kota'
    _rec_name= 'kota'


    kota = fields.Char()
    provinsi = fields.Many2one(comodel_name='cnt_backup.provinsi') # kalo Many2one pake id id belakang 