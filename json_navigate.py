import json
import jmespath


def data_loading(file):
    with open(file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def recursive_items(data, prev=''):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                pre_prev = prev
                prev += key + '.'
                yield from recursive_items(value, prev)
                prev = pre_prev
            elif isinstance(value, list) and value:
                if isinstance(value[0], dict):
                    prev += key + '[].'
                    for dct in value:
                        yield from recursive_items(dct, prev)
                else:
                    yield prev + key, value
            else:
                yield prev + key, value
    else:
        for dct in data:
            yield from recursive_items(dct)


def display_keys(data):
    for key, _ in recursive_items(data):
        print(key)


def goto_field(data, key):
    val = jmespath.search(f"[*].{key}", data)
    return val


def main():
    data = data_loading('twitter1.json')
    display_keys(data)
    print(goto_field(data, 'retweeted_status'))


if __name__ == '__main__':
    main()
