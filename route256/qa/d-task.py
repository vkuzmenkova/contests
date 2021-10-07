# Найти значение элемента по переданному пути
import json


def get_by_dotted_path(container, path: str):
    tmp = 'container'

    if path == '':
        return None
    for key in path.split('.'):
        if key.isdigit() and type(eval(tmp)) is list:
            tmp += f'[{int(key)}]'
        else:
            tmp += f'[\'{key}\']'

    return eval(tmp)


if __name__ == "__main__":
    input_str = input()
    [container, path] = json.loads(input_str)

    try:
        answer = get_by_dotted_path(container, path)
    except LookupError:
        answer = 'LookupError'
    except TypeError:
        answer = 'LookupError'

    print(json.dumps(answer))
