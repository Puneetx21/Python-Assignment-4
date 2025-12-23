file_name = "file.txt"

# Creating a file using xt or wt

with open(file_name,"wt") as fh:
   text_data =  input("Enter Some data to add in file : ")
   fh.write(text_data + "\n")

print(f"Data added successfully in {file_name}.")

with open(file_name,"at") as fh:
    new_data = input("Enter new data to append : ")
    fh.write(new_data)

print(f"New data appended successfully in {file_name}")

with open(file_name,"rt") as fh:
    print("Available content : ")
    content =  fh.readlines()
    for data in content:
        print(data.strip())
