class InvalidArgumentException(Exception):
    pass


class NoteUnavailableException(Exception):
    pass


def dispence(num: str):
    if not num:
        return []

    if num == '0':
        return []

    try:
        int(num[0])
    except ValueError:
        raise InvalidArgumentException()

    try:
        if num[-1] != '0':
            raise NoteUnavailableException()
        
        return [int(num)]
    except ValueError:
        raise InvalidArgumentException()

    return []
