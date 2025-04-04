from stats import get_num_words
from stats import get_char_count
from stats import sort_dict_list
import sys

def get_book_text(filename_path):
  with open(filename_path) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  text = get_book_text(book_path)
  num_words = get_num_words(text) 
  char_count = get_char_count(text)
  sorted_list = sort_dict_list(char_count)


  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in sorted_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["count"]}")

  
main()
