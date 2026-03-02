from odoo import models, fields

class CoachingClass(models.Model):
    _name = 'coaching.class'
    _description = 'Coaching Class'

    name = fields.Char(string='Class Name', required=True)
    code = fields.Char(string='Code')
    
    student_ids = fields.One2many(
        'res.partner',
        'coaching_class_id',
        domain=[('is_coaching_student', '=', True)]
    )
    
    subject_ids = fields.One2many('coaching.subject', 'class_id')
    
    def action_coaching_students(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'view_mode': 'list,form',
            'res_model': 'res.partner',
            'domain': [('coaching_class_id', '=', self.id)],
            'context': "{'create': False}"
        }