import pandas as pd
from scipy.stats import pearsonr
import os

df = pd.read_csv('output.csv')
correlation = "./correlation_matrix.csv"
data = df.iloc[:, 1:]
correlation_matrix = data.corr(method='pearson')
p_values = data.apply(lambda x: data.apply(lambda y: pearsonr(x, y)[1]))
correlation_matrix = data.corr()
print("The correlation matrix is", correlation_matrix)
print("P-Values Matrix:", p_values)

data_path = "output.csv"
directory = os.path.dirname(data_path)

correlation_matrix_path = os.path.join(directory, "correlation_matrix.csv")
p_values_path = os.path.join(directory, "p_values.csv")
correlation_matrix.to_csv(correlation_matrix_path)
p_values.to_csv(p_values_path)


