from utils.utils import truncate_comment, escape_characters


def parse_issue_comment(json):
    result = None
    action = json['action']
    if action == 'created':
        if json['issue'].get('pull_request') is not None:
            result = notify_new_pull_request_comment(json)
        else:
            result = notify_new_issue_comment(json)
    return result


def notify_new_pull_request_comment(json):
    repository_name = json['repository']['name']
    sender = json['sender']['login']
    text = truncate_comment(json['comment']['body'])
    number = json['issue']['number']
    title = escape_characters(json['issue']['title'])
    comment_url = json['comment']['html_url']

    notification = '🔵 *{}*\n\n💬 {} has commented pull request [#{}: {}]({})\n\n{}'.format(
        repository_name, sender, number, title, comment_url, text)
    return notification


def notify_new_issue_comment(json):
    repository_name = json['repository']['name']
    sender = json['sender']['login']
    text = truncate_comment(json['comment']['body'])
    number = json['issue']['number']
    title = escape_characters(json['issue']['title'])
    comment_url = json['comment']['html_url']

    notification = '🔵 *{}*\n\n💬 {} has commented issue [#{}: {}]({})\n\n{}'.format(
        repository_name, sender, number, title, comment_url, text)
    return notification
