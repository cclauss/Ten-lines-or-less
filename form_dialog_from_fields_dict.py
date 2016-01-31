# coding: utf-8

import collections, dialogs

# simplify the creation of simple form_dialogs
    
def form_dialog_from_fields_dict(title, fields_dict):
    return dialogs.form_dialog(title, [{'title': k, 'type': v}
        for k, v in fields_dict.iteritems()])

# left side is the field name
# right side is the field data type
my_fields_dict = collections.OrderedDict((
    ('name',          'text'),
    ('age',           'number'),
    ('developer',     'switch'),
    ('web page',      'url'),
    ('email address', 'email'),
    ('password',      'password'),
    ('check',         'check'),
    ('datetime',      'datetime'),
    ('date',          'date'),
    ('time',          'time')))

print(form_dialog_from_fields_dict('My form dialog', my_fields_dict))
