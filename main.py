import sys
from stats import get_word_count, count_characters, chars_dict_to_sorted_list

def get_book_text(book_path: str) -> str:
  with open(book_path) as f:
    file_contents = f.read()
  return file_contents

def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(word_count)
  print("--------- Character Count -------")
  for char, count in sorted_list:
    if not char.isalpha():
      continue
    print(f"{char}: {count}")
  print("============= END ===============")


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  word_count = get_word_count(book_text)
  char_count = count_characters(book_text)
  sorted_list = chars_dict_to_sorted_list(char_count)
  report = print_report(book_path, word_count, sorted_list)


main()

