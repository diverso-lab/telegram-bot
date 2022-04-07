import os

MAX_COMMENT_LENGTH = int(os.environ['MAX_COMMENT_LENGTH'])


def truncate_comment(comment):
    return comment[:MAX_COMMENT_LENGTH] + ".." if len(comment) > MAX_COMMENT_LENGTH else comment


def escape_characters(text):
    result = text
    characters = ['_', '*', '`', '[']
    for character in characters:
        result = str(result).replace(character, '\{}'.format(character))
    return result
