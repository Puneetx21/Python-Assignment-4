file_name = "sample.txt"

try:
    with open(file_name, "rt") as fh:
        read = fh.readlines()
        print("Reading the content :")
        i = 0
        for line in read:
            i = i + 1
            line = line.strip()
            print(f"Line {i} :{line}")


except FileNotFoundError :
    print(f"Error : The file {file_name} is not Found.")
