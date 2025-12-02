# Exercise 1
print("Checking login attempts...")
login_attempts = [("alice", "success"),("bob", "failed"),("bob", "failed"),("charlie", "success"),("bob", "failed"),("alice", "failed")]
failed_attempts = {}
for username, attempt in login_attempts:
    if attempt == "failed":
        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1
for username in failed_attempts:
    if failed_attempts[username] >= 3:
        print("ALERT: User " + username + " has " + str(failed_attempts[username]) + " failed login attempts")