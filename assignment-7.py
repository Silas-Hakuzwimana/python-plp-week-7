from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use('Agg')  # Use non-GUI backend for saving files

# Set seaborn style
sns.set_theme(style="whitegrid", palette="pastel")

try:
    #load and prepare the iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    grouped = df.groupby('species', observed=False).mean().reset_index()
    
    # Set up the matplotlib figure
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Line Chart
    sns.lineplot(data=grouped, x='species', y='petal length (cm)', marker='o', ax=axs[0, 0])
    axs[0, 0].set_title('Line - Average Petal Length per Species')
    axs[0, 0].set_xlabel('Species')
    axs[0, 0].set_ylabel('Petal Length (cm)')

    # Bar Chart
    sns.barplot(data=grouped, x='species', y='sepal width (cm)', hue='species', palette='Oranges', ax=axs[0, 1], legend=False)
    axs[0, 1].set_title('Bar Chart - Average Sepal Width per Species')
    axs[0, 1].set_xlabel('Species')
    axs[0, 1].set_ylabel('Sepal Width (cm)')

    # Histogram
    sns.histplot(df['sepal length (cm)'], bins=20, color='green', kde=True, ax=axs[1, 0])
    axs[1, 0].set_title('Histogram - Distribution of Sepal Length')
    axs[1, 0].set_xlabel('Sepal Length (cm)')

    # Scatter Plot
    sns.scatterplot(
        data=df,
        x='sepal length (cm)',
        y='petal length (cm)',
        hue='species',
        palette=['red', 'blue', 'purple'],
        ax=axs[1, 1]
    )
    axs[1, 1].set_title('Scatter Plot - Sepal Length vs Petal Length')
    axs[1, 1].set_xlabel('Sepal Length (cm)')
    axs[1, 1].set_ylabel('Petal Length (cm)')

    plt.tight_layout()

    # Define file paths
    pdf_path = "iris_plots.pdf"
    png_path = "iris_plots.png"

    # Try saving the plots
    try:
        plt.savefig(pdf_path, format='pdf')
        plt.savefig(png_path, format='png')
        plt.close(fig)
        print(f"\nPlots saved successfully to {pdf_path} and {png_path}")
    except Exception as e:
        print(f"Failed to save plots: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
