import numpy as np

def vectorized_forward_pass(self, input_matrix):
    # your code goes here
    return input_matrix.dot (self.w.T)+self.b>0
