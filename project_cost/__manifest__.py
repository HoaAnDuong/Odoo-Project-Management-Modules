{
    'name': 'Project Cost Management',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Project',
    'summary': 'Manage costs for tasks, stages, and projects',
    'depends': ['project', 'account'],
    'data': [
        'views/project_task_views.xml',
        'views/project_stage_views.xml',
        'views/project_project_views.xml',
    ],
    'installable': True,
    'application': False,
}
