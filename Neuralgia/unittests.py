import unittest
from nn import struct

class PerceptronTest(unittest.TestCase):

	def test_sum(self):
		perceptron = struct.Perceptron([3, 2], -13)
		self.assertEqual(perceptron.sum([4, 5]), 22)

	def test_output_true(self):
		perceptron = struct.Perceptron([3, 2], -13)
		self.assertEqual(perceptron.output([4, 5]), 1)

	def test_output_false(self):
		perceptron = struct.Perceptron([3, 2], -23)
		self.assertEqual(perceptron.output([4, 5]), 0)

if __name__ == '__main__':
    unittest.main()