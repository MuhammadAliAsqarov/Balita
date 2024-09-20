def fibonacci_recursive(n):
    # Base cases: Fib(0) = 0, Fib(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: Fib(n) = Fib(n-1) + Fib(n-2)
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage:
num = 7
print(f"Fibonacci number at position {num} is {fibonacci_recursive(num)}")