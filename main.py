import sys
from stats import get_number_of_words
from stats import get_sorted_list_of_dictionaries


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    print("----------- Word Count ----------")
    print(f'Found {get_number_of_words(sys.argv[1])} total words')
    print("--------- Character Count -------")

    for char, count in get_sorted_list_of_dictionaries(sys.argv[1]):
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")
    
 
main()