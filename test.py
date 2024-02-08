def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    r1 = round(number_of_cans)
    print(f"You'll need {r1} cans of paint.")

test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
