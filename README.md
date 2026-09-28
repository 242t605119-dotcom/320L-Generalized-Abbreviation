# LeetCode 320 - Generalized Abbreviation

## Problem Statement

Given a string `word`, return all possible generalized abbreviations of the word.

A generalized abbreviation can replace one or more consecutive characters with their count.

For example, `"word"` can be abbreviated as `"w2d"` or `"4"`.

## Example 1

### Input

```text
word = "word"
```

### Output

```text
["4","1w1d","1wo1","1wor","w1r1","w1rd","wo2","wor1","word"]
```

## Example 2

### Input

```text
word = "a"
```

### Output

```text
["1","a"]
```

## Approach

Use **Backtracking** to generate all possible abbreviations.

At every character, there are two choices:

1. Abbreviate the character by increasing the abbreviation count.
2. Keep the character and add any pending count before it.

This explores all possible combinations.

## Algorithm

1. Start from the first character.
2. Maintain the current abbreviation and the number of consecutive abbreviated characters.
3. For each character, choose to abbreviate it.
4. Also choose to keep the character.
5. If a count exists, add it before the kept character.
6. Continue recursively until all characters are processed.
7. Add the completed abbreviation to the result.
8. Return all generated abbreviations.

## Time Complexity

`O(2ⁿ × n)`

## Space Complexity

`O(2ⁿ × n)`

## Key Concepts

* Backtracking
* Recursion
* Strings
* Combinations
* Depth-First Search
* Decision Tree

## Language

Python

## LeetCode Details

* **Problem:** 320
* **Title:** Generalized Abbreviation
* **Difficulty:** Medium

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
