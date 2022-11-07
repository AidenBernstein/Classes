import math

def main():
    inner_radius = float(input("enter inner diameter(in cm): "))
    inner_radius = inner_radius/2

    outer_radius = float(input("enter outer diameter(in cm): "))
    outer_radius = outer_radius/2

    coil_length = float(input("enter length of coil(in cm): "))

    density = (math.pi * math.sqrt(3))/6
    print("Gauge", "%14s" % "Wire dia.", "%13s" % "Wire len.", "%13s" % "Resistance", "%18s" % "Total Loops")

    for n in range(26):
        diameter = (0.0127 * math.pow(92, ((36 - n)/39)))
        wire_length = (((math.pi * (outer_radius ** 2)) - (math.pi * (inner_radius ** 2))) * coil_length * density) / (math.pi * (diameter/2) ** 2)
        resistance = wire_length * 0.0333
        loops = math.floor(((outer_radius - inner_radius))/diameter) * (math.floor((coil_length)/diameter))

        print(f"{n:2}", "ga%10.2f mm" % (diameter*10), "%10.2f m" % (wire_length/100), "%10.2f ohms" % (resistance), "%10d loops" % (loops))
        if (n % 4) == 0:
            print()


main()