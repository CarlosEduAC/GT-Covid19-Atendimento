import re

def get_real_data(data: list) -> list:
    return list(map(format_real_data, filter(filter_real_data, data)))


def get_others_data(data: list) -> list:
    return list(filter(filter_others_data, data))


def filter_real_data(data: str) -> bool:
    return 'real_data_' in data


def filter_others_data(data: str) -> bool:
    return not filter_real_data(data)


def format_real_data(data: str) -> int:
    return int(data.replace('real_data_', ''))


def data_or_null(data: str, cast=None):
    if cast is None:
        cast = str

    return cast(data) if len(data) != 0 else None


def only_num(data: str):
    if data is None:
        return None

    return re.sub('[^\\d]', '', data)


def multiselect(form, name: str, size) -> list:
    ret = []

    for i in range(1, int(size) + 1):
        name = '{}_{}'.format(name, i).replace('_1', '')
        if name in form:
            ret.append(data_or_null(form[name]))
        else:
            ret.append(None)

    return ret