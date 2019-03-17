import numpy as np
import matplotlib.pyplot as mp
data = np.genfromtxt("HDFCBANK-I_ycc.csv" ,delimiter = ',' , autostrip = True)
o = [20,50,75,100,150,200,300,400]
rsi = [53.2, 58.7, 60.4, 62.7, 63.4,62.8,62.7, 62.8]
mp.plot(o, rsi, label='C')
mp.title("Accuracy at minimum sample split = 6")
mp.xlabel("Number of estimators")
mp.ylabel("Accuracy(%)")
#mp.text(1, 60, 'Penalty Constant')
mp.show()