# -*- coding: utf-8 -*


from odoo import models, fields, api, _

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    @api.model
    def search(self, args, offset=0, limit=0, order=None, count=False):
        if self.env.user.has_group('base.group_portal'):
            args += [('partner_id', '=', self.env.user.partner_id.id)]
        return super(ProjectTask, self).search(args, offset, limit, order, count)

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        if self._context.get('is_show_work_order_task', False) and self.env.user.has_group('base.group_portal'):
            domain.append(('partner_id', '=', self.env.user.partner_id.id))
        return super(ProjectTask, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)