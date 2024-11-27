{
    'name': 'Project Invoice Linking',
    'version': '1.0',
    'category': 'Project Management',
    'summary': 'Link invoices to tasks, phases, and projects for accurate cost calculation.',
    'author': 'Your Name',
    'depends': ['project', 'account'],
    'data': [
        'views/project_views.xml',
        'views/invoice_views.xml'
    ],
    'installable': True,
    'application': False
}
