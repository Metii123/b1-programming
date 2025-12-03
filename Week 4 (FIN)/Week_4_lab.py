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
print(" ")
# Exercise 2
print("Scanning network devices...")
devices = [ ("192.168.1.10", [22, 80, 443]),("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,80, 3389])]
risky_ports = [21, 23, 3389]
risk_count = 0
for ip, open_ports in devices:
    for ports in open_ports:
        if ports in risky_ports:
            print("WARNING: "+ ip + "has risky port " + str(ports) + " open")
            risk_count = risk_count + 1
print(f"Scan complete: {risk_count} security risks found")
print("")
# Exercise 3
passwords = [ "Pass123","SecurePassword1", "weakKKKKKKK","MyP@ssw0rd", "NOLOWER123"]
min_length = 8
compliant = 0
non_compliant = 0

for password in passwords:
    issues = []
    require_upper = True
    require_lower = True
    require_digit = False
    password_valid = True
    if len(password) < min_length:
        issues.append(" Too short")
        password_valid = False
    if require_upper and not any(c.isupper() for c in password):
        issues.append(" No uppercase letters")
        password_valid = False
    if require_lower and not any(c.islower() for c in password):
        issues.append(" No lowercase letters")
        password_valid = False
    for char in password:
        if '0' <= char <= '9':
            require_digit = True
    if not require_digit:
        issues.append(" No digits")
        password_valid = False
    if len(issues) == 0:
        print("PASS: " + password + " - Meets all requirements")
        compliant += 1
    else:
        issue_text = ",".join(issues)
        print("Fail: " + password + " -" + issue_text)
        non_compliant += 1

print("\nSummary: " + str(compliant) + " compliant, " + str(non_compliant) + " non-compliant")
