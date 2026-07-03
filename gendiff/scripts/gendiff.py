import argparse
from gendiff.parser import parse_file


def generate_diff(file1, file2):
    first_file = parse_file(file1)
    second_file = parse_file(file2)

    deleted_keys = set(first_file.keys()) - set(second_file.keys())
    added_keys = set(second_file.keys()) - set(first_file.keys())
    shared_keys = set(first_file.keys()) & set(second_file.keys())
    for k in shared_keys:
        if first_file[k] != second_file[k]:
            deleted_keys.add(k)
            added_keys.add(k)
    unchanged_keys = shared_keys - deleted_keys - added_keys

    diff_dict = {}

    total_keys = set(first_file.keys()) | set(second_file.keys())
    for k in sorted(total_keys):
        if k in deleted_keys:
            diff_dict[f"- {k}"] = first_file[k]
        if k in added_keys:
            diff_dict[f"+ {k}"] = second_file[k]
        elif k in unchanged_keys:
            diff_dict[f"  {k}"] = first_file[k]

    print("{")
    for key, value in diff_dict.items():
        print(f"  {key}: {value}")
    print("}")

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
