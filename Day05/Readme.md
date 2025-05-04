# 🔐 Password Generator Project

This project is a Python-based **Password Generator** that lets users generate secure and randomized passwords using letters, numbers, and symbols. It gives you full control over how many characters of each type you want in your password, ensuring flexibility and safety.

---

## 🚀 Features

- Accepts user input for:
  - Number of **letters** (uppercase & lowercase)
  - Number of **numbers** (0–9)
  - Number of **symbols** (!, @, #, etc.)
- Two password generation styles:
  - ✅ **Easy Mode**: Characters are added in a fixed sequence (letters → numbers → symbols)
  - ✅ **Hard Mode**: Characters are shuffled for maximum randomness
- Uses the built-in `random` module for selection and shuffling

---

## 🛠️ How It Works

1. The user specifies how many letters, numbers, and symbols the password should have.
2. The program randomly picks characters from each category.
3. It then shuffles the list of characters (in hard mode) to prevent predictable sequences.
4. Finally, it joins them into a secure password and prints it.

---

## 📦 Example

