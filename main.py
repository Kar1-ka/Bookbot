from stats import get_num_words, get_char_list
def main():
    path = "books/frankenstein.txt" # got the path here
    words = get_book_text(path) # function calling variable for pathfile
    num_text = get_num_words(words) # function in stats, calling pathfile to variable for number of words
    charac = get_char_list(words) # put dict in variable from stats.py
    print (f"{num_text} words found in the document") # print the num of words in document
    print (f"{charac}") # print the dict

def get_book_text(path):
    
    with open(path) as f:
        file_contents = f.read() 
        return file_contents
    




    
main() # call main operation