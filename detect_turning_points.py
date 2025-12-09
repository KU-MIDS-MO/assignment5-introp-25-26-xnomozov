import numpy as np
import matplotlib.pyplot as plt


"""
 
 A function detect_turning_points(signal, filename="turning_points.pdf") that:
 receives a 1D NumPy array representing a signal
 identifies all indices where the direction of the signal changes
 (i.e., where the discrete difference changes sign),
 plots the signal and mark these turning points,
 saves the figure as a PDF file,
 and returns a NumPy array containing the indices of the detected points
 
 """
 

def detect_turning_points(signal, filename="turning_points.pdf"):
    
    differences = np.diff(signal)
    
    signs = np.sign(differences)
    
    sign_changes = np.diff(signs)
    
    turning_points = np.where(sign_changes != 0)[0] + 1
    
    plt.figure(figsize=(12, 6))
    plt.plot(signal, 'b-', linewidth=2, label='Signal')
    
    if len(turning_points) > 0:
        plt.plot(turning_points, signal[turning_points], 'rx', markersize=8, label='Turning Points')
    
    plt.xlabel('Index')
    plt.ylabel('Signal Value')
    plt.title('Signal with Turning Points')
    plt.legend()
    plt.grid(True, alpha=0.15)
    
    
    plt.savefig(filename, format='pdf')
    plt.close()
    
    return turning_points



x = np.linspace(0, 4*np.pi, 1000)
print()
test_signal = np.sin(x)
result = detect_turning_points(test_signal)