# -*- coding: utf-8 -*


from lxml import etree
from odoo import models, fields, api, _
from openerp.exceptions import UserError

class MachineRepairSupport(models.Model):
    _inherit = 'machine.repair.support'

    @api.model
    def create(self, vals):
        context = self._context.copy()
        if 'default_is_report_view' in context and self.env.user.has_group('base.group_portal'):
            raise UserError(_('You can not create a new request.'))
        else:
            return super(MachineRepairSupport, self).create(vals)

    @api.multi
    def write(self, vals):
        context = self._context.copy()
        if '__contexts' in context:
            context = context['__contexts'][0]
        if 'default_is_report_view' in context and self.env.user.has_group('base.group_portal'):
            raise UserError(_('You can not change request.'))
        else:
            return super(MachineRepairSupport, self).write(vals)

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(MachineRepairSupport, self).fields_view_get(view_id, view_type, toolbar, submenu)
        context = self._context.copy()
        if context.get('default_is_report_view', False):
            doc = etree.XML(res['arch'])
            if view_type == 'kanban':
                for node in doc.xpath("//kanban"):
                    node.set('create', "false")
                    node.set('edit', "false")
            elif view_type == 'tree':
                for node in doc.xpath("//tree"):
                    node.set('create', "false")
                    node.set('edit', "false")
            elif view_type == 'form':
                for node in doc.xpath("//form"):
                    node.set('create', "false")
                    node.set('edit', "false")
                if self.env.user.has_group('base.group_portal'):
                    for node in doc.xpath("//div[@class='oe_chatter']"):
                        node.set('class', 'hidden')
            res['arch'] = etree.tostring(doc)
        return res
