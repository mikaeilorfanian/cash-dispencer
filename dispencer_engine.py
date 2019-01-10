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
        
        if len(num) > 2:
            hundreds = int(num[:-2])
            tens = int(num[-2:])
        else:
            hundreds = 0
            tens = int(num)

        notes = [100 for _ in range(hundreds)]

        if tens >= 50:
            notes.append(50)
            tens -= 50

        while tens >= 20:
            notes.append(20)
            tens -= 20

        if tens != 0:
            notes.append(10)
        
        return notes

    except ValueError:
        raise InvalidArgumentException()

    return []
