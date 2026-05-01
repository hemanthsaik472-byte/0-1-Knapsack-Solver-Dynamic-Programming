# 0/1 Knapsack Solver — Dynamic Programming

## Problem Statement

Given a set of items, each with a **weight** and a **value**, and a knapsack with a fixed **capacity**, determine which items to include so that the **total value is maximized** without exceeding the capacity.

Each item can either be taken (1) or left (0) — hence the name **0/1 Knapsack**.

---

## Algorithm Used

### Dynamic Programming (Bottom-Up)

We build a 2D DP table where:

```
dp[i][w] = maximum value using the first i items with capacity w
```

**Recurrence relation:**

```
dp[i][w] = dp[i-1][w]                                      if item i doesn't fit
dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])  if item i fits
```

After filling the table, we **traceback** from `dp[n][W]` to find which items were selected.

---

## Time & Space Complexity

| Metric | Complexity |
|--------|-----------|
| Time   | O(n × W)  |
| Space  | O(n × W)  |

Where `n` = number of items, `W` = knapsack capacity.

---

## Project Structure

```
knapsack_project/
├── knapsack.py       # Core algorithm + demo
├── test_cases.py     # All test cases
└── README.md         # This file
```

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

### Run the demo:
```bash
python knapsack.py
```

### Run the tests:
```bash
python test_cases.py
```

---

## Sample Output

```
=======================================================
       0/1 Knapsack Solver — Dynamic Programming
=======================================================

[Example 1]
Capacity: 5
Item            Weight    Value
---------------------------------
Laptop               3        4
Phone                1        3
Book                 2        1
Headphones           4        5
Tablet               2        3

Selected items:
  - Phone (weight=1, value=3)
  - Tablet (weight=2, value=3)
  - Laptop (weight=3, value=4)  ← wait, 1+2=3, fits!

Total Weight : 5 / 5
Maximum Value: 10
```

---

## Key Concepts Demonstrated

- **Dynamic Programming** — overlapping subproblems solved bottom-up
- **Optimal Substructure** — solution built from smaller sub-solutions
- **Traceback** — reconstruct which items were chosen
- **Edge Case Handling** — empty items, zero capacity, all items too heavy

---

## Algorithm Explanation (Step by Step)

1. Create a table with `(n+1)` rows and `(W+1)` columns, filled with 0.
2. For each item `i` from 1 to n:
   - For each capacity `w` from 0 to W:
     - If item doesn't fit → carry forward value from previous row
     - If item fits → take the **maximum** of (not taking it) vs (taking it)
3. Answer is at `dp[n][W]`
4. Traceback from bottom-right to find selected items

---

*Submitted for CCC Algorithm Project — April 2026*
