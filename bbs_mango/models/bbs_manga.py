from odoo import models, fields

class Manga(models.Model):
    _name = 'bbs_mango.bbs_manga'
    _description = 'Manga'

    name = fields.Char(string='Título', required=True)
    precio = fields.Float(string='Precio', required=True)
    fecha_publicacion = fields.Date(string='Fecha de publicación')
    stock = fields.Integer(string='Stock', default=0)

    autor_id = fields.Many2one('manga.shop.autor', string='Autor')
    editorial_id = fields.Many2one('manga.shop.editorial', string='Editorial')
    pedidos_ids = fields.Many2many('manga.shop.pedido', string='Pedidos')

    genero = fields.Selection([
        ('shonen', 'Shonen'),
        ('shojo', 'Shojo'),
        ('seinen', 'Seinen'),
        ('josei', 'Josei'),
        ('kodomo', 'Kodomo')
    ], string='Género', default='shonen')