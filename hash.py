import hashlib
import random
import string

def generate_captcha():
    # Generate a random CAPTCHA challenge
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    # Generate a unique validation key using a hash function
    validation_key = hashlib.sha1(captcha_text.encode()).hexdigest()
    return captcha_text, validation_key

def validate_captcha(user_response, validation_key):
    # Recalculate the hash based on user response
    expected_key = hashlib.sha1(user_response.encode()).hexdigest()
    return expected_key == validation_key

# Generate CAPTCHA
captcha_text, validation_key = generate_captcha()
print(f"CAPTCHA: {captcha_text}, Validation Key: {validation_key}")

# Simulate user response
user_response = input("Enter the CAPTCHA text: ")
if validate_captcha(user_response, validation_key):
    print("CAPTCHA validation successful!")
else:
    print("CAPTCHA validation failed.")