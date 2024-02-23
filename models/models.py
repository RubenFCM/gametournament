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
    logo = fields.Image(string="Logo", help="Logo del torneo", maxheight=120)
    description = fields.Text()
    prize = fields.Float(string="Prize")
    start_date = fields.Date()

    organizer_id = fields.Many2one('res.company', ondelete='set null', string="Organizer")

    due_date = fields.Date()

    inscription_id = fields.One2many('gametournament.inscription', 'inscription_id', string="Inscription")

    game_id = fields.Many2many('gametournament.game','game_tournament_rel', 'tournament_id', 'game_id',ondelete='cascade', string="Game", auto_join=True)


class Inscription(models.Model):
    _name = 'gametournament.inscription'

    name_id = fields.Many2many("res.partner", string='Name team or player')
    name_display = fields.Char(string="Team or Player Names", compute='_compute_name_display')

    date_inscription = fields.Date()
    inscription_id = fields.Many2one('gametournament.tournament', ondelete='cascade', string="Tournament",
                                     required=True)

    @api.depends('name_id')
    def _compute_name_display(self):
        for record in self:
            names = ", ".join(record.name_id.mapped('name'))
            record.name_display = names


class Game(models.Model):
    _name = 'gametournament.game'

    name = fields.Char(string="Name Game", required=True)
    gender = fields.Char(string="Gender")
    platform = fields.Char(string="Platform")
    description = fields.Text()
    # game_id = fields.Many2many('gametournament.tournament', ondelete='cascade', string='Tournament')
    # games = fields.Char(string="Game Names", compute='_compute_name_display')
    tournament_ids = fields.Many2many('gametournament.tournament', 'game_tournament_rel', 'game_id', 'tournament_id',string='Tournaments',auto_join=True)

    tournament_names = fields.Char(ondelete='cascade',string="Tournament Names", compute='_compute_tournament_names')

    @api.depends('tournament_ids')
    def _compute_tournament_names(self):
        for game in self:
            tournament_names = ", ".join(game.tournament_ids.mapped('name'))
            game.tournament_names = tournament_names
