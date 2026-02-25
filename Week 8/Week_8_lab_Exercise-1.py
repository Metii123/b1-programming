class User:
    def __init__(self, username, password, privilege='guest'):
        self.__username = username
        self.__hashed_password = self.__hash_password(password)
        self.__privilege = privilege
        self.__login_attempts = 0
        self.__status = 'active'
        self.__activity_log = []

    def __hash_password(self, password):
        return f"hash_{password}"

    def log_activity(self, action):
        self.__activity_log.append(action)
        print(f"[LOG]: {action}")

    def authenticate(self, provided_password):
        if self.__status == 'locked':
            print("Account is locked")
            return False
        
        if self.__hash_password(provided_password) == self.__hashed_password:
            self.reset_login_attempts = 0
            self.log_activity("Login Successful")
            return True
        else:
            self.__login_attempts += 1
            self.log_activity(f"Failed login attempt ({self.__login_attempts}/3)")
            
            if self.__login_attempts >= 3:
                self.lock_account()
            return False
        
    def check_privileges(self, required_level):
        privilege_hierarchy = {'guest': 0, 'standard': 1, 'admin': 2}
        return privilege_hierarchy.get(self.__privilege, 0) >= privilege_hierarchy.get(required_level, 0)
    
    def lock_account(self):
        self.__status = "locked"
        self.log_activity("Account status changed to LOCKED")
    
    def reset_login_attempts(self, admin_password):
        if self.__hash_password(admin_password) == 'hash_admin_secret':
            self.__status = 'active'
            self.__login_attempts = 0
            self.log_activity('Account unlocked by admin.')
            return True
        self.log_activity('Unauthorised reset attempt.')
        return False
    def display_info(self):
        return {
            'username':       self.__username,
            'privilege':      self.__privilege,
            'status':         self.__status,
            'login_attempts': self.__login_attempts,
        }

    def get_activity_log(self):
        return list(self.__activity_log)

    
