import Regression.linnearRegression
import numpy as np 

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]


model = Regression.linnearRegression.linnearRegression(x, y)

print(model.getPredicted())

