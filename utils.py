import math
import scipy.integrate as integ
def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	# a = 1
	# while (a < n):
	# 	b = a * (a + 1)
	# 	a += 1
	# return b
	res = 1
	while (n >= 1):
		res *= n
		n -= 1
	return res

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = b * b - 4 * a * c
	if delta < 0:
		return None
	elif delta == 0:
		return -b / 2 * a
	elif delta > 0:
		return ((-b - math.sqrt(delta))/2*a, (-b + math.sqrt(delta))/2*a)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	
	result = integ.quad(lambda x: eval(function), lower, upper)
	return result

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
