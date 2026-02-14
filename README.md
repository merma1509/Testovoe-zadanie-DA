# Data Analyst Technical Test Assignment

## Overview

This repository contains solutions for a comprehensive technical assessment for a Data Analyst position, covering probability theory, Python algorithms, SQL, statistics, and machine learning basics.

## Structure

```bash
test-assignment/
│
├── README.md                  # This file
├── probability/               # Block 1: Probability & Logic
│   ├── farmer.md              # Farmer problem solution
│   ├── cooking_competition.md # Cooking competition solution
│   └── lonely_road.md         # Lonely road probability solution
│
├── python/                    # Block 2: Python Algorithms
│   ├── isomorphic.py          # String isomorphism check
│   ├── missing_number.py      # Find missing number in sequence
│   ├── prime_factors.py       # Prime factorization
│   └── complexity_analysis.md # Time/space complexity analysis
│
├── sql/                      # Block 3: SQL Problems
│   ├── ranking.sql           # Applicants ranking query
│   ├── full_join_analysis.md   # FULL JOIN row count analysis
│   └── purchases.sql           # Low spending clients query
│
├── statistics/                 # Block 4: Statistics & A/B Testing
│   ├── ab_test_reasoning.md    # A/B test interpretation
│   ├── p_value_definition.md   # p-value explanation
│   └── t_test_applicability.md # t-test for log-normal data
│
└── ml/                         # Block 5: Machine Learning Basics
    ├── model_selection.md      # ROC-AUC model choice reasoning
    ├── roc_auc_manual.md       # Manual ROC-AUC calculation
    └── correlation_analysis.md # Pearson correlation and causation
```

## Python Solutions

```bash
cd python
python isomorphic.py
python missing_number.py
python prime_factors.py
```

## SQL Solutions

Execute SQL files in your preferred database environment (PostgreSQL, MySQL, etc.).

## Requirements

- Python 3.8+
- SQL database (for SQL solutions)
- Basic understanding of probability theory, statistics, and algorithms

## Solutions Summary

### Block 1: Probability & Logic

- **Farmer**: Expected number of different animals in 6 visits
- **Cooking Competition**: Expected winners in two-round tournament
- **Lonely Road**: Car appearance probabilities for different time periods

### Block 2: Python Algorithms

- **Isomorphism**: O(n) time, O(n) space string pattern matching
- **Missing Number**: O(n) time, O(1) space arithmetic solution
- **Prime Factorization**: O(√n) time factorization algorithm

### Block 3: SQL

- **Ranking**: Window functions for student ranking
- **FULL JOIN**: Row count analysis for table joins
- **Purchases**: JOIN + GROUP BY + HAVING for spending analysis

### Block 4: Statistics & A/B Testing

- **A/B Test**: Proper experiment interpretation and scaling
- **p-value**: Statistical significance definition
- **t-test**: Applicability for log-normal distributions

### Block 5: Machine Learning Basics

- **Model Selection**: ROC-AUC interpretation and model inversion
- **ROC-AUC**: Manual calculation from prediction data
- **Correlation**: Pearson correlation and causation analysis
