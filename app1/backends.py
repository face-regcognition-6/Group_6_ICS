from django.contrib.auth.backends import ModelBackend
from .models import User

class MyCustomBackend(ModelBackend):
    def get_user(self, user_id):
        # 确保从会话获取的 user_id 是字符串类型，避免转换错误
        if isinstance(user_id, str):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None
        return None
