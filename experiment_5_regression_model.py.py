import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 

waist = np.array([70, 71, 72, 73, 74, 75, 76, 77, 78, 79]) 
weight = np.array([55, 57, 59, 61, 63, 65, 67, 69, 71, 73]) 
data = pd.DataFrame({'waist': waist, 'weight': weight}) 

X = data[['waist']] 
y = data['weight'] 

model = LinearRegression().fit(X, y) 

new_waist = 80
predicted_weight = model.predict(pd.DataFrame({'waist': [new_waist]})) 
print(f"Predicted weight for waist {new_waist}: {predicted_weight[0]:.2f}") 

plt.scatter(X, y, color='green', label='Actual Data') 
plt.scatter(new_waist, predicted_weight, marker='*', color='red', s=200, label='Prediction') 
plt.plot(X, model.predict(X), color='orange', label='Regression Line') 
plt.xlabel('Waist (cm)'); plt.ylabel('Weight (kg)')
plt.title('Linear Regression Model'); plt.legend()
plt.show()