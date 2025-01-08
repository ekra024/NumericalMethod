# Save this code as project3.py
import numpy as np

def handle_missing_values(data):
    indices = np.arange(len(data))
    known_indices = indices[~np.isnan(data)]
    known_values = data[~np.isnan(data)]
    interpolated = np.interp(indices, known_indices, known_values)
    return interpolated

def main():
    data = input("Enter data points separated by spaces (use 'nan' for missing values): ").split()
    data = np.array([float(x) if x != 'nan' else np.nan for x in data])
    print("Data with missing values handled:", handle_missing_values(data))

if __name__ == "__main__":
    main()
