def sqrt(n, tolerance=1e-10):
    # If n is 0 or a very small number, return 0
    if n == 0:
        return 0
    
    # Start with an initial guess. We can start with n/2 as an initial guess.
    guess = n / 2.0
    
    while True:
        # Calculate the next approximation
        next_guess = 0.5 * (guess + n / guess)
        
        # Check if the approximation is good enough (within the tolerance)
        if abs(next_guess - guess) < tolerance:
            return next_guess
        
        # Update guess for the next iteration
        guess = next_guess

# Test the function
number = float(input("Enter a positive number: "))
result = sqrt(number)
print(f"The square root of {number} is approximately {result}")