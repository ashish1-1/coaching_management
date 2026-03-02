from odoo import models, fields


class CoachingSubject(models.Model):
    _name = 'coaching.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    class_id = fields.Many2one('coaching.class', string='Class', required=True, ondelete='cascade')
    teacher_id = fields.Many2one(
        'res.partner',
        domain=[('is_coaching_teacher', '=', True)]
    )