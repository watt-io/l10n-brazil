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
    "version": "12.0.20.0.0",
    "development_status": "Production/Stable",
    "depends": [
        "uom",
        "decimal_precision",
        "product",
        "l10n_br_base",
    ],
    "data": [
        # security
        "security/fiscal_security.xml",
        "security/ir.model.access.csv",
        # Data
        # Some data is being loaded via post_init_hook in hook file
        "data/l10n_br_fiscal_email_template.xml",
        "data/l10n_br_fiscal_data.xml",
        "data/uom_data.xml",
        "data/product_data.xml",
        "data/partner_profile_data.xml",
        "data/res_partner_data.xml",
        "data/l10n_br_fiscal.tax.group.csv",
        "data/l10n_br_fiscal.icms.relief.csv",
        "data/l10n_br_fiscal.document.type.csv",
        "data/l10n_br_fiscal.product.genre.csv",
        "data/l10n_br_fiscal.cst.csv",
        "data/l10n_br_fiscal.tax.csv",
        "data/l10n_br_fiscal.tax.pis.cofins.csv",
        "data/l10n_br_fiscal_server_action.xml",
        "data/ir_cron.xml",
        "data/l10n_br_fiscal_comment_data.xml",
        # Views
        "views/cnae_view.xml",
        "views/cfop_view.xml",
        "views/comment_view.xml",
        "views/cst_view.xml",
        "views/tax_group_view.xml",
        "views/tax_view.xml",
        "views/tax_definition_view.xml",
        "views/icms_regulation_view.xml",
        "views/icms_relief_view.xml",
        "views/tax_pis_cofins_view.xml",
        "views/tax_pis_cofins_base_view.xml",
        "views/tax_pis_cofins_credit_view.xml",
        "views/tax_ipi_control_seal_view.xml",
        "views/tax_ipi_guideline_view.xml",
        "views/tax_ipi_guideline_class_view.xml",
        "views/ncm_view.xml",
        "views/nbm_view.xml",
        "views/nbs_view.xml",
        "views/service_type_view.xml",
        "views/cest_view.xml",
        "views/product_genre_view.xml",
        "views/document_type_view.xml",
        "views/document_serie_view.xml",
        "views/document_email_view.xml",
        "views/certificate_view.xml",
        "views/simplified_tax_view.xml",
        "views/simplified_tax_range_view.xml",
        "views/operation_view.xml",
        "views/operation_line_view.xml",
        "views/product_template_view.xml",
        "views/product_product_view.xml",
        "views/tax_estimate_view.xml",
        "views/partner_profile_view.xml",
        "views/res_partner_view.xml",
        "views/res_company_view.xml",
        "views/document_view.xml",
        "views/document_related_view.xml",
        "views/document_line_view.xml",
        "views/document_fiscal_mixin_view.xml",
        "views/document_fiscal_line_mixin_view.xml",
        "views/res_config_settings_view.xml",
        "views/subsequent_operation_view.xml",
        "views/subsequent_document_view.xml",
        "views/uom_uom.xml",
        "views/closing.xml",
        "views/invalidate_number_view.xml",
        "views/city_taxation_code.xml",
        "views/mdfe/mdfe_views.xml",
        "views/dfe/dfe_views.xml",
        "views/operation_dashboard_view.xml",
        "views/document_event_view.xml",
        # Wizards
        "wizards/document_cancel_wizard.xml",
        "wizards/document_correction_wizard.xml",
        "wizards/document_status_wizard.xml",
        "wizards/invalidate_number_wizard.xml",
        # Actions
        "views/l10n_br_fiscal_action.xml",
        # Menus
        "views/l10n_br_fiscal_menu.xml",
    ],
    "demo": [
        # Some demo data is being loaded via post_init_hook in hook file
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": True,
    "auto_install": False,
    "external_dependencies": {
        "python": [
            "erpbrasil.base",
            "erpbrasil.assinatura",
            "OpenSSL",
        ]
    },
}
