import numpy as np
import  pandas as pd

def __generate_x_y_from_nsc_df(__data_frame, time_step=4):
    data_array = __data_frame.to_numpy()
    X = []
    y = []

    for i in range(len(data_array) - time_step):
        row = data_array[i:i + time_step]
        label = data_array[i + time_step]
        X.append(row)
        y.append(label)
    return np.array(X), np.array(y)
