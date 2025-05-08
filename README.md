---
# 📊 Week 7 Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib

## 📌 Objective

This project demonstrates how to:

* Load and process a dataset using the `pandas` library.
* Perform grouping and statistical analysis.
* Visualize the results using `matplotlib` and `seaborn`.
* Handle errors gracefully and save plots to files.
---
## 📂 Dataset Used

The **Iris dataset**, a classic dataset used in machine learning, includes:

* Features:

  * Sepal length (cm)
  * Sepal width (cm)
  * Petal length (cm)
  * Petal width (cm)
* Classes:

  * Setosa
  * Versicolor
  * Virginica

**Loaded via:**

```python
from sklearn.datasets import load_iris
```

---

## 🧪 Task Overview

### ✅ Load and Explore Data

* Loaded the dataset using pandas.
* Converted numeric targets to species names using `pd.Categorical`.
* Grouped data by species and computed mean values.

### ✅ Visualizations Created

* 📈 Line Chart – Average Petal Length per Species
* 📊 Bar Chart – Average Sepal Width per Species
* 📉 Histogram – Distribution of Sepal Length
* 🔵 Scatter Plot – Sepal Length vs Petal Length by Species

---

## 💻 How to Run the Code

### 🔧 Install Required Libraries

```bash
pip install pandas matplotlib seaborn scikit-learn
```

### 🏃‍♂️ Run the Script

Depending on your operating system:

#### 💻 Windows

Open CMD or PowerShell in the script folder:

```bash
python assignment-7.py
```

Or in **Visual Studio Code**, press:

```
Ctrl + Alt + N
```

(Requires the *Code Runner* extension)

#### 🐧 Linux

In terminal:

```bash
python3 assignment-7.py
```

Or in VS Code:

```
Ctrl + Alt + N
```

#### 🍎 macOS

In terminal:

```bash
python3 assignment-7.py
```

Or in VS Code:

```
Ctrl + Option + N
```

---

## 🖼️ Output

The script saves the visualizations as:

```
Plots saved successfully at 2025-05-08_15-36-13.

Visualizations saved successfully:
- PDF: iris_analysis_report_2025-05-08_15-36-13.pdf
- PNG: iris_analysis_report_2025-05-08_15-36-13.png
```

> ✅ Note: The script uses `matplotlib.use('Agg')` so it works in headless (non-GUI) environments.

---

## ⚠️ Error Handling

Robust `try-except` blocks handle:

* File permission errors
* Plotting issues
* Data processing errors

Any issues are printed to the terminal with meaningful messages.

---

## 📎 Requirements

* Python 3.x
* `pandas`
* `matplotlib`
* `seaborn`
* `scikit-learn`

---

## 🧑‍💻 Author

**Prepared by:**
**Silas HAKUZWIMANA**
*PLP – February 2025 Cohort*
*Module: Python*

---
