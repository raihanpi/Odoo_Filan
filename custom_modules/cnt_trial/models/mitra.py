from odoo import models, api, fields

class Mitra(models.Model):
    # _name = 'cnt_trial.mitra'
    # _rec_name = 'partner_id'
    _inherit = [
        'res.partner'
        ]

    # name = fields.Char(string='Nama')
    # partner_id = fields.Many2one(string='Nama Mitra', comodel_name='res.partner')
    # phone= fields.Char(string='Phone')
    # mobile= fields.Char(string='Mobile')
    # email= fields.Char(string='Email')
    # website= fields.Char(string='Website')
    fundraiser_id= fields.Many2one(string='Fundraiser', comodel_name='res.users')
    # logo= fields.Binary()
    mitradetail_ids=fields.One2many(string='Detail', comodel_name='cnt_trial.mitra_detail', inverse_name='partner_id', tracking=True)
    
    partner_type= fields.Selection(selection=[
     ('retail' ,'Retail') ,
     ('corporate' ,'Corporate') ,
     ('crowdfunding' ,'Crowdfunding') 
    ],string='Tipe Partner')
    # spp_ids= fields.One2many (string="SPP")
    # mipro_ids= fields.One2many (string=" MIPRO")
    # mil_ids= fields.One2many (string="MIL")
    # proposal_ids= fields.One2many (string="Proposal")
    # mip_ids= fields.One2many (comodel_name='cnt_pm.mip',inverse_name="mitra_id" ,string="MIP")
    # donasi_ids= fields.One2many (string="List Donasi")

    #hasil dari donasi spp_ids
    donasi_spp= fields.Float(string='Donasi') 
   
    #total donasi dari donasi_spp
    donasi_total=fields.Float(string='Total Donasi')
    implementasi_project=fields.Char(string='Implementasi Project')
    rab_realisasi=fields.Char(string='RAB vs Realisasi')
    laporan_project=fields.Binary(string='Laporan Project')
    
    # Many2many
    #mip_ids = fields.Many2many(comodel_name="cnt_pm.mip", string="MIP")
    spp_ids = fields.Many2many(comodel_name="cnt_pm.spp", string="SPP")
    mipro_ids= fields.Many2many (comodel_name="cnt_pm.mipro",string=" MIPRO")
    mil_ids= fields.Many2many(comodel_name="cnt_pm.mil", string="MIL")
    proposal_ids= fields.Many2many(comodel_name="cnt_pm.proposal", string="Proposal")
    donasi_ids= fields.Many2many(comodel_name="cnt_pm.donasi", string="List Donasi")
    image = fields.Binary(string='Image')
    
class LogNote(models.Model):
    _name = 'log.note'
    _description = 'Log Note'

    name = fields.Char(string='Title')
    record_id = fields.Integer(string='Record ID')
    model_id = fields.Many2one('ir.model', string='Model')
    note = fields.Text(string='Note')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    create_date = fields.Datetime(string='Create Date', default=fields.Datetime.now)
    #Function
   



    