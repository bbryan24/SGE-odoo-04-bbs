from odoo import models, fields

class Manga(models.Model):
    _name = 'bbs_mango.bbs_manga'
    _description = 'Manga'

    name = fields.Char(string='Título', required=True)
    precio = fields.Float(string='Precio')
    stock = fields.Integer(string='Stock', default=0)
    fecha_publicacion = fields.Date(string='Fecha de publicación')

    autor_id = fields.Many2one('bbs_mango.bbs_autor', string='Autor')
    editorial_id = fields.Many2one('bbs_mango.bbs_editorial', string='Editorial')
    generos_ids = fields.Many2many('bbs_mango.bbs_genero', string='Genero')

    image_1920 = fields.Image(string='Imagen', max_width=1920, max_height=1920)
