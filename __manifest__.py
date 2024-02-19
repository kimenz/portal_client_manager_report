# -*- coding: utf-8 -*-

{
    'name': "Portal Client Manager Report",
    'price': 0.0,
    'currency': 'BRL',
    'license': 'GPLv3',
    'summary': """This module will show backend to portal user and acess to reporting.""",
    'description': """
Clinical Engeneering Reporting for Client Managers
    - This module will show backend to portal user.
    """,
    'author': "Kimenz",
    'website': "http://www.kimenz.com",
    'support': 'webmaster@kimenz.com',
    'version': '1.4',
    'category' : 'HelpDesk',
    'depends': [
        'helpdesk',
        'field-service',
        'agreement',
        'br_base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_view.xml',
        'views/field_service_order_view.xml',
        'views/my_ticket_portal_template.xml',
        'views/menus.xml',
        'views/contract_view.xml'
    ],
    'installable' : True,
    'application' : False,
}
