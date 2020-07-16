# open the file for read access
with open("data.json") as data:
    # read the file to the variable state
    states = data.read()

# show what we just read
print(states)
