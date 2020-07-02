from rest_framework.serializers import ModelSerializer

def serializer(self, *args):
	class GeneralSerializer(ModelSerializer):
		class Meta:
			model = type(self)
			fields = args or '_all_'

	return GeneralSerializer(self).data

models.Model.serializer = serializer