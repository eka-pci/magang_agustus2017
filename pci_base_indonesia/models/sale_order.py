# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.model
    def default_get(self, vals):
        res = super(SaleOrder, self).default_get(vals)
        so_incoterm = self.partner_id.incoterm_cust_id.id or False
        if so_incoterm == False:
            so_inc = self.env['stock.incoterms'].search([('id', '=', 1)])
            res.update({'incoterm': so_inc.id})
        else:
            res.update({'incoterm': so_incoterm})
        return res
    
    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(SaleOrder, self).onchange_partner_id()
        so_incoterm = self.partner_id.incoterm_cust_id.id or False
        if so_incoterm == False:
            so_inc = self.env['stock.incoterms'].search([('id', '=', 1)])
            self.update({'incoterm': so_inc.id})
        else:
            self.update({'incoterm': so_incoterm})
        return res