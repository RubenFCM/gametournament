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
import base64
import io
from PIL import Image  # Asegúrate de importar la clase Image desde PIL
from odoo import models, fields, api


class Tournament(models.Model):
    _name = 'gametournament.tournament'
    name = fields.Char(string="Name", required=True, help="Nombre del torneo")
    logo = fields.Image(string="Logo", help="Logo del torneo", max_width=300, max_height=200)
    # Campos ocultos para almacenar la versión redimensionada de la imagen
    logo_resized = fields.Binary(string="Resized Logo", compute='_compute_resized_logo', invisible=1)
    description = fields.Text()
    prize = fields.Float(string="Prize")
    start_date = fields.Date()

    organizer_id = fields.Many2one('res.company', ondelete='set null', string="Organizer")

    due_date = fields.Date()

    inscription_id = fields.One2many('gametournament.inscription', 'inscription_id', string="Inscription")

    @api.depends('logo')
    def _compute_resized_logo(self):
        for record in self:
            if record.logo:
                record.logo_resized = self._resize_image(record.logo, 100, 100)

    def _resize_image(self, image, max_width, max_height):
        img = Image.open(io.BytesIO(base64.b64decode(image)))
        img.thumbnail((max_width, max_height), Image.ANTIALIAS)
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue())



class Inscription(models.Model):
    _name = 'gametournament.inscription'

    name = fields.Char(string="Name Team", required=True)

    inscription_id = fields.Many2one('gametournament.tournament', ondelete='cascade', string="Tournament", required=True)
