import numpy as np
import matplotlib.pyplot as plt


"""
        
        A function column_range_plot(A, filename="column_ranges.pdf") that;
        receives a 2D NumPy array A,
        computes the range (maximum minus minimum) of each column,
        create a bar plot showing the ranges of all columns,
        saves the plot as a PDF file,
        and returns a 1D NumPy array containiing the column ranges.
        
        
"""

def column_range_plot(A, filename="column_ranges.pdf"):
    
    col_ranges = np.max(A, axis=0) - np.min(A, axis=0)
    colors = ['steelblue','purple', 'forestgreen']
   
    plt.figure(figsize=(12, 8))
    bars = plt.bar(range(len(col_ranges)), col_ranges, color=[color for color in colors], edgecolor='white')
    
    for i, bar in enumerate(bars):
        bar.set_label(f'{i+1} - columns range')
        
    plt.xlabel('Column Index', color='coral', fontsize=15)
    plt.ylabel('Range (Max - Min)', color='coral', fontsize=15)
    plt.title('Range of Each Column', fontsize=16, fontweight='bold')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.legend(title = 'Legend', loc = 'upper left', frameon=False, fontsize=12);
 
   
    plt.savefig(filename, format='pdf')
    plt.close()
   
    return col_ranges



data = np.array([[3, 5, 2],
                 [3, 2, 8],
                 [7, 9, 4]])

# Get ranges and save plot
ranges = column_range_plot(data, "my_ranges.pdf")
print(ranges)