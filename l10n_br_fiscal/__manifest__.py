# Copyright (C) 2013  Renato Lima - Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Módulo fiscal brasileiro",
    "summary": "Brazilian fiscal core module.",
    "category": "Localisation",
    "license": "AGPL-3",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["renatonlima"],
    "website": "https://github.com/OCA/l10n-brazil",
    "development_status": "Production/Stable",
    "version": "14.0.12.2.0",
    "depends": [
        "l10n_br_base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/cnae_view.xml",
        "data/l10n_br_fiscal.cnae.csv",
    ],
    "demo": [
        # Some demo data is being loaded via post_init_hook in hook file
    ],
    "installable": True,
    "application": True,
}
