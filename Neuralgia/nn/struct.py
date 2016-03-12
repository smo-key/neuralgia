import math;

class Perceptron:
	weights = []	# weights
	bias = 0		# bias value == -threshold

	def __init__(self, weights, bias):
		self.weights = weights;
		self.bias = bias;

	def sum(self, inputs):
		# compute weighted sum
		if (len(inputs) != len(self.weights)):
			raise IndexError()
		return reduce(lambda x,y:x+y, map(lambda x,y:x*y, self.weights, inputs));

	def output(self, inputs):
		sum = self.sum(inputs)
		if sum + self.bias > 0: return 1
		else: return 0

class Neuron:
	sigmoid = lambda z:1 / (1 + math.exp(-z)) # sigmoid function
	step = lambda x:1 if x > 0 else 0		  # step function
	
	activationFunc = sigmoid				  # activation function (interchangable)
	weights = []	# weights
	bias = 0		# bias value == -threshold

	def __init__(self, weights, bias, activationFunc=sigmoid):
		self.weights = weights;
		self.bias = bias;
		self.activationFunc = activationFunc;
		
	def sum(self, inputs):
		# compute weighted sum
		if (len(inputs) != len(self.weights)):
			raise IndexError()
		return reduce(lambda x,y:x+y, map(lambda x,y:x*y, self.weights, inputs));

	def output(self, inputs):
		sum = self.sum(inputs)
		return self.activationFunc(sum);