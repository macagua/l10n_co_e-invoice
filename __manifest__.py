# -*- coding: utf-8 -*-

{
    'name': "Colombian e-invoice",
    'summary': """
        Generates electronic invoice for Colombian distribution according to DIAN requirements - Odoo 12.0""",
    'category': 'Administration',
    'version': '12.0.0.1.1',
    'depends': [
        'base',
        'account',
        'contacts',
        'stock',
        'l10n_co',
        'l10n_co_tax_extension'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/dian_fiscal_responsability_data.xml',
        'data/dian_tributes_data.xml',
        'data/sequence.xml',
        'data/dian_cron.xml',
        'views/dian_view.xml',
        'views/company_view.xml',
        'views/invoice_view.xml',
        'views/res_partner_view.xml',
        'views/report_invoice.xml',
        'views/account_view.xml',
        'views/sequence_view.xml',
        'views/product_view.xml',
        'views/l10n_cities_co_view.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable' : True
}
