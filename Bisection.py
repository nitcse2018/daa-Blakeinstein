'''
Implementation of Bisection Method for finding root of a given equation by using divide
and conquer. Based on binary search.

The bisection method works by switching to the bounded region that contains the root,
if value at left bound times the value at right bound is negative , then that
indicates a positive value was multiplied by a negative value and the function
crossed zero in between.

The bounds are switched to more accurately hone in on the zero as specified by the error
margin by considering the middle of the existing bounds.
'''

def bisection(a, b):
    # A recursive method called upon region a and b.
    if func(a) * func(b) >= 0:
        #check if a zero even exists in the given region
        return None
    elif b - a >= 0.01:
        # check if current error is above requirement, goes to next accurate region
        c = (b+a)/2 # The median is selected.
        if func(c)==0:
            return c # return median, if it is the root, EDGE CASE
        if func(c)*func(a) < 0:
            return bisection(a, c) # Switch to left section if that contains root
        else:
            return bisection(c, b) # Switch to right section
    else:
        return a # return left bound as answer, as left bound is more likely to be the root
    
#Test code, function not considered as function parameter, as import wasnt necessary.
if __name__ == "__main__":
    # Define function as a string
    y = "x**3 - x**2 + 2" # y = x³ - x² + 2
    # Define a function func to evaluate the string return value at point x, uses eval(Unsafe)
    func = lambda x: eval(y)
    #define left and right bounds
    a = -200
    b = 300
    #print answer
    print (bisection(a, b)) # Approx -1.0025