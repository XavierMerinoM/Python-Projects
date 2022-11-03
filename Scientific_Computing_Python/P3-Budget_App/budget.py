# Complete the Category class in budget.py.
# It should be able to instantiate objects based on
# different budget categories like food, clothing,
# and entertainment.
# When objects are created, they are passed in
# the name of the category. The class should have an
# instance variable called ledger that is a list.
class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category

    # A deposit method that accepts an amount and
    # description. If no description is given,
    # it should default to an empty string.
    # The method should append an object to the
    # ledger list in the form of
    # {"amount": amount, "description": description}.
    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})

    # A get_balance method that returns the current
    # balance of the budget category based on the
    # deposits and withdrawals that have occurred.
    def get_balance(self):
        result = 0

        for i in range(len(self.ledger)):
            result += self.ledger[i]['amount']

        return result

    # A check_funds method that accepts an amount as an
    # argument. It returns False if the amount is
    # greater than the balance of the budget category
    # and returns True otherwise. This method should be
    # used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        balance = self.get_balance()

        if amount > balance:
            return False
        else:
            return True

    # A withdraw method that is similar to the deposit
    # method, but the amount passed in should be stored
    # in the ledger as a negative number.
    # If there are not enough funds, nothing should be
    # added to the ledger. This method should return True
    # if the withdrawal took place, and False otherwise.
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount, "description": description})

            return True
        else:
            return False

    # A transfer method that accepts an amount and
    # another budget category as arguments. The method
    # should add a withdrawal with the amount and
    # the description "Transfer to [Destination Budget
    # Category]". The method should then add a deposit
    # to the other budget category with the amount and
    # the description "Transfer from [Source Budget
    # Category]". If there are not enough funds,
    # nothing should be added to either ledgers.
    # This method should return True if the transfer
    # took place, and False otherwise.
    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + budget.category)
            budget.deposit(amount, 'Transfer from ' + self.category)

            return True
        else:
            return False

    # Special function to use in the create_spend_chart function
    # Returns the sum of withdraws
    def get_spent(self):
        result = 0

        for i in range(len(self.ledger)):
            value = self.ledger[i]["amount"]

            if value < 0:
                result += value

        return round(result, 2)

    # When the budget object is printed it should display:
    # * A title line of 30 characters where the name
    #   of the category is centered in a line of
    #   * characters.
    # * A list of the items in the ledger. Each line
    #   should show the description and amount. The
    #   first 23 characters of the description should
    #   be displayed, then the amount. The amount should
    #   be right aligned, contain two decimal places,
    #   and display a maximum of 7 characters.
    # * A line displaying the category total.
    def __str__(self):
        # Initialize variables
        max_len = 30
        max_len_dsc = 23
        max_len_amn = 7
        message = ''
        description = ''
        amount = ''

        # Title line
        message += ((max_len - len(self.category)) // 2) * '*' + self.category + ((max_len - len(self.category)) // 2) * '*'
        # If len of category is odd, add an *
        # to complete the 30 characters
        # This is due to the integer division
        if len(self.category) % 2 == 1:
            message += '*'

        # Add a new line
        message += '\n'

        # List items from ledger
        for i in range(len(self.ledger)):
            description = self.ledger[i]["description"]
            amount = str(self.ledger[i]["amount"])

            # Check if the amount is an integer to add decimals
            if '.' not in amount:
                amount += '.00'

            # Validate the char limit of description
            if len(description) > max_len_dsc:
                description = description[:max_len_dsc]
            else:
                description += ' ' * (max_len_dsc - len(description))

            # Validate the char limit of amount
            if len(amount) > max_len_amn:
                amount = amount[:max_len_amn-1]
            else:
                amount = ' ' * (max_len_amn - len(amount)) + amount

            message += description + amount + '\n'

        # Shows total

        message += 'Total: ' + str(self.get_balance())

        return message

def create_spend_chart(categories):
    # Initialize variables
    message = ''
    total = 0
    percentage = 0
    data = {}
    ordered_data = {}
    max_len = 0

    # Show the first message
    message += 'Percentage spent by category' + '\n'

    # Get data from the list categories in a dictionary
    for category in categories:
        # Check max length of the categories. Will use it later.
        aux = len(category.category)
        if aux > max_len:
            max_len = aux

        data[category.category] = category.get_spent()

    # Sum values to get percentages later
    total = sum(data.values())

    # Order (reverse) the dictionary value
    # for key in sorted(data, key=data.get):
    for key in data:
        # Get the percentage
        percentage = round((data[key] / total) * 100, 0)
        # To round down, get the decimal value and then multiply by 10
        percentage = (percentage // 10) * 10
        ordered_data[key] = percentage

    # Print percentage section
    for perc in range(100, -1, -10):
        # Depending on the len of the number, add space(s)
        if len(str(perc)) == 2:
            message += ' '
        elif len(str(perc)) == 1:
            message += '  '

        message += str(perc) + '| '

        # Check the dictionary to add 'o' char
        # If actual value equals percentage, add
        # Else, break
        for key in ordered_data:
            if ordered_data[key] >= perc:
                message += 'o  '
            else:
                message += '   '

        message += '\n'

    # First, add some chars according to the format
    # It is 3 hypens per each category plus the initial hypen
    # And new line
    message += ' ' * 4 + '-' + '---' * (len(categories)) + '\n'

    # Add text in vertical orientation
    # This for goes to the index of longest key
    for i in range(max_len):
        # Always add initial 5 spaces
        message += ' ' * 5

        # Adds texts char by char cheking it
        # If there is no char, add spaces
        for key in ordered_data:
            if i <= len(key) - 1:
                message += key[i] + '  '
            else:
                message += ' ' * 3

        message += '\n'

    # Delete the extra new line char in the end
    message = message[:len(message)-1]

    return message