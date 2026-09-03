def get_word_count(book_text: str) -> int:
  words = book_text.split()
  return f"Found {len(words)} total words"

def count_characters(book_text: str) -> dict[str, int]:
  char_count = {}
  for char in book_text:
    lowered_char = char.lower()
    if lowered_char in char_count:
      char_count[lowered_char] += 1
    else:
      char_count[lowered_char] = 1
  return char_count

def sort_on(item: tuple[str, int]) -> int:
  return item[1]

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
  count_list = []
  for char in char_count.keys():
    count = char_count[char]
    count_list.append((char, count))
  sorted_list = sorted(count_list, reverse=True, key=sort_on)
  return sorted_list