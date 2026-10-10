"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True, remove_duplicates=False):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    if remove_duplicates:
        items = list(set(items))

    return sorted(items, reverse=(not ascending))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending = DEFAULT_ASCENDING
    if len(sys.argv) in (3, 4):
        filename = sys.argv[1]
        duplicate_option = sys.argv[2].lower()
        if duplicate_option not in ("yes", "no"):
            print("The second argument must be yes or no")
            sys.exit(1)
        remove_duplicates = duplicate_option == "yes"
        if len(sys.argv) == 4:
            order_option = sys.argv[3].lower()
            if order_option not in ("asc", "ascending", "desc", "descending"):
                print("The third argument must be asc or desc")
                sys.exit(1)
            ascending = order_option in ("asc", "ascending")
    else:
        print("The filename must be provided as the first argument")
        print("The second argument indicates whether duplicate words should be removed")
        print("The third argument optionally indicates the sort order: asc or desc")
        sys.exit(1)

    print(f"Reading words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list, ascending=ascending, remove_duplicates=remove_duplicates))
