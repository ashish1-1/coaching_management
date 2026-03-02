from odoo import models, fields, api

class CoachingStudentFee(models.Model):
    _name = 'coaching.student.fee'
    _description = 'Student Fee'
    _rec_name = 'student_id'

    student_id = fields.Many2one(
        'res.partner',
        string='Student',
        domain=[('is_coaching_student', '=', True)],
        required=True
    )

    fee_structure_id = fields.Many2one(
        'coaching.fee.structure',
        string='Fee',
        required=True
    )

    amount = fields.Float(
        related='fee_structure_id.amount',
        store=True
    )

    invoice_id = fields.Many2one(
        'account.move',
        string='Invoice',
        readonly=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('invoiced', 'Invoiced'),
            ('paid', 'Paid')
        ],
        compute='_compute_state',
        store=True
    )
    
    @api.depends('invoice_id.payment_state', 'invoice_id.state')
    def _compute_state(self):
        for rec in self:
            if not rec.invoice_id:
                rec.state = 'draft'
            elif rec.invoice_id.payment_state == 'paid':
                rec.state = 'paid'
            else:
                rec.state = 'invoiced'

    def action_create_invoice(self):
        for rec in self:
            if rec.invoice_id:
                continue

            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': rec.student_id.id,
                'invoice_line_ids': [(0, 0, {
                    'product_id': rec.fee_structure_id.product_id.id,
                    'quantity': 1,
                    'price_unit': rec.amount,
                })]
            })

            rec.invoice_id = invoice.id
            rec.state = 'invoiced'