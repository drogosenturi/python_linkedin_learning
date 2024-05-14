from datetime import datetime
## while loops
datetime.now().second
datetime.now().second + 2
# while loop that waits 2 seconds then prints
wait_until = (datetime.now().second + 2) % 60

# Pass statement
while datetime.now().second != wait_until:
    pass # to fill in space under while loop
print(f'We are at {wait_until} seconds!')

# Break statement
wait_until = (datetime.now().second + 2) % 60
while True:
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds!')
        break # breaks the first loop it is in

# Continue
# skips lines that follow it inside the while loop
while datetime.now().second != wait_until:
    continue # usually see continue in an if statement
    print("still waiting") # to fill in space under while loop
print(f'We are at {wait_until} seconds!')

wait_until = (datetime.now().second + 2) % 60
while True:
    if datetime.now().second == wait_until:
        continue
    break
print(f'We are at {wait_until} seconds!')