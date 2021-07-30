import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    result = []
    exp_L = np.exp(L)
    sum_exp_L = sum(exp_L)
    for i in exp_L:
        result.append(i*1.0/sum_exp_L)
    return result

print(softmax([2, 1, 0]))
