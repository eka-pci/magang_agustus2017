# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError


class location(models.Model):
    _inherit = "stock.location"
    
    branch_id = fields.Many2one('res.partner','Branch')
    this_for_all = fields.Boolean('This location for all branch')


class warehouse(models.Model):
    _inherit = "stock.warehouse"
    
    branch_id = fields.Many2one('res.partner','Branch')
    code = fields.Char('Short Name', size=20, required=True, help="Short name used to identify your warehouse")
