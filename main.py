def main():
    path = "books/frankenstein.txt"
    words = get_book_text(path)
    num_text = num_in_string(words)
    print (f"{num_text} words found in the document")
    
def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def num_in_string(words): 
    num_in_text = words.split()
    num = len(num_in_text)
    return num



    
main()