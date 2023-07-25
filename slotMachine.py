import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

rows = 3
cols = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end=" ")
        print()


def deposit():

    while True:
        amount = input('What would you like to deposit $:')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be in digits!')
        else:
            print('Please Enter a amount in number!')

    return amount


def get_num_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on :')
        if lines.isdigit():
            lines = int(lines)
            if lines <= MAX_LINES:
                break
            else:
                print('Lines Must be less than maximum lines!!')
        else:
            print('Please Enter a number!')

    return lines


def bet_amount():
    while True:
        bet = input('How much you would like to bet$:')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Bet amount must be {MIN_BET} to {MAX_BET} ')
        else:
            print('Please Enter a amount in number!')

    return bet


def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = bet_amount()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have that much of amount to bet.Your current balance is :${balance} ')
        else:
            break
    print(f'you are betting {bet} for {lines} lines.Your total bet is {total_bet}! ')
    slots=get_slot_machine_spin(rows,cols,symbol_count)
    print_slot_machine(slots)

main()
