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
    if isinstance(data, dict):
        val = jmespath.search(f"{key}", data)
    elif isinstance(data, list):
        val = jmespath.search(f"[*].{key}", data)
    return val


def check_way(way: str):
    way_lst = way.split()
    if way_lst[0] == 'cd' and len(way_lst) == 2:
        return True

    return False


def main():
    while True:
        print('\033[96m' + f"Put the name of JSON file you'd like to navigate through" + '\033[0m')
        file_name = input('>>> ')
        try:
            data = data_loading(file_name)
            break
        except FileNotFoundError:
            print('\033[96m' + "The file does not exist. Try again..." + '\033[0m')
            continue
    display_keys(data)
    print('\033[96m' + 'cd <total path to the key>\n'
                       'ls  # to see ALL the keys' + '\033[0m')
    while True:
        str_jmes = input('>>> ')
        res_lst = str_jmes.split()
        if res_lst[0] == 'cd' and len(res_lst) == 2:
            content = goto_field(data, res_lst[1])
            js_content = json.dumps(content, indent=4)
            print(js_content)
        elif res_lst[0] == 'cd' and len(res_lst) == 1:
            continue
        elif str_jmes == 'ls':
            display_keys(data)
        else:
            print('\033[96m' + "command not found" + '\033[0m')
            continue


if __name__ == '__main__':
    main()
