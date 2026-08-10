# The Syndicate just intercepted a transmission containing the master code for a rival's vault. 
# But the signal is corrupted with garbage text and duplicate numbers.

# The Intercepted String: "42-XRay-15-99-Alpha-42-15"

corrupted_signal = "42-XRay-15-99-Alpha-42-15"

# 1. Create the empty SET
real_numbers = set()

# 2. Split the string by the exact hyphen
pieces = corrupted_signal.split("-")

# 3. The Loop
for piece in pieces:
    
    # 4. The Blast Shield
    try:
        # Try to convert to integer
        number = int(piece)
        
        # Add the valid number to the set (NOW INSIDE THE TRY BLOCK)
        real_numbers.add(number)
        
    except ValueError:
        # Use the keyword that skips to the next iteration (NOW INSIDE THE EXCEPT BLOCK)
        continue

# 5. Calculate the final passcode using the sum() function
final_passcode = sum(real_numbers)

print("Vault Passcode:", final_passcode)