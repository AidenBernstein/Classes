import math

def main():
    inner_radius = float(input("enter inner diameter(in cm): "))
    inner_radius = inner_radius/2

    outer_radius = float(input("enter outer diameter(in cm): "))
    outer_radius = outer_radius/2

    coil_length = float(input("enter length of coil(in cm): "))

    density = (math.pi * math.sqrt(3))/6

    for n in range(26):
        wire_length = (((math.pi * (outer_radius ** 2)) - (math.pi * (inner_radius ** 2))) * coil_length * density) / (math.pi * ((0.0127 * math.pow(92, ((36 - n)/39))) / 2) ** 2)
        print(n, "ga\t%.2f m" % (wire_length/100))


main()