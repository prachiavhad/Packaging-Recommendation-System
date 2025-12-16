import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the file path is correct
file_path = 'prepared_materials_data.csv'
df = pd.read_csv(file_path)

# Set a style for better visualization
sns.set_style("whitegrid")


# --- Plot 1: Histogram of Material Suitability Score (Target Variable) ---
plt.figure(figsize=(10, 6))
sns.histplot(df['Material_Suitability_Score'], bins=15, kde=True, color='skyblue')
plt.title('1. Distribution of Material Suitability Score', fontsize=16)
plt.xlabel('Material Suitability Score', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tight_layout()
plt.savefig('python_suitability_score_histogram.png')
plt.show() # Display the graph

# --- Plot 2: Bar Chart of Material Type Counts ---
material_counts = df['material_type'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(12, 7))
# Note: Using hue explicitly to silence the FutureWarning
sns.barplot(x=material_counts.index, y=material_counts.values, palette='viridis', hue=material_counts.index, legend=False)
plt.title('2. Distribution of Material Types in Dataset', fontsize=16)
plt.xlabel('Material Type', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('python_material_type_distribution.png')
plt.show() # Display the graph


# --- Plot 3: Box Plot of Suitability Score by Material Type ---
plt.figure(figsize=(14, 8))
sns.boxplot(x='material_type', y='Material_Suitability_Score', data=df, palette='pastel')
plt.title('3. Material Suitability Score Distribution by Material Type', fontsize=16)
plt.xlabel('Material Type', fontsize=14)
plt.ylabel('Material Suitability Score', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('python_suitability_score_boxplot.png')
plt.show() # Display the graph


# --- Plot 4: Scatter Plot of Cost Efficiency vs. CO2 Impact ---
# Useful for visualizing the trade-off between two key engineered features
plt.figure(figsize=(10, 8))
sns.scatterplot(
    x='CO2_Impact_Index',
    y='Cost_Efficiency_Index',
    data=df,
    hue='material_type', # Color-code points by type
    size='Material_Suitability_Score', # Use size to indicate overall score
    palette='deep',
    sizes=(20, 200) # Define size range for points
)
plt.title('4. Trade-off: CO2 Impact Index vs. Cost Efficiency Index', fontsize=16)
plt.xlabel('CO2 Impact Index (Lower is Better)', fontsize=14)
plt.ylabel('Cost Efficiency Index (Higher is Better)', fontsize=14)
plt.legend(title='Material Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('python_cost_vs_co2_scatterplot.png')
plt.show() # Display the graph

print("All four visualizations generated and displayed successfully!")
