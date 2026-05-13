from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ExpectationMaximization
import pandas as pd
import numpy as np

# Create a sample structure
model = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Generate sample data with missing values (NaN)
data = pd.DataFrame(np.random.randint(low=0, high=2, size=(1000, 3)), columns=['A', 'B', 'C'])
data.loc[:100, 'C'] = np.nan  # Introduce missing data

# Use EM to estimate CPDs
estimator = ExpectationMaximization(model, data)
cpds = estimator.get_parameters(latent_card={'C': 2})

print("Learned CPD for node C using EM:")
print(cpds[2]) # Display the learned conditional probability table