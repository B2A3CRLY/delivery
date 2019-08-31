from kumba_api.users.serializers import UserSerializer


def my_jwt_response_handler(token, user=None, request=None):
    print("toekn ", token)
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
