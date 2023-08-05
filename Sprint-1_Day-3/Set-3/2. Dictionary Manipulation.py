# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. 
# Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"


def add(pair, Dict):
    if pair[0] in Dict:
        return f"Name: {pair[0]} is already present in Dictionary."
    
    Dict[pair[0]] = pair[1]
    return f"Name: {pair[0]} is added along with Age: {pair[1]}."

def update(pair, Dict):
    if pair[0] in Dict:
        Dict[pair[0]] = pair[1]
        return f"Name: {pair[0]} is updated along with Age: {pair[1]}."
    
    return f"Name: {pair[0]} is not Present in the Dictionary."

def delete(name, Dict):
    if name in Dict:
        del Dict[name]
        return f"Name: {name} is Deleted from Dictionary."
    
    return f"Name: {name} is not present in Dictionary."


# Add Operation
Dict = dict()
print(add(("Sima", 25), Dict))
print(add(("Sima", 26), Dict))
print(Dict)

# Update Operation
print(update(("Sima", 27), Dict))
print(update(("Asha", 54), Dict))
print(Dict)

# Delete Operation
print(delete("Asha", Dict))
print(delete("Sima", Dict))
print(Dict)