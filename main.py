### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    },
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###


class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
        Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry there is not enough {item}")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
        Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        large_dollars = int(input("How many large dollars?: ")) * 1.00
        half_dollars = int(input("How many half dollars?: ")) * 0.50
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        total = large_dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
        Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry thats not enough money, Your money has been refunded")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
        Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon Appetit!")

    def report(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} slice(s)")


### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        print("Turning off the machine.")
        break
    elif choice == "report":
        machine.report()
    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]
        
        if machine.check_resources(ingredients):
            
            inserted_coins = machine.process_coins()
            
            if machine.transaction_result(inserted_coins, cost):
                machine.make_sandwich(choice, ingredients)
                
    else:
        print("invalid option. Please choose small, medium, larg, off, or report.")
