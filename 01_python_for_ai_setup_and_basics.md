# Practical 1: PYTHON FOR AI — SETUP AND BASICS

Objective: To set up the Python AI development environment and practice the core data structures and libraries used throughout the course.
Scenario: Before any AI algorithm can be built, you need a working environment and comfort with Python's basic data structures (used to represent graphs, states, and datasets in later practicals) and the NumPy/Pandas libraries (used to represent numerical and tabular data).

## Question 1: Python & Development Environment Setup

Procedure:
1. Download Python 3.x from python.org and install it (ensure 'Add Python to PATH' is checked).
2. Verify installation by terminal command: python --version
3. Install Jupyter Notebook via pip: pip install notebook
4. Launch environment: jupyter notebook
5. Alternatively, install VS Code with the official Python and Jupyter extensions.

### Question 1 - Environment Verification Script

```python
# Verification script for environment & Python runtime
import sys
import platform

print("Python Version:", platform.python_version())
print("Compiler / Build:", platform.python_compiler())
print("Execution Path:", sys.executable)
```

### Sample output from the source report

```text
Python Version: 3.10.12
Compiler / Build: GCC 11.4.0
Execution Path: /usr/bin/python3
[STATUS] Python and Jupyter runtime environment successfully initialized.
```

## Question 2: AI Core Libraries Installation and Verification

### Question 2 - Library Import & Version Check

```python
# Terminal command executed:
# pip install numpy pandas scikit-learn matplotlib

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

print("NumPy Version:", np.__version__)
print("Pandas Version:", pd.__version__)
print("scikit-learn Version:", sklearn.__version__)
print("All foundational AI libraries imported successfully!")
```

### Sample output from the source report

```text
NumPy Version: 1.24.3
Pandas Version: 2.0.3
scikit-learn Version: 1.3.0
All foundational AI libraries imported successfully!
```

## Question 3: List, Dictionary, and Set Operations (Product Inventory)

### Question 3 - Python Data Structures Code

```python
# List: product names in stock
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
products.append("Webcam")   # add an item
products.remove("Mouse")    # remove an item
print("Products:", products)

# Dict: product -> price mapping
prices = {"Laptop": 55000, "Keyboard": 1200, "Monitor": 9500}
prices["Webcam"] = 2200    # add new key-value pair
print("Laptop price:", prices["Laptop"])
print("All prices:", prices)

# Set: unique categories sold this week
categories_mon = {"Electronics", "Accessories", "Electronics"}
categories_tue = {"Accessories", "Furniture"}
print("Unique categories (union):", categories_mon | categories_tue)
print("Common categories (intersection):", categories_mon & categories_tue)
```

### Sample output from the source report

```text
Products: ['Laptop', 'Keyboard', 'Monitor', 'Webcam']
Laptop price: 55000
All prices: {'Laptop': 55000, 'Keyboard': 1200, 'Monitor': 9500, 'Webcam': 2200}
Unique categories (union): {'Electronics', 'Furniture', 'Accessories'}
Common categories (intersection): {'Accessories'}
```

## Question 4: NumPy Array Operations (Sales Units Analysis)

### Question 4 - NumPy Vectorized Calculations

```python
import numpy as np

# Weekly units sold for a product across 7 days
sales_units = np.array([12, 18, 9, 25, 30, 22, 15])
print("Array:", sales_units)
print("Shape:", sales_units.shape)
print("Total units:", sales_units.sum())
print("Average per day:", sales_units.mean())
print("Max day:", sales_units.max())

# Element-wise operation: apply a 10% growth projection
projected = sales_units * 1.10	
print("Projected next week:", projected)

# 2D array: units sold for 2 products across 7 days
matrix = np.array([
    [12, 18, 9, 25, 30, 22, 15],
    [8, 14, 11, 19, 21, 17, 13]
])
print("2D shape:", matrix.shape)
print("Row sums (total per product):", matrix.sum(axis=1))
```

### Sample output from the source report

```text
Array: [12 18  9 25 30 22 15]
Shape: (7,)
Total units: 131
Average per day: 18.714285714285715
Max day: 30
Projected next week: [13.2 19.8  9.9 27.5 33.  24.2 16.5]
2D shape: (2, 7)
Row sums (total per product): [131 103]
```

## Question 5: Pandas Series and DataFrame Basics (Sales Table)

### Question 5 - Pandas Data Processing

```python
import pandas as pd

# Series example
prices = pd.Series([55000, 600, 1200, 9500],
                   index=["Laptop", "Mouse", "Keyboard", "Monitor"])
print("Series:\n", prices)

# DataFrame example
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    "UnitsSold": [12, 45, 30, 18],
    "UnitPrice": [55000, 600, 1200, 9500]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Basic operations: Revenue calculation and aggregation
df["Revenue"] = df["UnitsSold"] * df["UnitPrice"]
print("\nWith Revenue column:\n", df)
print("\nGrouped by Category:\n", df.groupby("Category")["Revenue"].sum())
```

### Sample output from the source report

```text
Series:
Laptop       55000
Mouse          600
Keyboard      1200
Monitor       9500
dtype: int64

DataFrame:
    Product     Category  UnitsSold  UnitPrice
0    Laptop  Electronics         12      55000
1     Mouse  Accessories         45        600
2  Keyboard  Accessories         30       1200
3   Monitor  Electronics         18       9500

With Revenue column:
    Product     Category  UnitsSold  UnitPrice  Revenue
0    Laptop  Electronics         12      55000   660000
1     Mouse  Accessories         45        600    27000
2  Keyboard  Accessories         30       1200    36000
3   Monitor  Electronics         18       9500   171000

Grouped by Category:
Category
Accessories     63000
Electronics    831000
Name: Revenue, dtype: int64
```
