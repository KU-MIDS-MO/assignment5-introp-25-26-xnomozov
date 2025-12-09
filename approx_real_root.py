import numpy as np

"""
 
 A function approx_real_root(coeffs, interval) that:
 receives a list coeffs of four numbers representing a cubic polynomial,starting with the coefficient 
 of the free term and finishing with the coefficient of x^3
 receives a tuple interval = (a, b) with a < b,
 assumes that the polynomial has exactly one real root inside this interval,
 computes and returns a floating-point approximation of that root,
 and ensures that the approximation is accurate to at least 1×10⁻⁹ in absolute error
 
 """


def approx_real_root(coeffs, interval):
    
    def poly_value(x):
        reversed_coeffs = coeffs[::-1]
        p = np.poly1d(reversed_coeffs)
        return p(x)
   
   
    a, b = interval
    tolerance = 1e-9
   
 
    if poly_value(a) == 0:
        return a
    if poly_value(b) == 0:
        return b
   
   
    while (b - a) > 2 * tolerance:
       
        mid = (a + b) / 2
       
      
        val_mid = poly_value(mid)
       
       
        if val_mid == 0:
            return mid
       
      
        if poly_value(a) * val_mid < 0:
           
            b = mid
        else:
          
            a = mid
   
   
    return (a + b) / 2



coeffs1 = [-5, -2, 0, 1]
root1 = approx_real_root(coeffs1, (2, 3))
print("Root:", root1)