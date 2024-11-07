f = open("about_me.txt", "a")
f.close()

f = open("about_me.txt", "a")
f.write("If you could do anything for your 'perfect' night out, where would you go and what would you do?\n")
f.write("Answer: I would go to a nice dinner, then catch a live concert or sporting event.\n")
f.close()

# Step 10: Open the file in read mode and print the entire content
f = open("about_me.txt", "r")
print(f.read())
f.close()

# Step 12: Read and print the first 50 characters, then the next 50
f = open("about_me.txt", "r")
print(f.read(50))
print(f.read(50))
f.close()

# Step 13: Experiment with readline()
f = open("about_me.txt", "r")
print(f.readline(10))  # Reads the first 10 characters of the first line
print(f.readline())    # Reads the remainder of the first line

# Loop to read the next 4 lines
for i in range(1, 5):
    print(f.readline())
f.close()

# Step 14: Experiment with readlines()
f = open("about_me.txt", "r")
print(f.readlines())          # Reads all lines into a list
print(f.readlines(1))         # Reads the entire file again since readlines() was used before
print(f.readlines(10))        # Reads up to 10 characters as lines
print(f.readlines(100))       # Reads up to 100 characters as lines
print(f.readlines(-1))        # Reads everything remaining in the file
f.close()

f = open("about_me.txt", "r")

# Step 15: Using different read methods and storing results in variables
first_50_chars = f.read(50)  # First 50 characters

# Capturing the next 4 lines using readline() in a loop and storing in a list
next_four_lines = []
for _ in range(4):
    next_four_lines.append(f.readline().strip())

# Read the next 100 characters as a list using readlines()
next_100_chars_lines = f.readlines(100)

f.close()

# Step 16: Print results
print("First 50 characters:", first_50_chars)
print("Next four lines, as list by line:", next_four_lines)
print("Next 100 characters, as list by line, rounded up to complete lines:", next_100_chars_lines)

