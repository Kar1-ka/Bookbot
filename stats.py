def get_num_words(words): 
    num_in_text = words.split()
    num = len(num_in_text)
    return num

def get_char_list (alphabets): # words "string" in function
    chara_dict = {}  # start new dict
    for characters in alphabets: # words in full book string
        lowercase_chara = characters.lower() #lowercase all words
        if lowercase_chara not in chara_dict: # if lowercase charachters not in dictionary
            chara_dict[lowercase_chara] = 1 # add the key as chara and add the value as +1
        elif lowercase_chara in chara_dict: # else if in the dictionary
            chara_dict[lowercase_chara] +=1 # add the value
    return chara_dict # return the dictionary with key and values for all chara
        
def sort_list(new_dict):
    return new_dict["num"]

def list_of_dictionaries(chara_dict):
    new_list = []
    for char in chara_dict:
        count_num = chara_dict[char]
        new_dict = {"char": char, "num":count_num}
        new_list.append(new_dict)
    new_list.sort(reverse= True, key = sort_list)
    return new_list
