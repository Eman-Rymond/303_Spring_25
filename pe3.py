import string
import datetime

# A. Encoding function
def encode(input_text, shift):
    encoded_text = ''
    
    for char in input_text:
        if char.isalpha():  
            if char.islower():
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encoded_text += new_char
        else:
            encoded_text += char
    
    return encoded_text  # Only return encoded text


# B. Decoding function
def decode(input_text, shift):
    decoded_text = ''
    
    for char in input_text:
        if char.isalpha():  
            if char.islower():
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decoded_text += new_char
        else:
            decoded_text += char
    
    return decoded_text


# A. BankAccount class
class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date and creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future")
        
        self.name = name
        self.ID = ID
        self.creation_date = creation_date if creation_date else datetime.date.today()
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def view_balance(self):
        return self.balance


# B. SavingsAccount class (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        # Withdrawal allowed only after 180 days
        if (datetime.date.today() - self.creation_date).days < 180:
            raise Exception("Cannot withdraw before 180 days of account creation.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")


# C. CheckingAccount class (inherits from BankAccount)
class CheckingAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if amount > self.balance:
            # Overdraft fee applies if balance is negative
            fee = 30
            self.balance -= (amount + fee)
            print(f"Overdraft fee applied. Withdrawal successful. New balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")


# -----------------------------
# TEST CASES
# -----------------------------

# Test Caesar cipher encoding and decoding
print(encode("a", 3))  # Expected: "d"
print(decode("d", 3))  # Expected: "a"
print(encode("XyZ", 3))  # Expected: "AbC"
print(decode("AbC", 3))  # Expected: "XyZ"
print(encode("Calmly we walk on this April day", 10))  # Expected shifted text
print(decode("Mkvwvi go gkvu yx drsc Kzbsv nki", 10))  # Expected original text

# Test BankAccount functionality
account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.view_balance())  # Expected: 50

# Test SavingsAccount functionality (Set date 200 days ago to allow withdrawal)
savings = SavingsAccount(balance=200, creation_date=datetime.date.today() - datetime.timedelta(days=200))
savings.withdraw(100)  # Should work now

# Test CheckingAccount functionality
checking = CheckingAccount(balance=50)
checking.withdraw(70)  # Should apply overdraft fee and print new balance
print(checking.view_balance())  # Expected: -50 (after overdraft fee)

