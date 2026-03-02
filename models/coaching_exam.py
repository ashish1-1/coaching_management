from odoo import models, fields


class CoachingExam(models.Model):
    _name = 'coaching.exam'
    _description = 'Exam'

    name = fields.Char(required=True)
    year = fields.Char()
    gpa = fields.Float()
    total_marks = fields.Float()

    student_id = fields.Many2one(
        'res.partner',
        domain=[('is_coaching_student', '=', True)]
    )