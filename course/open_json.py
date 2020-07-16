# import the JSON module
import json

# open the file for read access
with open("data.json") as data:
    # read the file to the variable state
    text = data.read()
    # parse the text to a dict
    states = json.loads(text)

# show the object details
# first object from the array [0]
print("Pin: " + str(states[0]['pin']))
print("In/Out: "+ states[0]['io'])

# second object from the array [1]
print("Pin: " + str(states[1]['pin']))
print("In/Out: "+ states[1]['io'])

print("\nREAD IN LOOP")
# read the data in a for loop
for state in states:    
    print("Pin: " + str(state['pin']))
    print("In/Out: "+ state['io'])
