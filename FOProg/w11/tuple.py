def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

# Call the function and unpack the returned tuple
length = float(input("Give the length of a rectangle:\n"))
width = float(input("Give the width of a rectangle:\n"))

result = calculate_area_and_perimeter(length, width) # tuple
area = result[0]
perimeter = result[1]

print(f"""For length {length} and width {width},
the area is {area:.2f} and perimeter is {perimeter:.2f}.""")
