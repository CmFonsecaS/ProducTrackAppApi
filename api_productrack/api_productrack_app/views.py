from rest_framework import viewsets, status
from rest_framework.response import Response
from firebase_admin import firestore
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request):
        db = firestore.client()
        users_ref = db.collection('users')
        users = [doc.to_dict() for doc in users_ref.stream()]

        # Asegurar que uid esté presente en los datos del usuario
        for user in users:
            user['uid'] = user.get('uid', '')

        serialized_users = [self.serializer_class(user_data).data for user_data in users]
        return Response(serialized_users)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return Response(user_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        db = firestore.client()
        user_ref = db.collection('users').document(pk)
        user = user_ref.get()
        if user.exists:
            user_data = user.to_dict()
            user_data['uid'] = user.id  # Asegurarse de incluir el UID
            serialized_user = self.serializer_class(user_data).data
            return Response(serialized_user)
        else:
            return Response({'detail': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        db = firestore.client()
        user_ref = db.collection('users').document(pk)
        user_ref.update(serializer.validated_data)
        return Response({'detail': 'Usuario actualizado con éxito'})

    def partial_update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        db = firestore.client()
        user_ref = db.collection('users').document(pk)
        user_ref.update(serializer.validated_data)
        return Response({'detail': 'Usuario actualizado parcialmente con éxito'})

    def destroy(self, request, pk=None):
        db = firestore.client()
        user_ref = db.collection('users').document(pk)
        user_ref.delete()
        return Response({'detail': 'Usuario eliminado con éxito'}, status=status.HTTP_204_NO_CONTENT)
