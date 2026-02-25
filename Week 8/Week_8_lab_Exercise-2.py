import datetime

class Device:
    def __init__(self, device_id, device_type, firmware_version, owner):
        self.__device_id          = device_id
        self.__device_type        = device_type
        self.__firmware_version   = firmware_version
        self.__owner              = owner
        self.__compliance_status  = 'compliant'
        self.__last_security_scan = None
        self.__is_active          = True
        self.__activity_log       = []

    def __log(self, action):
        self.__activity_log.append(action)
        print(f"[LOG]: {action}")

    def check_compliance(self, user=None):
        if user and user.get_privilege() == 'admin':
            return True
        if self.__last_security_scan is None or \
           (datetime.datetime.now() - self.__last_security_scan).days > 30:
            self.__compliance_status = 'non-compliant'
            self.__log("Compliance FAILED - scan overdue.")
            return False
        return True

    def authorise_access(self, user):
        if not self.__is_active:
            self.__log("Access denied - device quarantined.")
            return False
        if user.get_username() != self.__owner and user.get_privilege() != 'admin':
            self.__log(f"Access denied for '{user.get_username()}' - not owner or admin.")
            return False
        if not self.check_compliance(user):
            self.__log(f"Access denied for '{user.get_username()}' - non-compliant.")
            return False
        self.__log(f"Access authorised for '{user.get_username()}'.")
        return True

    def run_security_scan(self, user):
        if not self.authorise_access(user): return False
        self.__last_security_scan = datetime.datetime.now()
        self.__compliance_status  = 'compliant'
        self.__log(f"Security scan completed by '{user.get_username()}'.")
        return True

    def update_firmware(self, new_version, user):
        if not self.authorise_access(user): return False
        self.__firmware_version = new_version
        self.__log(f"Firmware updated to '{new_version}' by '{user.get_username()}'.")
        return True

    def quarantine(self, user):
        if user.get_privilege() != 'admin':
            self.__log(f"Quarantine denied - '{user.get_username()}' is not an admin.")
            return False
        self.__is_active = False
        self.__compliance_status = 'non-compliant'
        self.__log(f"Device QUARANTINED by '{user.get_username()}'.")
        return True

    def display_info(self):
        return {'device_id': self.__device_id, 'type': self.__device_type,
                'firmware': self.__firmware_version, 'owner': self.__owner,
                'compliance': self.__compliance_status, 'active': self.__is_active}

    def get_device_id(self):  return self.__device_id
    def get_activity_log(self): return list(self.__activity_log)


class User:
    def __init__(self, username, privilege='guest'):
        self.__username  = username
        self.__privilege = privilege
    def get_username(self):  return self.__username
    def get_privilege(self): return self.__privilege


class DeviceManager:
    def __init__(self):
        self.__devices = {}

    def add_device(self, device, user):
        if user.get_privilege() != 'admin': return False
        self.__devices[device.get_device_id()] = device
        print(f"[LOG]: '{device.get_device_id()}' added by '{user.get_username()}'.")
        return True

    def remove_device(self, device_id, user):
        if user.get_privilege() != 'admin' or device_id not in self.__devices: return False
        del self.__devices[device_id]
        print(f"[LOG]: '{device_id}' removed by '{user.get_username()}'.")
        return True

    def generate_security_report(self, user):
        if user.get_privilege() != 'admin': return None
        return [d.display_info() for d in self.__devices.values()]
