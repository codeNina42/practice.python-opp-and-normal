# Base class
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User Name: {self.name}"
class AdminUser(User):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
    def __str__(self):
        return f"Admin Name: {self.name}, Role: {self.role}"
user1 = User("Alice")
user2 = User("Bob")
admin1 = AdminUser("Charlie", "SuperAdmin")
admin2 = AdminUser("David", "Moderator")
all_users = [user1, user2, admin1, admin2]
for u in all_users:
    print(u)
