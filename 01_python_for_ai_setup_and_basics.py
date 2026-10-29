"""Practical 1: PYTHON FOR AI — SETUP AND BASICS.

Extracted from BSBXLB302P_AI_Lab_Practical_Report.docx.
"""

# Verification script for environment & Python runtime
import sys
import platform

print("Python Version:", platform.python_version())
print("Compiler / Build:", platform.python_compiler())
print("Execution Path:", sys.executable)

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
