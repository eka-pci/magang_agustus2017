# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
 
class StockPicking(models.Model):
    _inherit = "stock.picking"
    
    rel_consignment = fields.Boolean(related='picking_type_id.warehouse_id.partner_id.consignment')
    
    
    @api.model
    def _default_partner_id(self):
        pick_type_id = (self._context.get('default_picking_type_id', False)
                      or self._context.get('picking_type_id', False))
        if pick_type_id:
            line = self.env['stock.picking.type'].browse(pick_type_id)
            if line.warehouse_id.partner_id.consignment == True :
                return line.warehouse_id.partner_id
            
    @api.model
    def create(self, vals):
        if vals.get('picking_type_id'):
            picking_type = self.env['stock.picking.type'].browse(vals.get('picking_type_id'))
            if picking_type.warehouse_id.partner_id.consignment == True :
                vals['partner_id'] = picking_type.warehouse_id.partner_id.id
        return super(StockPicking, self).create(vals)            
    
    @api.multi
    def write(self, vals):
        if vals.get('picking_type_id'):
            picking_type = self.env['stock.picking.type'].browse(vals.get('picking_type_id'))
            if picking_type.warehouse_id.partner_id.consignment == True :
                vals['partner_id'] = picking_type.warehouse_id.partner_id.id
        return super(StockPicking, self).write(vals)
    
    

    _defaults = {
                 'partner_id' : _default_partner_id
    }
     
