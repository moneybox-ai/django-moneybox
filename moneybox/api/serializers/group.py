from rest_framework.serializers import ModelSerializer

from wallet.models.group import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
