MAX_COMMENT_LENGTH = 200


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
    sender = json['sender']['login']
    text = truncate_comment(json['comment']['body'])
    number = json['issue']['number']
    title = json['issue']['title']

    notification = '{} has commented pull request "#{}:{}":\n\n{}.'.format(
        sender, number, title, text)
    return notification


def notify_new_issue_comment(json):
    sender = json['sender']['login']
    text = truncate_comment(json['comment']['body'])
    number = json['issue']['number']
    title = json['issue']['title']

    notification = '{} has commented issue "#{}:{}":\n\n{}.'.format(
        sender, number, title, text)
    return notification


def truncate_comment(comment):
    return comment[:MAX_COMMENT_LENGTH] + ".." if len(comment) > MAX_COMMENT_LENGTH else comment
