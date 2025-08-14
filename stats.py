def get_number_of_words(book_path):
    with open(book_path) as text:
        return len(text.read().split())
    
def get_number_of_characters(book_path):
    with open(book_path) as text:
        char_counts = {}
        for character in str.lower(text.read()):
            char_counts[character] = char_counts.get(character, 0) + 1
        return char_counts
            
def get_sorted_list_of_dictionaries(book_name):
    char_counts = get_number_of_characters(book_name)
    sorted_characters = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters
 
    
        