# @ 2016 Kmee - www.kmee.com.br
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allow_cnpj_multi_ie = fields.Boolean(
        string='Multiple partners with the same CNPJ',
        config_parameter='l10n_br_base_allow_cnpj_multi_ie',
        default=False)

    module_l10n_br_zip_correios = fields.Boolean(
        string='Use Brazilian postal service API')
