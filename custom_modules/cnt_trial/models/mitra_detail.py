from odoo import models, api, fields

class MitraDetail(models.Model):
    _name = 'cnt_trial.mitra_detail'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one(string='Nama Mitra', comodel_name='res.partner')
    fundraiser_id= fields.Many2one(string='Fundraiser', comodel_name='res.users')
    mip_ids= fields.One2many(comodel_name='cnt_pm.mip',inverse_name="mitra_id" ,string="MIP")
    spp_id= fields.Many2one(string='spp', comodel_name='cnt_pm.spp')
   



    