print("____________________________________________")
print("|                                          |")
print("|            DUPLICATE DATA FINDER         |")
print("|__________________________________________|")
from collections import Counter
import os
def process_entries():
  filename = input("Enter the filename (e.g., data.txt): ").strip()
  # Handle missing file error
  try:
    with open(filename, 'r', encoding='utf-8') as f:
      lines = f.readlines()
  except FileNotFoundError:
    print(f'(a) File \'{filename}\' not found. Please enter a valid filename.')
    return 
  # Handle empty file error
  # Strip newlines to see if there is any actual content 
  cleaned_lines = [line.strip() for line in lines if line.strip()]
  if not cleaned_lines:
    print("(b) File is empty. Nothing to check.")
    return
  print('\nMenu options:')
  print('1. Exact match')
  print('2. Ignore case and extra spaces')
  choice = input('Select menu option (1 or 2): ').strip()
  processed_entries = []
  original_mapping = {} # To keep track of original representations for display
  for line in lines:
    original = line.strip()
    if not original:
      continue # skip blank lines
    if choice == '2':
      # Ignore case and extra spaces
      normalized = ' '.join(original.split()).lower()
    else:
      # Exact match      
      normalized = original
    processed_entries.append(normalized)
    # Store the first seen original representation for clean output
    if normalized not in original_mapping:
      original_mapping[normalized] = original
  total_items = len(processed_entries)
  unique_set = set(processed_entries)
  unique_items = len(unique_set)
  # Count frequencies using a loop / Counter
  counts = Counter(processed_entries)
  # Find duplicates (items with count > 1)
  duplicates = {item: count for item, count in counts.items() if count > 1}
  print(f'\nTotal items: {total_items} | Unique items: {unique_items}')
  if duplicates:
    dup_str_parts = []
    for item, count in duplicates.items():
      orig_name = original_mapping[item]
      dup_str_parts.append(f'{orig_name} ({count} times)')
    print(f'Duplicates: {" |".join(dup_str_parts)}')
  else:
    print("No duplicates found.")
  # Save unique entries to unique.txt
  # Keeping original formatting for the saved unique list
  unique_to_save =[original_mapping[item] for item in sorted(unique_set, key=processed_entries.index)]
  with open('unique.txt', 'w', encoding='utf-8') as f_out:
    for item in unique_to_save:
      f_out.write(item + '\n') 
  print("Unique list saved to 'unique.txt")
if __name__ == "__main__":
  process_entries()  