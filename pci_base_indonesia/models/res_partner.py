# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError


class ResUser(models.Model):
    _inherit = "res.users"

    SELF_WRITEABLE_FIELDS = ['branch_id', 'signature', 'action_id', 'company_id', 'email', 'name', 'image', 'image_medium', 'image_small', 'lang', 'tz']

    branch_ids = fields.Many2many(comodel_name='res.partner', relation='branch_allowed_users',column1='user_id', column2='branch_id', string='Allowed Branches'
                                  , context={'user_preference': True})
    branch_id = fields.Many2one('res.partner', string='Branch', context={'user_preference': True})

    warehouse_ids = fields.Many2many(comodel_name='stock.warehouse', relation='warehouse_allowed_user', column1='user_id', column2='warehouse_id', string='Allowed Warehouses',
                                     context={'user_preference': True})

    warehouse_id = fields.Many2one('stock.warehouse', string='Default Warehouse', context={'user_preference': True})

    # test code

    @api.multi
    def write(self, vals):
        res = super(ResUser, self).write(vals)
        if vals.get('branch_id'):
            self.sudo().partner_id.write({'branch_id':vals.get('branch_id')})
        return res

    @api.model
    def create(self, values):
        user = super(ResUser, self).create(values)
        user.partner_id.write({'branch_id': user.branch_id.id})
        return user

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _default_branch(self):
        return self.env.user.partner_id.branch_id

    @api.model
    def _default_branch_ids(self):
        if self.env.context.get('default_supplier'):
            if self.env.user.partner_id.branch_id:
                return [self.env.user.partner_id.branch_id.id]

    consignment = fields.Boolean('Consignment')
    salesman = fields.Boolean('Salesman')
    branch = fields.Boolean('Branch')
    main_branch = fields.Boolean('Pusat')
    this_for_all = fields.Boolean('This for all')
    branch_id = fields.Many2one('res.partner', string='Branch', default=_default_branch, track_visibility='onchange')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', help='Warehouse branch or consignment')
    warehouse_all_ids = fields.One2many('stock.warehouse', 'branch_id')
    branch_ids = fields.Many2many(comodel_name='res.partner', relation='branch_customer',column1='branch_customer_id', 
                column2='branch_id', string='Allowed Branches', default=_default_branch_ids)
    incoterm_cust_id = fields.Many2one('stock.incoterms', string="Customer Incoterm")
    incoterm_supplier_id = fields.Many2one('stock.incoterms', string="Supplier Incoterm")

    _defaults = {
         'company_type': 'company'
    }

    @api.multi
    def name_get(self):
        super(ResPartner, self).name_get()
        res = []
        for partner in self:
            display_value = partner.name
            if not partner.branch and (partner.customer or partner.supplier):
                display_value = "[%s] %s" % (partner.ref or "", partner.name or "")            
            res.append((partner.id, display_value))
        return res
