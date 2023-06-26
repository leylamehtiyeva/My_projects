import numpy as np

""""
A simple neural network solving binary classification problem: have the girl sympathy or not (0/1)
"""


def act(x):
    """
    Activation function
    :param x: number
    :return: 0/1 depending on x value
    """
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    """
    Passes the input signal through the neural network
    :param house: value of parameter 'have an own house' (0/1)
    :param rock: value of parameter 'like rock music' (0/1)
    :param attr: value of parameter 'attractiveness' (0/1)
    :return:
    """
    x = np.array([house, rock, attr])  # input signal vector (0/1)
    w11 = [0.3, 0.3, 0]  # weights for the first hidden layer (accordingly for house, rock, attr)
    w12 = [0.4, -0.5, 1]  # weights for the second hidden layer (accordingly for house, rock, attr)
    weight1 = np.array([w11, w12])  # weight's matrix 2x3
    weight2 = np.array([-1, 1])  # connection vector for the output neuron

    sum_hidden = np.dot(weight1, x)
    print(f'Sum values on hidden layer neurons {sum_hidden}')

    out_hidden = np.array([act(x) for x in sum_hidden])
    print(f'Values at the outputs of neurons in the hidden layer {out_hidden}')

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print(f'Neural network output value {y}')

    return y


house, rock, attr = 1, 0, 1

res = go(house, rock, attr)
print('Like') if res == 1 else print('Dislike')




