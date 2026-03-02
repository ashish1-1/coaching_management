from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Coaching roles
    is_coaching_student = fields.Boolean("Student")
    is_coaching_teacher = fields.Boolean("Teacher")
    is_coaching_guardian = fields.Boolean("Guardian")

    # Student-specific
    coaching_class_id = fields.Many2one(
        'coaching.class',
        string="Class"
    )

    guardian_ids = fields.Many2many(
        'res.partner',
        'coaching_student_guardian_rel',
        'student_id',
        'guardian_id',
        string="Guardians",
        domain=[('is_coaching_guardian', '=', True)]
    )

    # Guardian side
    student_ids = fields.Many2many(
        'res.partner',
        'coaching_student_guardian_rel',
        'guardian_id',
        'student_id',
        string="Students",
        domain=[('is_coaching_student', '=', True)]
    )
    
    exam_ids = fields.One2many(
        'coaching.exam',
        'student_id',
        string="Exams"
    )
    
    subject_ids = fields.One2many(
        'coaching.subject',
        'teacher_id',
        string="Subjects"
    )