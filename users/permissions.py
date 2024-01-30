from rest_access_policy import AccessPolicy


class UserAccessPolicy(AccessPolicy):
    statements = [
        {
            'action': ['<safe_methods>'],
            'principal': '*',
            'effect': 'allow',
        },
        {
            'action': ['create', 'destroy', 'partial_update', 'update'],
            'principal': ['authenticated'],
            'effect': 'allow',
        }
    ]
