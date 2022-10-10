# Open the required file I/O
file_pop = open("worldpop.txt", "r")
file_area = open("worldarea.txt", "r")
file_density = open("world_pop_area.txt", "w")

# Declaration of list for data
nations = []
population = []
area = []
density = []


# Function that calculate the density of the nation
# with the index i and return the double rounded to
# two decimal
def calc_density(i):
    return round(population[i] / area[i], 2)


def main():
    # Read the data from the file_pop file
    # and append data to nations and populations list
    for line in file_pop.readlines():
        record = line.split()

        nations.append(" ".join(record[:-1]))
        population.append(int(record[-1]))

    # Read the data from the file_area file
    # and append data to area list
    for line in file_area.readlines():
        record = line.split()

        area.append(int(record[-1]))

    # Write result to file_density using the
    # calc_density file
    for index, name in enumerate(nations):
        file_density.write(f"{name} {calc_density(index)}\n")


main()
