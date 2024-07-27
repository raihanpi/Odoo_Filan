from odoo import models, api, fields

class Backup(models.Model):
    _name = 'cnt_backup.backup'

    name = fields.Char()
    alamat = fields.Text()
    tanggal_lahir = fields.Date()
    umur = fields.Integer(store=True)
    jenis_kelamin = fields.Selection([
        ('Laki-Laki', 'laki-laki'), 
        ('Perempuan', 'perempuan')
    ])
    
    social_media = fields.Selection([
        ('Twitter', 'twitter'), 
        ('Perempuan', 'perempuan')
    ])

    nik = fields.Text()
    
    ngekos = fields.Boolean()

    
    
    # @api.depends('tanggal_lahir')
    def hitung_umur(self):
        tahun_sekarang = 2024
        for i in self:
            if i.tanggal_lahir:
                tahun_lahir = i.tanggal_lahir.year
                i.umur = tahun_sekarang - tahun_lahir
            else:
                i.umur = 0

    # kota = fields.Many2one(comodel_name='cnt_backup.kota')
    # anak_ids = fields.One2many(comodel_name='cnt_backup.anak')