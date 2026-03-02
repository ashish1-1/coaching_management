from odoo import models, fields

class CoachingFeeStructure(models.Model):
    _name = 'coaching.fee.structure'
    _description = 'Fee Structure'

    name = fields.Char(string='Fee Name', required=True)
    amount = fields.Float(string='Amount', required=True)

    class_id = fields.Many2one(
        'coaching.class',
        string='Class',
        required=True
    )

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
        help="Used for invoice line"
    )
