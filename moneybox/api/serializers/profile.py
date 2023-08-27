from rest_framework.serializers import ModelSerializer

from users.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
