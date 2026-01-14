from odoo import models, fields

class Autor(models.Model):
    _name = 'bbs_mango.bbs_autor'
    _description = 'Autor de manga'

    name = fields.Char(string='Nombre', required=True)
    nacionalidad = fields.Char(string='Nacionalidad')
    mangas_ids = fields.One2many('bbs_mango.bbs_manga', 'autor_id', string='Mangas')
