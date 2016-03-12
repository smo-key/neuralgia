class Perceptron:
	weights = [] # weights
	bias = 0 # bias value == -threshold

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