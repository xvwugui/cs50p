name = input("Please enter your name: ")

name = name.strip().title()
first, last = name.split(" ")

print(f"Hello, {first} {last}")
