#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def check_length(password):
    return len(password) >= 8

def check_digits(password):
    return bool(re.search(r"\d", password))

def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password))

def check_lowercase(password):
    return bool(re.search(r"[a-z]", password))

def check_symbols(password):
    return bool(re.search(r"[!@#$%^&*()_+]", password))

def check_password_strength(password):
    checks = [
        check_length,
        check_digits,
        check_uppercase,
        check_lowercase,
        check_symbols
    ]
    score = sum(check(password) for check in checks)

    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    else:
        return "Weak"

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")


# In[ ]:




