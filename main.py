
def main():
  book_path = "./books/frakenstein.txt"
  text = get_book_content(book_path)
  word_count = get_word_count(text)
  char_dict = get_char_count(text)

  list_char_dict = transform_dict_to_sorted_list(char_dict)

  pretty_print(book_path, word_count, list_char_dict)
  
def get_book_content(path):
  with open(path) as f:
    return f.read()
  
def get_word_count(content: str):
  word_count = len(content.split())
  return word_count

def get_char_count(content: str):
  char_dict = {}
  lowered = content.lower()
  for char in lowered:
    if char not in char_dict:
      char_dict[char] = 0
    
    char_dict[char] += 1

  return char_dict

def sort_on(dict):
  return dict["count"]

def transform_dict_to_sorted_list(dict):
  list = []
  for item in dict:
    list.append({
      "name": item,
      "count": dict[item]
    })

  list.sort(reverse=True, key=sort_on)
  return list

def pretty_print(book_path: str, word_count: int, char_dict: list):
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document\n")

  for item in char_dict:
    if item["name"].isalpha():
      print(f"The '{item["name"]}' character was found {item["count"]} times")

  print("--- End report ---")


main()


