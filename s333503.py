import numpy as np

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0]) 

def f2(x: np.ndarray) -> np.ndarray:
    return 100 * (79.31034482758619 * ((x[1] / 0.00924390680275859) + ( (x[0] *130.79667063020165 ) - (x[0] * ((x[0] + x[2]) * (x[1] * 10.34482758620689) )) )))

def f3(x: np.ndarray) -> np.ndarray:
    return (np.abs(((np.abs(np.abs(((x[1] * (x[2] / x[1])) - (10.34482758620689)) * x[0])) + -0.8813793103448284) + -3.448275862068968) - 0.0803297862620687)) - (x[1] * (x[1] * x[1]))

def f4(x: np.ndarray) -> np.ndarray:
    return (np.cos((((np.sqrt(np.abs(np.log(np.abs(x[1]))))) * (x[1])) * (-44.827586206896555)) / (44.82758620689654))) * (np.log((((-51.724137931034484) / (np.abs(np.abs(x[1])))) / (np.abs(x[1] + 0.10120082833221793))) / (-0.05309087837389616)))

def f5(x: np.ndarray) -> np.ndarray:
    return ((((np.sqrt(np.abs(x[1]))) + (np.sin(np.sqrt(np.abs(x[1] * x[0]))))) - (x[1])) / (35522.38793103447)) / (35522.38793103447)

def f6(x: np.ndarray) -> np.ndarray:
    return ((x[1] * 0.7803448275862044 ) - (x[0])) + (x[1])

def f7(x: np.ndarray) -> np.ndarray:
    return np.abs((17.241379310344826) * (np.log(np.abs(x[0] - x[1]))))

def f8(x: np.ndarray) -> np.ndarray:
    return (x[5]) * (np.abs((x[5]) * ((np.abs(x[5] * 24.137931034482747)) * (x[5]))))