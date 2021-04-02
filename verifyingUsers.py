unconfirmed_users = ['alice','bob','candace','joe','sinthiya']

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying User: " + current_user.title())
    confirmed_users.append(current_user)

print("Users Verified Successfully.\n\nFollowing is the list of verified users.\n")

for verifiedUsers in confirmed_users:
    print(verifiedUsers.title())