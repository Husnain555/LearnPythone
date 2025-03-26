file_path = "/home/southville/cvtindell.txt"

# Read existing numbers
with open(file_path, "r") as f:
    existing_numbers = f.read().split()  # Read and split into a list of strings

# Open in append mode and write only new numbers
with open(file_path, "a") as f:
    for i in range(1, 10):
        print(i)
        if str(i) not in existing_numbers:  # Check if number already exists
            f.write(str(i) + "\n")  # Write new number with a newline

# Read and print the file content
with open(file_path, "r") as f:
    print(f.read(), "here is the highest")
