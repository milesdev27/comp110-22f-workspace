"""An example of for in syntax."""

names: list[str] = ["Miles", "Kaki", "Ezri", "Marc"]

# Example of iterating through names using a while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for..in loop is the same as the while loop above
for name in names:
    print(name)