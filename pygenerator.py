import random
import string

def generate_random_number(length):
    """Generate a random number with the specified length."""
    if length <= 0:
        return "Length must be greater than 0"
     
        
    return ''.join(random.choices(string.digits, k=length))

def generate_random_letters(length):
    """Generate a random string of letters with the specified length."""
    if length <= 0:
        return "Length must be greater than 0"
    else:
        print("Invalid Letter")
    
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_password(length):
    """Generate a random password with a mix of letters, digits, and symbols."""
    if length <= 0:
        return "Length must be greater than 0"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))
    

# Random functions:
random_number = generate_random_number(5)
random_letters = generate_random_letters(8)
random_password = generate_random_password(12)

print("Random Number:", random_number)
print("Random Letters:", random_letters)
print("Random Password:", random_password)
