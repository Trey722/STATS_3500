import numpy as np 

def get_m(x, y):
        n = min(len(x), len(y)) 
    
        top = n * sum(x * y) - sum(x) * sum(y)
        bottom = n * sum(x * x) - sum(x) * sum(x) 
        
        return top / bottom
    
    
def get_intercept(x_bar, y_bar, m):
    return y_bar - (m * x_bar)
    
        



class linnearRegression: 
    def __init__(self, independentVar, dependentVar) -> None:
        self.x = np.array(independentVar)
        self.y = np.array(dependentVar)
        x = self.x
        y = self.y
        
        
        if len(x) != len(y):
            self.real = False
        else:
            self.x_bar = np.mean(x)
            self.y_bar = np.mean(y)
            self.b1 = get_m(x, y)
            self.b0 = get_intercept(self.x_bar, self.y_bar, self.b1) 
            
            
            self.y_predicted = None
            self.Fstat = None
            
            
        
            
            
    def getValue(self, x):
        return x * self.b1 + self.b0 
    
    def getPredicted(self):
        if self.y_predicted is None:
            self.y_predicted = np.array([self.getValue(xi) for xi in self.x])
            
        return self.y_predicted
    
    
            
            
    
    

    
            
        
   