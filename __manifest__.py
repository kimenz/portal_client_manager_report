# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Machine Repair Management Portal",
    'price': 0.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """This module will show backend to portal user.""",
    'description': """
Machine Repair Request and Management Portal
    - This module will show backend to portal user.
    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'version': '1.4',
    'category' : 'Manufacturing',
    'depends': [
        'machine_repair_management_extend',
        'material_purchase_requisitions',
        'br_base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/machine_repair_support_view.xml',
        'views/my_ticket_portal_template.xml',
        'views/menus.xml',
        'views/project_view.xml'
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
