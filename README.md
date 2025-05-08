
# Week 7 Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib

## 📌 Objective

This project demonstrates how to:

- Load and process a dataset using the `pandas` library.
- Perform grouping and analysis using pandas operations.
- Visualize the results using `matplotlib`.
- Safely execute code with error handling and save plots to file.

## 📂 Dataset Used

The **Iris dataset**, a widely used dataset in machine learning, is used for this analysis. It includes:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

Classes:

- Setosa
- Versicolor
- Virginica

Loaded via:

> from sklearn.datasets import load_iris

**🧪 Task Overview
✅ Load and Explore Data**


> Loaded the dataset using pandas.

> Converted target values to species names using pd.Categorical.

> Grouped data by species to compute mean values.

**✅ Visualizations Created**

> Line Chart – Average Petal Length per Species

> Bar Chart – Average Sepal Width per Species

> Histogram – Distribution of Sepal Length

> Scatter Plot – Sepal Length vs Petal Length per Species

**💻 How to Run the Code**


Make sure the required packages are installed:

> pip install pandas matplotlib searbon scikit-learn

Then run the script depending on your OS(Operating System):

**🏃‍♂️ How to Run the Script**


You can run the script in several ways depending on your operating system or code editor setup:

**💻 Windows**


Open a terminal (CMD or PowerShell), navigate to the script folder, then run:

> python assignment-7.py

Or, if using Visual Studio Code, press:

> Ctrl + Alt + N

(Requires the Code Runner extension)

**🐧 Linux**

Open a terminal and run:

> python3 assignment-7.py

In VS Code with Code Runner installed, press:

> Ctrl + Alt + N

**🍎 macOS**

Open Terminal and run:

> python3 assignment-7.py

In VS Code, you can also press:

> Ctrl + Option + N

✅ Note: Make sure you have Python and required libraries (pandas, matplotlib, scikit-learn) installed.

If successful, it will print:

> Plots saved successfully to iris_plots.pdf and iris_plots.png

🖼️ **Output**


The script saves the visualizations as:

> iris_plots.pdf
> iris_plots.png

They are created using matplotlib.use('Agg') so it works in non-GUI environments.

**✅ Error Handling**


The script uses a try-except block to handle any exceptions during data processing or saving.

**📎 Requirements**

> Python 3.x
> pandas
> matplotlib
> scikit-learn

**🧑‍💻 Author**

>
> Prepared by: Silas HAKUZWIMANA
> PLP - February 2025 Cohort
> Module: Python
