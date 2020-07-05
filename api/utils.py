from rest_framework.serializers import ModelSerializer
from api.models import Ong, NeedProduct, NeedBill, Tag

class OngModelSerializer(ModelSerializer):
	class Meta:
		model = Ong
		fields = ['id', 'name', 'cnpj', 'description', 'cep', 'state', 'city', 'address', 'number', 'complement', 'link', 'date_register']

	def create(self, validated_data):
		instance = self.Meta.model(**validated_data)
		instance.save()

		return instance

class NeedProductModelSerializer(ModelSerializer):
	class Meta:
		model = NeedProduct
		fields = ['id', 'name', 'amount', 'description', 'tags', 'ong','date_register']

	def create(self, validated_data):
		instance = self.Meta.model(**validated_data)
		instance.save()

		return instance

class NeedBillModelSerializer(ModelSerializer):
	class Meta:
		model = NeedBill
		fields = ['id', 'name', 'expiration', 'amount', 'description', 'tags', 'ong','date_register']

	def create(self, validated_data):
		instance = self.Meta.model(**validated_data)
		instance.save()

		return instance

class TagModelSerializer(ModelSerializer):
	class Meta:
		model = Tag
		fields = ['id', 'name']

	def create(self, validated_data):
		instance = self.Meta.model(**validated_data)
		instance.save()

		return instance