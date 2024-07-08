from rest_framework import serializers
from firebase_admin import auth, firestore

class UserSerializer(serializers.Serializer):
    uid = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=False, required=True)
    name = serializers.CharField()
    image = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        # Crear el usuario en Firebase Authentication
        user = auth.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Guardar el UID y otros datos en Firestore
        db = firestore.client()
        users_ref = db.collection('users')
        new_user_ref = users_ref.document(user.uid)
        new_user_ref.set({
            'uid': user.uid,
            'email': validated_data['email'],
            'password': validated_data['password'],  # Guardar la contraseña también en Firestore
            'name': validated_data['name'],
            'image': validated_data.get('image', '')
        })

        # Devolver los datos del usuario con el UID asignado
        validated_data['uid'] = user.uid
        return validated_data

    def update(self, instance, validated_data):
        db = firestore.client()
        user_ref = db.collection('users').document(instance['uid'])
        user_ref.update(validated_data)
        return validated_data

    def partial_update(self, instance, validated_data):
        db = firestore.client()
        user_ref = db.collection('users').document(instance['uid'])
        user_ref.update(validated_data)
        return validated_data

    def to_representation(self, instance):
        representation = {
            'uid': instance.get('uid', ''),
            'email': instance.get('email', ''),
            'password': instance.get('password', ''),  
            'name': instance.get('name', ''),
            'image': instance.get('image', ''),
        }
        return representation
