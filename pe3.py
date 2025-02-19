import string
import datetime

# A. Encoding function (ensure lowercase output)
def encode(input_text, shift):
    """
    Shift each letter in the input_text by 'shift' positions.
    Non-letter characters remain unchanged.
    Returns a tuple: (lowercase alphabet list, encoded text)
    """
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""

    for char in input_text:
        if char.isalpha():
            # Shift letter to lowercase before encoding
            new_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            encoded_text += new_char
        else:
            encoded_text += char

    return (alphabet, encoded_text)

# B. Decoding function (same handling for lowercase output)
def decode(input_text, shift):
    """
    Shift each letter in the input_text backward by 'shift' positions.
    Non-letter characters remain unchanged.
    Returns the decoded text.
    """
    return encode(input_text, -shift)[1]  # Reuse encode to shift back

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date if creation_date else datetime.date.today()
        self.balance = balance

        # Ensure the creation date is not in the future
        if self.creation_date > datetime.date.today():
            raise Exception("Account creation date cannot be in the future.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit denied: Amount must be positive.")
            return

        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied: Insufficient funds.")
            return

        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance:.2f}")

    def view_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # Ensure account is at least 180 days old
        if (datetime.date.today() - self.creation_date).days < 180:
            print("Withdrawal denied: Account must be at least 180 days old.")
            return  

        # Ensure there are enough funds (No overdraft allowed)
        if amount > self.balance:
            print("Withdrawal denied: Insufficient funds. Overdrafts are not permitted.")
            return  

        # Perform the withdrawal
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            # Allow overdraft but apply a $30 fee
            self.balance -= (amount + 30)
            print(f"Overdraft occurred! Withdrawal successful with $30 fee. New balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
# -----------------------------
# TEST CASES
# -----------------------------

# Test Caesar cipher encoding and decoding
print(encode("a", 3))  # Expected: (alphabet list, "d")
print(decode("d", 3))  # Expected: "a"
print(encode("XyZ", 3))  # Expected: (alphabet list, "abc") -> lowercase enforced
print(decode("abc", 3))  # Expected: "xyz"
print(encode("Calmly we walk on this April day", 10))  # Expected shifted text (all lowercase)
print(decode("mkvwvi go gkvu yx drsc kzbsv nki", 10))  # Expected original text (all lowercase)

# Test BankAccount functionality
account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.view_balance())  # Expected: 50

# Test SavingsAccount functionality (Set date 180 days ago to allow withdrawal)
savings = SavingsAccount(balance=200, creation_date=datetime.date.today() - datetime.timedelta(days=180))
savings.withdraw(100)  # Should work now

# Test CheckingAccount functionality
checking = CheckingAccount(balance=50)
checking.withdraw(70)  # Should apply overdraft fee and print new balance
print(checking.view_balance())  # Expected: -50