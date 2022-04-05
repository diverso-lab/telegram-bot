def parse_issue(json):
    result = None
    action = json['action']
    if action == 'opened':
        result = notify_opened_issue(json)
    if action == 'edited':
        result = notify_edited_issue(json)
    if action == 'deleted':
        result = notify_deleted_issue(json)
    if action == 'closed':
        result = notify_closed_issue(json)
    if action == 'reopened':
        result = notify_reopened_issue(json)
    return result


def notify_opened_issue(json):
    number = json['issue']['number']
    title = json['issue']['title']
    sender = json['sender']['login']
    repository_name = json['repository']['name']
    issue_url = json['issue']['html_url']
    notification = '{}\n\nIssue #{}:"{}" has been opened by {}.\n\n{}'.format(
        repository_name, number, title, sender, issue_url)
    return notification


def notify_edited_issue(json):
    number = json['issue']['number']
    old_title = json['changes']['title']['from']
    title = json['issue']['title']
    repository_name = json['repository']['name']
    issue_url = json['issue']['html_url']
    notification = None
    if old_title != title:
        notification = '{}\n\nIssue #{}:"{}" has been edited to "{}".\n\n{}'.format(
            repository_name, number, old_title, title, issue_url)
    return notification


def notify_deleted_issue(json):
    number = json['issue']['number']
    title = json['issue']['title']
    repository_name = json['repository']['name']
    notification = '{}\n\nIssue #{}:"{}" has been deleted.'.format(
        repository_name, number, title)
    return notification


def notify_closed_issue(json):
    number = json['issue']['number']
    title = json['issue']['title']
    repository_name = json['repository']['name']
    sender = json['sender']['login']
    issue_url = json['issue']['html_url']
    notification = '{}\n\nIssue #{}:"{}" has been closed by {}.\n\n{}'.format(
        repository_name, number, title, sender, issue_url)
    return notification


def notify_reopened_issue(json):
    number = json['issue']['number']
    title = json['issue']['title']
    repository_name = json['repository']['name']
    sender = json['sender']['login']
    issue_url = json['issue']['html_url']
    notification = '{}\n\nIssue #{}:"{}" has been reopened by {}.\n\n{}'.format(
        repository_name, number, title, sender, issue_url)
    return notification
