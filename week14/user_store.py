import json

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, "r") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except FileNotFoundError:
            return []

    def save(self, users):
        with open(self.file_path, "w") as f:
            json.dump(users, f)

    def find_by_id(self, user_id):
        users = self.load()
        for u in users:
            if u["id"] == user_id:
                return u
        return None

    def update_user(self, user_id, updated_data):
        users = self.load()
        for i, u in enumerate(users):
            if u["id"] == user_id:
                users[i] = {"id": user_id, **updated_data}
                self.save(users)
                return users[i]
        return None

    def delete_user(self, user_id):
        users = self.load()
        for i, u in enumerate(users):
            if u["id"] == user_id:
                users.pop(i)
                self.save(users)
                return True
        return False