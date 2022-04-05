from events.issues import parse_issue
from events.issue_comment import parse_issue_comment
from events.pull_request import parse_pull_request
from events.workflow_run import parse_workflow_run


def handle_request(event, json):
    result = None
    if event == 'issues':
        result = parse_issue(json)
    if event == 'issue_comment':
        result = parse_issue_comment(json)
    if event == 'pull_request':
        result = parse_pull_request(json)
    if event == 'workflow_run':
        result = parse_workflow_run(json)
    return result
