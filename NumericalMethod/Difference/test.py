import numpy as np

def forward_difference_table(values):
    n = len(values)
    table = np.zeros((n, n))
    table[:, 0] = values

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    return table

def backward_difference_table(values):
    n = len(values)
    table = np.zeros((n, n))
    table[:, 0] = values

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            table[i, j] = table[i, j - 1] - table[i - 1, j - 1]

    return table

def central_difference(values, x_values, x_target):
    n = len(values)
    h = x_values[1] - x_values[0]
    middle = n // 2

    # Calculate central differences
    table = forward_difference_table(values)
    differences = [table[middle - i, 2 * i] for i in range((n - 1) // 2 + 1)]

    # Compute central difference interpolation
    t = (x_target - x_values[middle]) / h
    result = values[middle]
    factor = 1
    for i, diff in enumerate(differences):
        factor *= t - i if i % 2 == 0 else t + i
        result += (diff / np.math.factorial(i + 1)) * factor

    return result

def find_missing_value(x_values, y_values):
    table = forward_difference_table(y_values)
    missing_index = y_values.index(None)
    estimated_value = table[missing_index, 0]
    return estimated_value

def print_table(table):
    print("\nDifference Table:")
    for row in table:
        print([round(val, 4) if val != 0 else "" for val in row])

if __name__ == "__main__":
    print("Numerical Methods Menu:")
    print("1. Forward Difference Table")
    print("2. Backward Difference Table")
    print("3. Central Difference Approximation")
    print("4. Find Missing Value Using Differences")
    
    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4]:
        n = int(input("Enter the number of data points: "))
        x_values = list(map(float, input("Enter x values separated by spaces: ").split()))

        if choice != 4:
            y_values = list(map(float, input("Enter y values separated by spaces: ").split()))
        else:
            y_values = []
            print("Enter y values (use 'None' for missing value):")
            for _ in range(n):
                val = input()
                y_values.append(float(val) if val.lower() != 'none' else None)

        if choice == 1:
            table = forward_difference_table(y_values)
            print_table(table)

        elif choice == 2:
            table = backward_difference_table(y_values)
            print_table(table)

        elif choice == 3:
            x_target = float(input("Enter the value of x to approximate: "))
            result = central_difference(y_values, x_values, x_target)
            print(f"Approximation at x = {x_target}: {result}")

        elif choice == 4:
            result = find_missing_value(x_values, y_values)
            print(f"Estimated missing value: {result}")

    else:
        print("Invalid choice. Please select a valid option.")
