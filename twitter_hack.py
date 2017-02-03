# coding: utf-8

# See: https://forum.omz-software.com/topic/2794/old-bugs/19

import twitter
account = twitter.get_all_accounts()[0]
fmt = '''> user: {user[screen_name]}
{text}
________________________>'''


def perform_search():
    data = twitter.search(account, 'Privacy OR Apple from:RepTedLieu',
                          parameters={'result_type': 'mixed'})
    print('\n'.join(fmt.format(**status) for status in data['statuses']))


perform_search()
