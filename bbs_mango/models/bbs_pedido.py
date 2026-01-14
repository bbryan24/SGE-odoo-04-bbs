from odoo import models, fields
from datetime import date

class Pedido(models.Model):
    _name = 'bbs_mango.bbs_pedido'
    _description = 'Pedido de manga'

    name = fields.Char(string='Referencia', required=True, default=lambda self: f'PED-{date.today()}')
    fecha = fields.Date(string='Fecha', default=date.today)
    cliente_id = fields.Many2one('manga.shop.cliente', string='Cliente', required=True)
    mangas_ids = fields.Many2many('manga.shop.manga', string='Mangas')
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='borrador')

    def _compute_total(self):
        for record in self:
            record.total = sum(manga.precio for manga in record.mangas_ids)

