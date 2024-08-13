from odoo import models, api, fields

class MitraDetail(models.Model):
    _name = 'cnt_trial.mitra_detail'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one(string='Nama Mitra', comodel_name='res.partner', tracking=True)
    proposal_id = fields.Many2one(string='Proposal', comodel_name='cnt_pm.proposal', tracking=True)
    mip_id = fields.Many2one(string='MIP', comodel_name='cnt_pm.mip', related='proposal_id.mip_id', tracking=True)
    mil_ids = fields.One2many(string='Mil', comodel_name='cnt_pm.mil', related='proposal_id.mil_ids', tracking=True)
    mipro_ids = fields.One2many(string='Mipro', comodel_name='cnt_pm.mipro', related='proposal_id.mipro_ids', tracking=True)
    donasi = fields.Float(string='Donasi', tracking=True)
    donasi_ids = fields.One2many(string='Donasi', comodel_name='cnt_pm.donasi', related='proposal_id.mipro_ids.donasi_ids', tracking=True)
    # donasi = fields.Float(string='Total Donasi', related='proposal_id.mipro_ids.total', tracking=True)
    spp_ids = fields.One2many(string='SPP', comodel_name='cnt_pm.spp', related='proposal_id.spp_ids', tracking=True)
    tag_ids = fields.Many2many(comodel_name='cnt_mitra.tag', string='Tags')


    @api.depends('tag_ids')
    def _compute_tag_text(self):
        for partner in self:
            partner.tag_text = ', '.join(partner.tag_ids.mapped('name'))

    @api.model
    def my_button(self):
        # Get the current partner record
        partner = self.env.context.get('active_id')
        if partner:
            # Get the tag text from the badge
            tag_text = partner.tag_ids.mapped('name')
            # Do something with the tag text...
            print(tag_text)
            # Return a message to the user
            return {'type': 'ir.actions.act_window_close'}
        else:
            return {'type': 'ir.actions.act_window_close'}


    # def view_drivers(self):
    #     return {
    #         'name': self.mip_id.nomor_mip,
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'cnt_pm.mip',
    #         'res_id': self.mip_id.id,
    #         'target': 'current'
    #     }

    # @api.model
    # def _get_view(self, **options):
    #     arch, view = super(MitraDetail,self)._get_view(**options)
    #     for node in arch.xpath("//button[@name='view_drivers']"):
    #         node.set('string', self.mip_id.nomor_mip)
    #     return arch, view
    #     return {
    #     'name': 'Mil',
    #     'view_type': 'form',
    #     'view_mode': 'tree',
    #     'res_model': 'cnt_pm.mil'',
    #     'type': 'ir.actions.act_window',
    #     'domain': [('id', 'in', mil_ids)], # List of IDs of the Drivers
    # }    