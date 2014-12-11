{
    'name': 'Website Product Attachments',
    'description': 'This module adds multiple product attachments/files into a tab in product.template in a tab called Product Attachments, and allows for the display of product attachments/files on the product view page.',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch and Cristian Sebastian Rocha',
    'depends': ['product','sale'],
    'data': [
        'views/product_attachments.xml',
        'views/website_product_attachments.xml',
    ],
    'application': True,
}
