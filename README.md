# Binary Trees Overview

This document provides an overview of different types of binary trees, including their definitions, properties, and common use cases.

## 1. Full Binary Tree

- **Definition:** 
  - A binary tree is full if every node has either 0 or 2 children. No node in a full binary tree has only one child.
  
- **Properties:**
  - **Node Count:** If the tree has `n` leaves, the total number of nodes in the tree is `2n - 1`.
  - **Internal Nodes:** The number of internal nodes in a full binary tree with `n` leaves is `n - 1`.
  - **Height:** The height `h` of a full binary tree can be calculated using `h = log2(n)`, where `n` is the number of leaves.
  - **Symmetry:** Full binary trees are often symmetric, making them suitable for algorithms requiring strict binary structures.

- **Example Use Case:**
  - **Heap Implementations:** Used in heap structures where a strict binary format is required.
  - **Decision Trees:** Applied in decision tree algorithms where each decision node has exactly two possible outcomes.

## 2. Complete Binary Tree

- **Definition:** 
  - A binary tree is complete if all levels are completely filled except possibly the last, which is filled from left to right.
  
- **Properties:**
  - **Height:** The height of a complete binary tree with `n` nodes is `O(log n)`.
  - **Node Distribution:** All levels above the last are fully filled, and the last level has all nodes as left-aligned as possible.
  - **Balance:** Complete binary trees are compact, minimizing the height and improving efficiency for certain operations.

- **Example Use Case:**
  - **Heap Data Structures:** Commonly used in binary heaps and priority queues.
  - **Binary Search Trees:** Utilized in certain balanced search trees like B-trees for efficient dynamic set management.

## 3. Perfect Binary Tree

- **Definition:** 
  - A perfect binary tree is one where all internal nodes have exactly two children, and all leaf nodes are at the same level.
  
- **Properties:**
  - **Node Count:** A perfect binary tree of height `h` has `2^(h+1) - 1` nodes.
  - **Leaf Nodes:** The number of leaf nodes in a perfect binary tree is `2^h`, where `h` is the height.
  - **Uniform Depth:** All leaf nodes are at the same level, ensuring uniform depth.
  - **Symmetry:** The tree is perfectly symmetric, making it ideal for certain algorithms.

- **Example Use Case:**
  - **Parallel Algorithms:** Used in parallel processing to evenly distribute tasks.
  - **Binary Search Trees:** Ensures optimal performance in balanced search trees, with operations taking `O(log n)` time.
