# Save this code as project2.py
def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
    return triangle

def main():
    rows = int(input("Enter the number of rows for Pascal's Triangle: "))
    triangle = generate_pascals_triangle(rows)
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()
