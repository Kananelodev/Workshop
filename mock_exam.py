
# ==============================================================================
# QUESTION 1: even_odd_tracker(numbers: list) -> list
# ==============================================================================
# Difficulty: ⭐ Easy
#
# Transform a list of integers into a list of "Even" or "Odd" strings
# 
# Example:
#   Input:  [1, 2, 3, 4]
#   Output: ["Odd", "Even", "Odd", "Even"]

def even_odd_tracker(numbers: list) -> list:
    """Convert even/odd numbers to their string representations."""
    pass


# ==============================================================================
# QUESTION 2: temperature_filter(temps: list) -> list
# ==============================================================================
# Difficulty: ⭐⭐ Easy-Medium
#
# Filter temperatures to keep only those between 18-25 (inclusive)
# Ignore temperatures below -50 or above 60
# Use only loops and conditionals
#
# Example:
#   Input:  [10, 18, 22, 30, 61, -100]
#   Output: [18, 22]

def temperature_filter(temps: list) -> list:
    """Filter valid temperatures between 18-25 degrees."""
    pass


# ==============================================================================
# QUESTION 3: calculate_order_total(price: int, quantity: int) -> int
# ==============================================================================
# Difficulty: ⭐⭐ Medium (DEBUG)
#
# Calculate total order cost with these rules:
# - Base fee = 10
# - Total = base + (price × quantity)
# - If quantity > 5: add 20
# - Minimum total = 50
#
# Fix the bugs in this implementation:

def calculate_order_total(price: int, quantity: int) -> int:
    """Calculate order total with fees and minimum."""
    base = 10
    total = base + price + quantity  

    if quantity >= 5:
        total = total + 20

    if total < 50:
        total == 50  

    return total


# ==============================================================================
# QUESTION 4: process_scores(scores: list) -> str
# ==============================================================================
# Difficulty: ⭐⭐⭐ Medium-Hard
#
# Loop through scores and stop if any score is below 40
# Return appropriate message based on whether loop completed
#
# Examples:
#   Input:  [60, 70, 35, 80]
#   Output: "Stopped early at score 35"
#
#   Input:  [45, 50, 55]
#   Output: "All scores processed"

def process_scores(scores: list) -> str:
    """Process scores and stop if any score is below 40."""
    pass


# ==============================================================================
# QUESTION 5: organize_products(items: list) -> dict
# ==============================================================================
# Difficulty: ⭐⭐⭐ Hard
#
# Group products by category
# Each item has 'name' and 'category' keys
# Return dict with categories as keys and lists of names as values
#
# Example:
#   Input:  [
#     {"name": "Milk", "category": "Dairy"},
#     {"name": "Cheese", "category": "Dairy"},
#     {"name": "Bread", "category": "Bakery"}
#   ]
#   Output: {
#     "Dairy": ["Milk", "Cheese"],
#     "Bakery": ["Bread"]
#   }

def organize_products(items: list) -> dict:
    """Group products by their category."""
    pass


# ==============================================================================
# QUESTION 6: sequence_growth(nums: list) -> int
# ==============================================================================
# Difficulty: ⭐⭐⭐⭐ Advanced
#
# Find the length of the longest strictly increasing consecutive sequence
#
# Examples:
#   Input:  [3, 4, 5, 1, 2]
#   Output: 3  (the sequence 3→4→5)
#
#   Input:  [1, 2, 3, 4, 5]
#   Output: 5  (entire list)
#
#   Input:  [5, 4, 3, 2, 1]
#   Output: 1  (no increasing sequence)

def sequence_growth(nums: list) -> int:
    """Find the longest strictly increasing consecutive sequence."""
    pass
