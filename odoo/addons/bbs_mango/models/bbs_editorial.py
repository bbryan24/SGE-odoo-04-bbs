from odoo import models, fields

class Editorial(models.Model):
    _name = 'bbs_mango.bbs_editorial'
    _description = 'Editorial de manga'

    name = fields.Char(string='Nombre', required=True)
    pais = fields.Char(string='País')

    mangas_ids = fields.One2many('bbs_mango.bbs_manga', 'editorial_id', string='Mangas publicados')
