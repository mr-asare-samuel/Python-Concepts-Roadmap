import sys

if len(sys.argv) < 3:
    print("Usage: python3 ledger_add.py <category> <amount>")
    sys.exit(1)

category = sys.argv[1]
amount = float(sys.argv[2])

print(f"Recorded expense: {category} -> ${amount:.2f}")

#run in the terminal: python3 ledger_add.py "Food" 100.00
# this prints "Recorded expense: Food -> $100.00"

"""run in the terminal: python3 ledger_add.py "Food" 100.00
# this prints "Usage: python3 ledger_add.py <category> <amount>"
# and exits the program

"""run in the terminal: python3 ledger_add.py "Food" 100.00
 this prints 'Usage: python3 ledger_add.py <category> <amount>' and exits the program

run in the terminal: python3 ledger_add.py 'Food' '100.00'
this prints 'Recorded expense: Food -> $100.00'"""