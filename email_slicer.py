# Get the users email user name
email = input("What is your email address: ").strip()

# Slice out user name
user = email[:email.index("@")]

# Slice out domain name
domain = email[email.index("@") + 1:]

# Format message
if domain == "gmail.com":
    gmail = "Google"
    print("Your username is {} and all your emails are being tracked by {}.".format(user, gmail))
else:
    print("Your username is {} and your email address is at {}.".format(user, domain))
