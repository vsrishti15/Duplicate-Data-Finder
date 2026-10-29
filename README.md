# Duplicate Data Finder

## 📌 Overview
Duplicate Data Finder is a Python-based program that identifies duplicate entries in a text file. It counts the total number of entries, determines the number of unique entries, displays duplicate values with their frequencies, and saves the unique entries to a separate file named `unique.txt`.

The program provides two comparison modes: exact matching and case-insensitive matching that ignores extra spaces.

## ✨ Features
- **File Handling:** Reads data from a user-specified text file.
- **Error Handling:** Handles missing files and empty files.
- **Two Comparison Modes:**
  - **Exact Match:** Identifies duplicates based on the original text.
  - **Ignore Case and Extra Spaces:** Treats differences in letter case and extra spaces as equivalent.
- **Duplicate Detection:** Displays duplicate entries and their occurrence counts.
- **Unique Entry Counting:** Calculates the total number of entries and unique entries.
- **Output File Generation:** Saves unique entries to `unique.txt`, preserving their first occurrence and original formatting.
- **Blank Line Handling:** Ignores empty lines in the input file.

## 🛠️ Technologies Used
- Python 3
- `collections.Counter` for counting entry frequencies
- `open()` for file handling
- `os` module (imported in the program)

## 📂 Project Structure

```text
Duplicate-Data-Finder/
│
├── main.py       # Main Python program
├── data.txt      # Input text file (created by the user)
├── unique.txt    # Generated file containing unique entries
└── README.md     # Project documentation
```

## ⚙️ Requirements
- Python 3.x
- A text editor or Python IDE
- An input text file containing the data to be checked

No additional package installation is required because the program uses Python's standard library.

## 🚀 How to Run

1. Save the Python code in a file named `main.py`.
2. Create a text file, such as `data.txt`, containing the entries you want to check.
3. Open a terminal or command prompt in the project directory.
4. Run the program:

   ```bash
   python main.py
   ```

5. Enter the input filename when prompted.
6. Select a comparison mode from the menu.
7. View the results and check the generated `unique.txt` file.

## 📝 Example Input

Suppose `data.txt` contains:

```text
Apple
Banana
apple
Orange
Banana
  Apple
```

## 💻 Example Execution

```text
Enter the filename (e.g., data.txt): data.txt

Menu options:
1. Exact match
2. Ignore case and extra spaces
Select menu option (1 or 2): 2

Total items: 6 | Unique items: 3
Duplicates: Apple (3 times) | Banana (2 times)
Unique list saved to 'unique.txt'
```

## 📄 Output File

After execution, the program generates `unique.txt` containing one representative of each unique entry.

Example:

```text
Apple
Banana
Orange
```

The output preserves the original formatting of the first occurrence of each unique entry.

## 🔍 How It Works

1. Accepts the input filename from the user.
2. Reads the file and removes blank lines.
3. Checks whether the file exists and contains valid entries.
4. Asks the user to select a comparison mode.
5. Normalizes entries when case-insensitive comparison is selected.
6. Counts the frequency of each entry using `Counter`.
7. Identifies duplicates and calculates the total and unique entry counts.
8. Displays the results on the screen.
9. Writes the unique entries to `unique.txt`.

## ⚠️ Limitations
- The program processes text files line by line.
- Each non-empty line is treated as a separate entry.
- The generated `unique.txt` file is overwritten each time the program runs.
- The program does not modify the original input file.
- Invalid menu choices are not explicitly validated in the current implementation.

## 🔮 Future Improvements
- Add validation for menu options.
- Support CSV and Excel files.
- Allow users to choose a custom output filename.
- Generate a detailed duplicate report.
- Add options to sort the output alphabetically.
- Provide a graphical user interface (GUI).

## 🎯 Conclusion
Duplicate Data Finder is a simple and useful Python project for detecting duplicate text entries and extracting unique data. It demonstrates fundamental programming concepts such as file handling, loops, conditional statements, dictionaries, sets, and frequency counting.

## 👩‍💻 Author
**Your Name**
