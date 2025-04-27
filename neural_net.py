import os 
os.getcwd()
import numpy as np

print('welcome \n to \n my \n neural net')

nn_architecture = [
    {"input_dim": 1, "output_dim": 5, "activation": "relu"},
    {"input_dim": 2, "output_dim": 3, "activation": "relu"},
    {"input_dim": 3, "output_dim": 7, "activation": "relu"},
    {"input_dim": 5, "output_dim": 1, "activation": "relu"},
    {"input_dim": 7, "output_dim": 2, "activation": "sigmoid"},
]


def init_layers(nn_architecture, seed = 99):
    np.random.seed(seed)
    number_of_layers = len(nn_architecture)
    params_values = {}

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        layer_input_size = layer["input_dim"]
        layer_output_size = layer["output_dim"]
        
        params_values['W' + str(layer_idx)] = np.random.randn(
            layer_output_size, layer_input_size) * 0.1
        params_values['b' + str(layer_idx)] = np.random.randn(
            layer_output_size, 1) * 0.1
        
    return params_values