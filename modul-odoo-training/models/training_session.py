# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, timedelta


class TrainingSession(models.Model):
    _name = 'training.session'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Training Session'

    name = fields.Char(string='Cours', required=True)
    start_date = fields.Date(string='Date de début de la session', required=True, default=fields.Date.today)
    # end_date
    # duration
    # trainer
    # max_nb_participants
    # list_participants
