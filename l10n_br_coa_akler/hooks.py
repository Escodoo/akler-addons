# Copyright 2026 - TODAY, Wesley Oliveira <wesley.oliveira@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    coa_generic_tmpl = env.ref("l10n_br_coa_akler.account_template_akler")
    if env["ir.module.module"].search_count(
        [
            ("name", "=", "l10n_br_account"),
            ("state", "=", "installed"),
        ]
    ):
        # Relate fiscal taxes to account taxes.
        akler_coa_charts = env["account.chart.template"].search(
            [("parent_id", "=", env.ref("l10n_br_coa_akler.account_template_akler").id)]
        )
        for akler_coa_chart in akler_coa_charts:
            akler_coa_chart.load_fiscal_taxes(env, coa_generic_tmpl)
