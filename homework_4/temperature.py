def convert_cel_to_far(C: float):

    F = C * 9/5 + 32

    return F

def convert_far_to_cel(F: float):

    C = (F - 32) * 5/9

    return C


a = float(input("Enter a temperature in degrees F: "))
print(f"{a} degrees F = {convert_far_to_cel(a):.2f} degrees C")

b = float(input("Enter a temperature in degrees C: "))
print(f"{b} degrees C = {convert_cel_to_far(b):.2f} degrees F")