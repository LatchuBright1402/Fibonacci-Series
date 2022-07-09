# Function for nth Fibonacci number
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

# output for Fn

print(Fibonacci(0),Fibonacci(1),Fibonacci(2),Fibonacci(3),Fibonacci(4),Fibonacci(5),Fibonacci(6),Fibonacci(7),Fibonacci(8),Fibonacci(9),Fibonacci(10),Fibonacci(11),Fibonacci(12))


