from utils.utils import escape_characters


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
    if action == 'synchronize':
        if json['before'] != json['after']:
            result = notify_new_pr_commit(json)
    return result


def notify_opened_pr(json):
    title = escape_characters(json['pull_request']['title'])
    number = json['pull_request']['number']
    base_label = escape_characters(json['pull_request']['base']['label'])
    head_label = escape_characters(json['pull_request']['head']['label'])
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '🔵 *{}*\n\n🔌 Pull request [#{}: {}]({}) from *{}* into *{}* has been opened.'.format(
        repository_name, number, title, html_url, head_label, base_label)
    return notification


def notify_merged_pr(json):
    title = escape_characters(json['pull_request']['title'])
    number = json['pull_request']['number']
    base_label = escape_characters(json['pull_request']['base']['label'])
    head_label = escape_characters(json['pull_request']['head']['label'])
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '🔵 *{}*\n\n🔌 Pull request [#{}: {}*]({}) from *{}* has been merged into *{}*.'.format(
        repository_name, number, title, html_url, head_label, base_label)
    return notification


def notify_closed_pr(json):
    title = escape_characters(json['pull_request']['title'])
    number = json['pull_request']['number']
    repository_name = json['repository']['name']
    html_url = json['pull_request']['html_url']
    notification = '🔵 *{}*\n\n🔌 Pull request [#{}: {}]({}) has been closed.'.format(
        repository_name, number, title, html_url)
    return notification


def notify_reopened_pr(json):
    title = escape_characters(json['pull_request']['title'])
    number = json['pull_request']['number']
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '🔵 *{}*\n\n🔌 Pull request [#{}: {}]({}) has been reopened.'.format(
        repository_name, number, title, html_url)
    return notification


def notify_edited_pr(json):
    old_title = json['changes']['title']['from']
    title = escape_characters(json['pull_request']['title'])
    number = json['pull_request']['number']
    html_url = json['pull_request']['html_url']
    repository_name = json['repository']['name']
    notification = '🔵 *{}*\n\n🔌 Pull request *#{}: {}* has been edited to [{}]({}).'.format(
        repository_name, number, old_title, title, html_url)
    return notification


def notify_new_pr_commit(json):
    repository_name = json['repository']['name']
    number = json['pull_request']['number']
    title = escape_characters(json['pull_request']['title'])
    pr_html_url = json['pull_request']['html_url']
    commit_html_url = pr_html_url + "/commits/" + json['after']
    notification = '🔵 *{}*\n\n🔌 A [new commit]({}) has been added to pull request [#{}: {}]({})'.format(
        repository_name, commit_html_url, number, title, pr_html_url)
    return notification
