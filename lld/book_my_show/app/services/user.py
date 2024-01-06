from models.user import User


class UserService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create(self):
        user = User.objects.create(username=self.username, password=self.password)
        user.save()

    def get_user_by_id(self, user_id):
        user = self.User.objects.get(id=user_id)
