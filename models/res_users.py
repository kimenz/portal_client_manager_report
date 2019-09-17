# -*- coding: utf-8 -*


from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        context = self._context or {}
        if context.get('active_model') ==  'machine.repair.support' or self.env.user.has_group('base.group_portal') and context.get('is_show_work_order_task'):
            return super(ResPartner, self.sudo()).read(fields, load=load)
        elif context.get('website_id'):
            return super(ResPartner, self.sudo()).read(fields, load=load)
        elif context.get('is_show_work_order_task'):
            return super(ResPartner, self.sudo()).read(fields, load=load)
        return super(ResPartner, self).read(fields, load=load)

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        context = self._context or {}
        if context.get('active_model') ==  'machine.repair.support' or self.env.user.has_group('base.group_portal') and context.get('is_show_work_order_task'):
            return super(ResUsers, self.sudo()).read(fields, load=load)
        elif context.get('website_id'):
            return super(ResUsers, self.sudo()).read(fields, load=load)
        elif context.get('is_show_work_order_task'):
            return super(ResUsers, self.sudo()).read(fields, load=load)
        return super(ResUsers, self).read(fields, load=load)
