# Generate Fibonacci series using lambda function (not recommended)
fibonacci = lambda n: [] if n <= 0 else [0] if n == 1 else [0, 1] if n == 2 else (lambda s: s.extend([s[-1] + s[-2]]) or s)(fibonacci(n-1)[:])

# Generate Fibonacci series using the lambda function
fib_series = fibonacci(50)

# Print the Fibonacci series
print("Fibonacci series with 50 elements:", fib_series)

