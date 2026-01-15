from odoo import models, fields

class Genero(models.Model):
    _name = 'bbs_mango.bbs_genero'
    _description = 'Etiqueta o género de manga'

    name = fields.Char(string='Nombre', required=True)
    mangas_ids = fields.Many2many('bbs_mango.bbs_manga', string='Mangas')
