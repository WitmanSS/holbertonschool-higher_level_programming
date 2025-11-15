#!/usr/bin/python3
output = ""
# Iterate backwards from 122 ('z') down to 97 ('a')
for i in range(122, 96, -1):
    # Check if the ASCII value is even or odd to determine case
    if i % 2 == 0:
        # Even ASCII (z, x, v, ...) are printed as lowercase
        output += chr(i)
    else:
        # Odd ASCII (y, w, u, ...) are converted to uppercase by subtracting 32
        output += chr(i - 32)
# Print the entire built string using one formatted print function, no newline
print("{}".format(output), end="")
