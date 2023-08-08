import random

# Global constant variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Function that assigns symbols to the slot machine columns
def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            allSymbols.append(symbol)

    columns = [] # Define columns list

    for _ in range(cols): # Generate a column for ever column that user selects (1-3)
        column = []
        currentSymbols = allSymbols[:] # Symbols that app can currently select is = a copy of allSymbols
        for _ in range(rows): # Loop through number of values app needs to generate which is = number of rows selected in the slot machine
            value = random.choice(currentSymbols) # Random value is chosen for the list
            currentSymbols.remove(value) # Remove the value that has been selected at random
            column.append(value) # Add value to the column

        columns.append(column) #Add the column to the columns list

    return columns

# Function that handles printing column values
def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: # if i is not = the max index print the | if not do not print |
                print(column[row], end=" | ") # by default end= /n which is new line which tells console to move to next line, by changing it to | the end will read |
            else:
                print(column[row], end="")

        print() # Empty print() so that a new line is generated after the for loop ends.

# Function that handles user deposits
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        # Conditional checking to see if amount user inputted is a number
        if amount.isdigit():
            amount = int(amount) # Converts string to an integer

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# Function that handles number of lines user wants to bet on
def getNumberOfLines():
    while True:
        lines = input("Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        # Conditional checking to see if the lines user inputted is a number
        if lines.isdigit():
            lines = int(lines) # Converts string to an integer

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines (1-3).")
        else:
            print("Please enter a number.")

    return lines

# Function that handles user bet
def getBet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        # Conditional checking to see if amount user inputted is a number
        if amount.isdigit():
            amount = int(amount) # Converts string to an integer

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def app():
    balance = deposit()
    lines = getNumberOfLines()

    # While loop to check if the user has sufficient funds for the bet they are trying to make
    while True: 
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You do not have sufficient funds, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")

    slots = getSlotMachineSpin(ROWS, COLS, symbol_count)
    printSlotMachine(slots)

app()
