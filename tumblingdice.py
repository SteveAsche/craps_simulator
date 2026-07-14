from random import randint
# create a dice rolling simulation

class Die:
    """A class representing a single die."""
    
    def __init__(self, sides=6):
        """Initialize the die with a given number of sides (default is 6)."""
        self.sides = sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.sides)
    
die1 = Die()
die2 = Die()

# Roll the dice 10 times and store the results in a list
roll_results = []
for _ in range(10):
    roll_results.append((die1.roll(), die2.roll()))

print("Roll results:")
for roll in roll_results:
    print(roll) 

for roll in roll_results:
    if roll[0] == roll[1]:
        print(f"Double rolled: {roll[0]} and {roll[1]}")
    else:
        print(f"Rolled: {roll[0]} and {roll[1]}")
        print(f"Total =  {roll[0] + roll[1]}")
              
