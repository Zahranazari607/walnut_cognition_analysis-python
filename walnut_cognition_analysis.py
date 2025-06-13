# Simple Data Analysis Example for Neuroscience Application

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate some cognitive score data related to walnut intake
np.random.seed(42)

groups = ['Control', 'Low Walnut', 'High Walnut']
data = {
    'Group': np.repeat(groups, 30),
    'Cognitive_Score': np.concatenate([
        np.random.normal(75, 5, 30),  # Control group
        np.random.normal(80, 5, 30),  # Low walnut group
        np.random.normal(85, 5, 30)   # High walnut group
    ])
}

# Create dataframe
df = pd.DataFrame(data)

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.groupby('Group')['Cognitive_Score'].describe())

# Visualization
plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='Cognitive_Score', data=df, palette='Set2')
plt.title('Cognitive Scores Across Groups')
plt.ylabel('Cognitive Score')
plt.xlabel('Group')
plt.grid(True)
plt.show()

# Save the figure
plt.savefig("cognitive_scores.png")

# Export the data to CSV
df.to_csv("cognitive_scores.csv", index=False)

