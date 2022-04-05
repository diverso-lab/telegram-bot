def parse_pull_request(json):
    result = None
    action = json['action']
    if action == 'opened':
        result = notify_opened_pr(json)
    if action == 'closed':
        if json['pull_request']['merged']:
            result = notify_merged_pr(json)
        else:
            result = notify_closed_pr(json)
    if action == 'reopened':
        result = notify_reopened_pr(json)
    if action == 'edited':
        result = notify_edited_pr(json)
    return result


def notify_opened_pr(json):
    title = json['pull_request']['title']
    number = json['pull_request']['number']
    base_label = json['pull_request']['base']['label']
    head_label = json['pull_request']['head']['label']
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '{}\n\nPull request "#{}:{}" from {} into {} has been opened.\n\n{}'.format(
        repository_name, number, title, head_label, base_label, html_url)
    return notification


def notify_merged_pr(json):
    title = json['pull_request']['title']
    number = json['pull_request']['number']
    base_label = json['pull_request']['base']['label']
    head_label = json['pull_request']['head']['label']
    repository_name = json['repository']['name']
    notification = '{}\n\nPull request "#{}:{}" from {} has been merged into {}.'.format(
        repository_name, number, title, head_label, base_label)
    return notification


def notify_closed_pr(json):
    title = json['pull_request']['title']
    number = json['pull_request']['number']
    repository_name = json['repository']['name']
    notification = '{}\n\nPull request "#{}:{}" has been closed.'.format(
        repository_name, number, title)
    return notification


def notify_reopened_pr(json):
    title = json['pull_request']['title']
    number = json['pull_request']['number']
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '{}\n\nPull request "#{}:{}" has been reopened.\n\n{}'.format(
        repository_name, number, title, html_url)
    return notification


def notify_edited_pr(json):
    old_title = json['changes']['title']['from']
    title = json['pull_request']['title']
    number = json['pull_request']['number']
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '{}\n\nPull request "#{}:{}" has been edited to {}.\n\n{}'.format(
        repository_name, number, old_title, title, html_url)
    return notification
