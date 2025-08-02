import hashlib
import random
import string

def generate_captcha():
    # Generate a random CAPTCHA challenge
    # captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    captcha_text = "vjdc"
    # Generate a unique validation key using a hash function
    validation_key = hashlib.sha1(captcha_text.encode()).hexdigest()
    print(validation_key)
    # Regenerate a unique validation key of first hash
    nd_validation_key = hashlib.sha1(validation_key.encode()).hexdigest()
    print(nd_validation_key)
    return captcha_text, validation_key

print(generate_captcha())