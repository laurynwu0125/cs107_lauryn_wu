import numpy as np

def layer(shape, actv):
    numInputs = shape[0]
    numUnits = shape[1]

    def inner(inputs, weights, bias):
        output = np.add(inputs.dot(weights), bias)
        return actv(output)

    return inner


t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network
shape1 = [100, 4]
shape2 = [4, 2]

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
# weights have size shape, 100 x 4 and 4 x 2
w1 = np.random.uniform(0.0, 1.0, shape1[0] * shape1[1]).reshape(shape1[0],-1)
w2 = np.random.uniform(0.0, 1.0, shape2[0] * shape2[1]).reshape(shape2[0],-1)

# biases are vectors with size 400 and 8, respectively
b1 = np.ones((shape1[1]))
b2 = np.ones((shape2[1]))

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer

print(h1)
print(h2)
