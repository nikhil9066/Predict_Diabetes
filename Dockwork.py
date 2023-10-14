import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from Seaborn
iris = sns.load_dataset("iris")

# Encode the 'species' column to numeric values
species_mapping = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
iris['species_id'] = iris['species'].map(species_mapping)

# Set a custom color palette for the species
palette = ['b', 'g', 'r']

# Create a pairplot to visualize relationships between features
sns.pairplot(iris, hue="species_id", palette=palette)
plt.title("Pairplot of Iris Dataset")
plt.show()

# Create a violin plot to visualize the distribution of sepal lengths by species
sns.violinplot(x="species", y="sepal_length", data=iris, palette=palette)
plt.title("Distribution of Sepal Length by Species")
plt.show()

# Create a correlation heatmap
correlation_matrix = iris.drop('species', axis=1).corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()