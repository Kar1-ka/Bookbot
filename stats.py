def get_num_words(words): 
    num_in_text = words.split()
    num = len(num_in_text)
    return num

def get_char_list (alphabets):
    chara_dict = {}
    for characters in alphabets:
        lowercase_chara = characters.lower()
        if lowercase_chara not in chara_dict:
            chara_dict[lowercase_chara] = 1
        elif lowercase_chara in chara_dict:
            chara_dict[lowercase_chara] +=1
    return chara_dict
        

        
