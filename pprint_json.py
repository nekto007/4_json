import json
import sys

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as json_data:
        json_data = json_data.read()
    return json_data


def pretty_print_json(data):
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    json_result = load_data(sys.argv[1])
    pretty_print_json(json_result)
