def poly_integral(poly, C=0):
    """
    Calculates the indefinite integral of a polynomial.
    Input:
        poly: list of coefficients, index = power of x
        C: integration constant
    Returns:
        list of coefficients representing the integral
    """
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not isinstance(C, (int, float)):
        return None

    integral = [C]  # Start with integration constant
    for power, coef in enumerate(poly):
        new_coef = coef / (power + 1)
        # Represent as int if whole number
        if new_coef == int(new_coef):
            new_coef = int(new_coef)
        integral.append(new_coef)
    
    # Remove trailing zeros for minimal list
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    
    return integral

# Example usage
if __name__ == "__main__":
    poly = [5, 3, 0, 1]  # Represents 5 + 3x + 0x^2 + x^3
    print(poly_integral(poly))  # Output: [0, 5, 1.5, 0, 0.25]
