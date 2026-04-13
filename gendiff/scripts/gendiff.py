import argparse
import json
from pathlib import Path

def generate_diff(file1, file2):

    first_file = json.load(open(file1))
    second_file = json.load(open(file2))
    
    deleted_keys = set(first_file.keys()) - set(second_file.keys())
    added_keys = set(second_file.keys()) - set(first_file.keys())
    shared_keys = set(first_file.keys()) & set(second_file.keys())
    for k in shared_keys:
        if first_file[k] != second_file[k]:
            deleted_keys.add(k)
            added_keys.add(k)

    output = {f"- {k}": first_file[k] for k in sorted(deleted_keys)} | {f"+ {k}": second_file[k] for k in sorted(added_keys)}

    print(output)
    #print(json.dumps(output, indent=4))
    # for k, v in output.items():
    #     print(f"{k}: {v}")

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
        )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument('-f', '--format', help="set format of output")

    args = parser.parse_args()
    
    generate_diff(args.first_file, args.second_file)

if __name__ == "__main__":
    main()
