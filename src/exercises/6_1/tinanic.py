from os import path

# Get the absolute filepath of the file to read
filepath = path.abspath("titanic.csv")

with open(filepath) as file:
    # Print the absolute filepath of the file to read
    print(f"Reading CSV file: {filepath}")

    # Read the CSV file
    lines = file.readlines()

    # Print all the lines
    for line in lines:
        print(line.strip())

    # Display the total number of lines
    print("The total number of lines: " + line)

    # Display only the names of the passengers
    lines.pop(0)
    for line in lines:
        sp = line.split(",")
        name = f"{sp[4].strip()[0:-1]} {sp[3].strip()[1:]}"
        print(name)

    # Summary the number of passengers of each class
    number_in_class = [None] + [0] * 3
    for line in lines:
        cls = int(line.split(",")[2])
        number_in_class[cls] += 1

    with open("summary.txt", "w") as output:
        output.write(f"Number of first class passengers: {number_in_class[1]}\n")
        output.write(f"Number of second class passengers: {number_in_class[2]}\n")
        output.write(f"Number of third class passengers: {number_in_class[3]}\n")
