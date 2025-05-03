# 🐍 Day 4: Python Learning and Mini Projects

## 📚 Topics Covered

Today’s focus was on **Randomisation**, the **random module**, and an introduction to the **List** data type. I explored how to use external modules, especially Python’s built-in `random` module, and worked on practical mini-projects to apply these concepts.

### ✅ Concepts Learned

- What is a **Module** in Python
- Purpose of **importing modules**
- Using the `random` module: `random.randint()`, `random.choice()`, `random.shuffle()`, etc.
- Writing a **Heads or Tails** program
- Working with **Lists**:
  - Accessing list elements using **indexes**
  - **Changing** list elements
  - **Appending** items to a list
- Writing mini programs using random and list together:
  - **Who Pays the Bill** – a fun random name picker
  - **Rock, Paper, Scissors** game – user vs computer logic

---
📝 Summary
Learned how Python modules work and why they’re important.

Understood the use of the random module in creating interactive and fun scripts.

Practiced with lists — indexing, modifying, and appending.

Built engaging beginner-level mini games using randomness and user input.

## 🧪 Mini Projects

### 1️⃣ Heads or Tails

A simple script that simulates a coin toss using `random.randint()`.

```python
import random

toss = random.randint(0, 1)
if toss == 1:
    print("Heads")
else:
    print("Tails")


