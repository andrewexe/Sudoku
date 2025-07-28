# Sudoku 📝🔄

---

## 🌐 Overview

This project implements a **Sudoku puzzle validator and solver** using **backtracking recursion**. Given a 9x9 grid, the program determines if the puzzle is valid and solvable, and provides a completed solution if one exists.

---

## 🔍 Features

* ✅ **Validation** of Sudoku puzzles

  * Checks that no duplicates exist in rows, columns, or 3x3 subgrids
  * Ensures input adheres to Sudoku rules before attempting to solve

* ♻️ **Solving with Backtracking**

  * Recursive brute-force search with pruning
  * Efficient early exit if a constraint is violated
  * Supports partially filled puzzles

* 📂 **Input/Output Handling**

  * Reads board from text or command line
  * Outputs clean formatted grid

---

## ⚖️ Time Complexity

* **Validation:** O(n^2), where n = 9
* **Solving:** Worst case O(9^m), where m is the number of empty cells. Pruned heavily with constraint checks.

---

## 📂 Sample Input

```txt
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

### ➡️ Output

```txt
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
```

---

## 💻 How It Works

1. Parse the puzzle into a 2D array
2. Validate the grid for rule violations
3. Recursively place digits 1-9 into empty cells
4. Backtrack if a digit breaks Sudoku rules
5. Continue until solution is found or board is unsolvable

---

## 🚀 Build and Run

```bash
g++ sudoku.cpp -o sudoku
./sudoku input.txt
```

Or run interactively:

```bash
./sudoku
(Then enter each row of the board)
```

---

## 🧪 Future Improvements

* Add GUI with SFML or SDL
* Implement difficulty classification
* Add randomized puzzle generation
* Optimize backtracking with heuristic ordering (e.g., least possible values first)

---

## 📄 File Structure

```
sudoku/
├── sudoku.cpp          # Solver and validator implementation
├── input.txt           # Sample puzzle
├── test_cases.txt      # Optional test suite
├── README.md
```

---

## 👤 Author Info

```
Name: Andrew Huang
System: macOS / Windows / Linux
Compiler: g++
IDE: CLion / VSCode / Terminal
```

---

## 📄 License

MIT License © 2023
