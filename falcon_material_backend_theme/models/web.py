# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class CustomResConfiguration(models.TransientModel):
    """ Inherit the base settings to add favicon. """
    _inherit = 'res.config.settings'

    fav_icon_backend = fields.Binary('Favicon')
    backend_logo = fields.Binary('Logo')

    @api.model
    def get_values(self):
        # def get_default_alias_domain(self, fields):
        res = super(CustomResConfiguration, self).get_values()
        fav_icon_backend = self.env["ir.config_parameter"].get_param(
            "fav_icon_backend", default=None)
        backend_logo = self.env["ir.config_parameter"].get_param(
            "backend_logo", default=None)
        res.update(
            fav_icon_backend=fav_icon_backend or False,
            backend_logo=backend_logo or False,
        )
        return res

    @api.multi
    def set_values(self):
        super(CustomResConfiguration, self).set_values()
        for record in self:
            self.env['ir.config_parameter'].set_param(
                "fav_icon_backend", record.fav_icon_backend or '')
            self.env['ir.config_parameter'].set_param(
                'backend_logo', record.backend_logo or '')
