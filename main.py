def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    dict_list = convert_dict_to_list_dicts(count_chars(file_contents))
    dict_list.sort(reverse=True, key=sort_on)

    for item in dict_list:
        print(f"'The '{item["char"]}' character was found {item["num"]} times")
 

def convert_dict_to_list_dicts(dict):
    item_list = []
    for k,v in dict.items():
        mydict = {
            "char": k,
            "num": v,
        }
        item_list.append(mydict)
    return item_list 
    
    



def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_dict = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def print_dict(dict):
    for k,v in dict.items():
        print(f"- ''{k}': {v}'") 

def sort_on(dict):
    return dict["num"]

main()
