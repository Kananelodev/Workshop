# 🎓 Mock Summative Assessment - Python

## Learning Outcomes Assessed

✅ Understanding of Python syntax  
✅ Conditional statements  
✅ Functions  
✅ Basic and advanced loops  
✅ Data structures (lists, sets, dictionaries)  
✅ Data manipulation  
✅ Debugging and problem solving  

---

## 📋 Assessment Structure

This assessment has two sections:

1. **Coding Assessment** - 6 progressing difficulty questions
2. **Long Questions** - 3 conceptual questions in `answers.txt`

You can answer them in any order.

---

## 🎯 Your Goal

Complete the following:

### For Coding Questions:
- Read the instructions for each coding question
- Implement each function in `mock_exam.py`
- Ensure your code is valid Python
- All unit tests must pass

### For Long Questions:
- Write answers in `answers.txt`
- DO NOT remove comments
- Answer clearly and completely

---

## 🧪 How to Run Your Tests

Run all tests:
```bash
python3 -m pytest tests/test_mock_exam.py -v
```

Run a specific test:
```bash
python3 -m pytest tests/test_mock_exam.py::TestMockExam::test_function_name -v
```

---

---

## 📁 Project Structure

```
Workshop/
├── mock_exam.py          (Complete the functions here)
├── answers.txt           (Answer long questions here)
├── tests/
│   └── test_mock_exam.py (Unit tests)
└── README.md             (This file)
```

---

# 📝 Coding Assessment

Complete all 6 questions of increasing difficulty.

---

## Question 1 - `even_odd_tracker(numbers: list) -> list`

**Difficulty: ⭐ Easy**

Given a list of integers, return a new list where:
- Even numbers become `"Even"`
- Odd numbers become `"Odd"`

**Example:**
```python
Input:  [1, 2, 3, 4]
Output: ["Odd", "Even", "Odd", "Even"]
```

---

## Question 2 - `temperature_filter(temps: list) -> list`

**Difficulty: ⭐⭐ Easy-Medium**

You are given a list of temperatures. Return only temperatures that:
- Are between 18 and 25 (inclusive)
- Ignore any temperature below -50 or above 60

Use loops and conditionals only.

**Example:**
```python
Input:  [10, 18, 22, 30, 61, -100]
Output: [18, 22]
```

---

## Question 3 - `calculate_order_total(price: int, quantity: int) -> int` 

**Difficulty: ⭐⭐ Medium (DEBUG)**

A system calculates order totals. Fix the bugs in this code:

**Rules:**
- Base fee = 10
- Total = base + (price × quantity)
- If quantity is more than 5 → add 20
- Minimum total = 50

**Broken Code:**
```python
def calculate_order_total(price, quantity):
    base = 10
    total = base + price + quantity      # BUG: Should be price * quantity

    if quantity >= 5:
        total = total + 20

    if total < 50:
        total == 50                      # BUG: Should use = not ==

    return total
```

**Example:**
```python
calculate_order_total(100, 1)  → 110
calculate_order_total(10, 5)   → 100 (10 + 10*5 + 20 = 100)
calculate_order_total(5, 2)    → 50  (minimum)
```

---

## Question 4 - `process_scores(scores: list) -> str`

**Difficulty: ⭐⭐⭐ Medium-Hard**

Process scores one by one using a loop.

**Rules:**
- Stop processing if a score below 40 appears
- Otherwise continue through all scores

**Returns:**
- `"Stopped early at score X"` if stopped before completion
- `"All scores processed"` if completed

**Example:**
```python
Input:  [60, 70, 35, 80]
Output: "Stopped early at score 35"

Input:  [45, 50, 55]
Output: "All scores processed"
```

---

## Question 5 - `organize_products(items: list) -> dict`

**Difficulty: ⭐⭐⭐ Hard**

Group products by category. Each item is a dictionary with `name` and `category` keys.

Return a dictionary where:
- Keys are category names
- Values are lists of product names in that category

**Example:**
```python
Input:
[
    {"name": "Milk", "category": "Dairy"},
    {"name": "Cheese", "category": "Dairy"},
    {"name": "Bread", "category": "Bakery"}
]

Output:
{
    "Dairy": ["Milk", "Cheese"],
    "Bakery": ["Bread"]
}
```

---

## Question 6 - `sequence_growth(nums: list) -> int`

**Difficulty: ⭐⭐⭐⭐ Advanced**

Return the length of the longest strictly increasing consecutive sequence.

**Example:**
```python
Input:  [3, 4, 5, 1, 2]
Output: 3  (the sequence 3→4→5)

Input:  [1, 2, 3, 4, 5]
Output: 5  (entire list)

Input:  [5, 4, 3, 2, 1]
Output: 1  (no increasing sequence)
```

---

# ✍️ Long Questions

Answer these questions in `answers.txt`. Your answers should be clear, complete, and demonstrate understanding.

---

## Question 1 — Debugging Concepts

Explain the following in your own words:

1. What is a **syntax error**?
2. What is a **logical error**?
3. Why are logical errors harder to detect than syntax errors?
4. Describe your step-by-step debugging process

**Marks: 4**

---

## Question 2 — Loops & Control Flow

Explain the following:

1. What is the difference between `for` and `while` loops?
2. When should you use each type?
3. Why does the order of conditions matter in control flow?
4. What is the difference between `if`, `elif`, and multiple `if` statements?

**Marks: 4**

---

## Question 3 — Data Structures

Explain the following:

1. When would you use a **list**?
2. When would you use a **set**?
3. When would you use a **dictionary**?
4. Give real-world examples for each

**Marks: 4**

---

## Total Marks: 12



## Instructions Reminder

* Read carefully before coding
* Think through edge cases
* Test your logic step-by-step
* Keep your code clean and readable

Good luck.
