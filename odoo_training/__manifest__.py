# -*- coding: utf-8 -*-
{
    'name': "Odoo Training",

    'summary': """
        IT4LIFE Test de recrutement Odoo
        Module de gestion de sessions d'apprentissage""",

    'description': """
        Module de gestion de sessions d'apprentissage
    """,

    'author': "Rodolphe_ci",
    'website': "https://www.linkedin.com/in/rodolphe-ci",
    'maintainer': 'Rodolphe CHABI ILOUGBADE',
    'category': 'Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/session_view.xml',
        # 'views/templates.xml',
    ],
    # 'license': 'AGPL-3',
    'application': True,
    'auto_install': False,
    'installable': True,
    'image': [
        'static/description/icon.jpg',
    ],
}
