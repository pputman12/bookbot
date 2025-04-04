def get_num_words(text):
  return len(text.split())

def get_char_count(text):
  word_count_dict = {}
  for word in text.split():
    word = word.lower()
    for char in word:
      if char not in word_count_dict:
        word_count_dict[char] = 1
      else:
        word_count_dict[char] += 1
  return word_count_dict

def sort_dict_list(mydict):
  my_list = []
  for item in mydict:
    temp_dict = {}
    temp_dict["char"] = item
    temp_dict["count"] = mydict[item]
    my_list.append(temp_dict)
  return my_list
