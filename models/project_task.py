from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    active2 = fields.Boolean(
        default=True,
    )

    @api.multi
    def toggle_active2(self):
        for r in self:
            r.active2 = not r.active2
