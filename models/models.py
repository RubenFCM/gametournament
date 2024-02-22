# -*- coding: utf-8 -*-
import base64


# from odoo import models, fields, api


# class gametournament(models.Model):
#     _name = 'gametournament.gametournament'
#     _description = 'gametournament.gametournament'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
class Tournament(models.Model):
    _name = 'gametournament.tournament'
    name = fields.Char(string="Name", required=True, help="Nombre del torneo")
    logo = fields.Image(string="Logo", help="Logo del torneo")
    description = fields.Text()
    prize = fields.Float(string="Prize")
    start_date = fields.Date()

    organizer_id = fields.Many2one('res.company', ondelete='set null', string="Organizer")

    due_date = fields.Date()

    inscription_id = fields.One2many('gametournament.inscription', 'inscription_id', string="Inscription")


class Inscription(models.Model):
    _name = 'gametournament.inscription'

    # name = fields.Char(string="Name Team or player", required=True)
    name_id = fields.Many2one('res.partner', ondelete='set null', string="Name Team or player")
    date_inscription = fields.Date()

    inscription_id = fields.Many2one('gametournament.tournament', ondelete='cascade', string="Tournament", required=True)
