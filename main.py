import sys
from stats import get_num_words, get_char_list, list_of_dictionaries 

def main():
    if len(sys.argv) != 2 :
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    path = sys.argv[1] # got the path here
    words = get_book_text(path) # function calling variable for pathfile
    num_text = get_num_words(words) # function in stats, calling pathfile to variable for number of words
    charac = get_char_list(words) # put dict in variable from stats.py
    newest_list = list_of_dictionaries(charac)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_text} total words")
    print("--------- Character Count -------")
    # Loop through your sorted list here
    for item in newest_list:
    # Check if the character is alphabetical
        if item["char"].isalpha():
        # Print in the format "e: 44538"
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read() 
        return file_contents
    
main() # call main operation