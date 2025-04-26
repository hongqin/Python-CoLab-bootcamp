import os
import filecmp


def get_all_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            files_list.append(relative_path)
    return files_list


def compare_directories(version0, version2):
    files_v0 = set(get_all_files(version0))
    files_v2 = set(get_all_files(version2))

    modified_files = []
    new_files = []

    # Files present in both, check if modified
    common_files = files_v0.intersection(files_v2)
    for file in common_files:
        path_v0 = os.path.join(version0, file)
        path_v2 = os.path.join(version2, file)
        if not filecmp.cmp(path_v0, path_v2, shallow=False):
            modified_files.append(file)

    # Files only in version2
    only_in_v2 = files_v2 - files_v0
    new_files.extend(list(only_in_v2))

    return modified_files, new_files


if __name__ == "__main__":
    version0_dir = "version0"
    version2_dir = "version2"

    modified, new = compare_directories(version0_dir, version2_dir)

    print("Modified files:")
    for f in modified:
        print(f"  {f}")

    print("\nNew files:")
    for f in new:
        print(f"  {f}")

