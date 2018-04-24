# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CRMExtras(models.Model):
    _inherit = 'crm.lead'

    customer_type = fields.Selection([('prospect', 'Prospect'), ('partner', 'Partner'), ('end_user', 'End User')])
    extra_contacts = fields.Many2many('res.partner')
