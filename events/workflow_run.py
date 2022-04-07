from utils.utils import escape_characters


def parse_workflow_run(json):
    result = None
    if json['workflow_run']['status'] == 'completed' and json['workflow_run']['conclusion'] == 'failure':
        result = notify_failed_workflow(json)
    return result


def notify_failed_workflow(json):
    repository_name = json['repository']['name']
    workflow_name = escape_characters(json['workflow_run']['name'])
    workflow_run = escape_characters(
        json['workflow_run']['head_commit']['message'])
    html_url = json['workflow_run']['html_url']

    notification = '🔵 *{}*\n\n❌ Workflow *{}* run [{}]({}) has failed.'.format(
        repository_name, workflow_name, workflow_run, html_url)
    return notification
