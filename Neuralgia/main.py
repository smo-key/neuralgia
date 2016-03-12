from nn import struct

perceptron = struct.Perceptron([1, 2], 16);
print perceptron.sum([4, 4]);
print perceptron.output([4, 4]);

neuron = struct.Neuron([1, 2], 16);
print neuron.sum([4, 4]);
print neuron.output([4, 4]);