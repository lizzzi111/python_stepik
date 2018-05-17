# put your python code here
import sys
import json
from operator import itemgetter

def get_parents(class_name, input_data):
    for row in input_data:
        if row["name"] == class_name:
            return row["parents"]
    return []


def walk(from_class, to_class, input_data):
    for parent in get_parents(from_class, input_data):
        if parent == to_class:
            return True
        else:
            part = walk(parent, to_class, input_data)
            if part:
                return part
    return False


def main():
    data_json = sys.stdin.read()
    data = json.loads(data_json)
    result_dict = {}
    for i in data:
        for j in data:
            a = i["name"]
            b = j["name"]
            if b not in result_dict:
                result_dict[b] = 1
            if a != b and walk(a, b, data):
                result_dict[b] += 1
    results = []
    for key in result_dict:
        results.append({"key": key, "value": result_dict[key]})
    result_sort = sorted(results, key=lambda x: x['key'])
    for i in result_sort:
        print(i["key"], ":", i["value"])


main()




