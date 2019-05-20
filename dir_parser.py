import json
import os
import argparse

def path_2_json(base_path):
    """Path to json converter (non-recursive)."""
    initial = {
        "name": os.path.basename(base_path),
        "path": os.path.abspath(base_path),
    }
    stack = [initial]
    while stack:
        last = stack.pop()
        try:
            list_of_dir = os.listdir(last["path"])
        except NotADirectoryError:
            last['type'] = "file"
        else:
            last['type'] = "directory"
            last['children'] = []
            for elem in list_of_dir:
                temp_dir = {
                    'name': os.path.basename(elem),
                    'path': os.path.join(last['path'], elem)
                }
                last['children'].append(temp_dir)
                stack.append(temp_dir)

    return json.dumps(initial, indent=4, separators=(',', ':'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory")
    args = parser.parse_args()
    print(path_2_json(args.directory))
