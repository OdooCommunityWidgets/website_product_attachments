from openerp.osv import osv, fields

class product_image(osv.Model):
    _name = 'product.attachment'

    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
        'attachment_alt': fields.text('Attachment Label'),
        'product_attachment': fields.binary('Attachment'),
        'product_tmpl_id': fields.many2one('product.template', 'Product'),
    }
product_attachment()

class product_product(osv.Model):
    _inherit = 'product.product'

    _columns = {
        'product_attachments': fields.related('product_tmpl_id', 'product_attachments', type="one2many", relation="product.attachment", string='Attachments', store=False),
    }
product_product()

class product_template(osv.Model):
    _inherit = 'product.template'
    
    _columns = {
        'product_attachments': fields.one2many('product.attachment', 'product_tmpl_id', string='Attachments'),
    }
product_template()
