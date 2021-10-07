import numpy as np

class Layer:
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weights = np.random.uniform(0.0, 1.0, shape[0] * shape[1]).reshape(shape[0],-1)
        self.bias = np.random.rand((shape[1]))

    def __str__(self):
        return "The weights are \n" + np.array2string(self.weights) + " \n and the biases are \n" + np.array2string(self.bias)

    def __repr__(self):
        return "The weights are \n" + np.array2string(self.weights)

    def __sizeof__(self):
        return str(self.shape)

    def forward(self, inputs):
        output = np.add(inputs.dot(self.weights), self.bias)
        return self.actv(output)


inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network
shape1 = [100, 4]
shape2 = [4, 2]
actv = np.tanh

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)

print(h1)
print(h2)
print(layer1)
print(repr(layer1))
print(layer1.__sizeof__())
