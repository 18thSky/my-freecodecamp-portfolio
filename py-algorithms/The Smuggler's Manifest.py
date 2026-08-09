# # You are writing a command-line tool for the Syndicate to calculate the total value of smuggled goods. 
# # The data comes in messy, and the smugglers often make typos.

# 1.. We need to accept the inputs from users and then we need check the datatype then segregate in separate items.
# 2. Once we have name and price from user input we will be loop to split each and every item using -.
# 3. we need to add try.. block of loop and then expect error(index,value,syntax and all) or result.
# 4. We need to dictionary to store if the item is in the dictionary it can it price. We need to add unique_categories and using .add() item name to it.
# 5. At the need we need return the finally dictionaries and print them item and price and if any unique items

# 1. Setup the empty dictionary and set
inventory = {

}
unique_categories = set() # Note: we use set() to create an empty set, not {}

# 2. Get the input and split it into a list
user_input = input("Enter smuggled goods: ")
items_list = user_input.split(", ")

# 3. The Loop
for item in items_list:
    # Split the current item by the hyphen
    parts = item.split("-")
    name = parts[0].strip()
    
    # 4. The Blast Shield
    try:
        # Try to convert the second part to an integer
        price = int(parts[1])
    except ValueError:
        print(f"Error: Invalid price for {name}. Skipping...")
        # Use the keyword that skips to the next iteration of the loop
        continue
        
    # 5. Dictionary & Set Logic (This only runs if the try block succeeds)
    if name in inventory:
        # Add the price to the existing total
        inventory[name] += price
    else:
        # Create the new entry in the dictionary
        inventory[name] = price
        
    # Add the name to the unique set
    unique_categories.add(name)

# 6. Final Output
print("\n--- Final Audit ---")
print("Inventory:", inventory)
print("Categories:", unique_categories)