# 📚 BookBot

BookBot is a simple Python program that analyzes the number of words and characters in a text file.  
This project was created as a practice exercise for the [Boot.dev](https://www.boot.dev) course.

---

## ✨ Features

- 📝 Counts the total number of words in a text file.
- 🔤 Counts the frequency of each character.
- 📊 Outputs characters sorted by frequency (most frequent first).
- 🚫 Ignores non-alphabetical characters in the character frequency output.

---

## ▶️ Usage

1. **Place** a text file (e.g., `book.txt`) in the project directory.
2. **Run** the program with the path to the file:
   ```bash
   python3 main.py <path_to_text_file>
   ```
   **Example:**
   ```bash
   python3 main.py book.txt
   ```

3. **Example output:**
   ```text
   ============ BOOKBOT ============
   Analyzing book found at book.txt...
   ----------- Word Count ----------
   Found 5234 total words
   --------- Character Count -------
   e: 3421
   t: 2789
   a: 2450
   ...
   ============= END ===============
   ```

---
