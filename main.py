def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    counted = count_char(file_contents)


    counted_list = convert_dict_to_list(counted)
    counted_list.sort(reverse=True, key=sort_on)
    
    for dict in counted_list:
        char   = dict["char"]
        number = dict["num"]
        print(f"'{char}': {number}")	
                

def count_char(file_contents):
    count = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in file_contents:
        char = char.lower()
        if char in alphabet:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count 
     
def sort_on(dict):
    return dict["num"]


def convert_dict_to_list(dict):
    dict_list = []
    for k,v in dict.items():
        entry = {
            "char": k,
            "num": v,
        }
        dict_list.append(entry)
    return dict_list

main()
