# -*- coding: utf-8 -*-
{
    'name': "Training Odoo",

    'summary': "Modul latihan technical Odoo",

    'description': """
Modul ini digunakan untuk latihan technical Odoo berdasarkan dokumentasi resmi.
Beberapa hal yang dipelajari:
- ORM
- Views (form, tree, kanban, calendar, pivot, graph, dll)
- Security (akses rights & record rules)
- Report
- Wizard
- Demo data
    """,

    'author': "PT. Ismata Nusantara Abadi",
    'website': "https://www.ismata.co.id",

    # Categories bisa lihat di base/data/ir_module_category_data.xml
    'category': 'Training',
    'version': '0.1',

    # Modul yang dibutuhkan
    'depends': ['base', 'product', 'mail','report_xlsx'],

    # Data yang selalu diload
    'data': [
        'report/report_training_session.xml',
        'report/report_action.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/scheduler_data.xml',
        'views/partner_views.xml',
        'wizard/training_wizard_views.xml',
        'views/menuitem_views.xml',
        'views/sequence_data.xml',
    ],

    # Data demo (jika saat create DB centang demo data)
    'demo': [
        'demo/demo.xml',
    ],

    # Properti tambahan
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
