from odoo import models, fields

class Cliente(models.Model):
    _name = 'bbs_mango.bbs_cliente'
    _description = 'Cliente de la tienda'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    pedidos_ids = fields.One2many('manga.shop.pedido', 'cliente_id', string='Pedidos')
