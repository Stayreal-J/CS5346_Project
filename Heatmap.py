import numpy as np
import matplotlib.pyplot as plt

correlation_matrix = np.array([
    [1.0,0.9206727661715740,0.9559567421835880,0.7884923844034820,0.9037352052746700],
    [0.9206727661715740,1.0,0.98702006160792,0.8412994941581370,0.9913398605274550], 
    [0.9559567421835880,0.98702006160792,1.0,0.8381354011327720,0.9828413324803960], 
    [0.7884923844034820,0.8412994941581370,0.8381354011327720,1.0,0.8435188320482120], 
    [0.9037352052746700,0.9913398605274550,0.9828413324803960,0.8435188320482120,1.0] 
        
])

labels = ["House price", "CPI", "GDP", "Govern_expense", "Population"]

plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='Blues', interpolation='nearest')

plt.colorbar()
plt.xticks(np.arange(len(labels)), labels, rotation=45)
plt.yticks(np.arange(len(labels)), labels)
plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)


plt.title('Correlation Heatmap')
plt.show()
