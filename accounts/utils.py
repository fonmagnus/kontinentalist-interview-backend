import jwt

# we don't need to decode the same token multiple times
jwt_decode_cache = {}


def get_user_id_by_request(request):
    access_token = request.headers.get('Authorization').split(" ")[1]
    if not access_token in jwt_decode_cache.keys():
        jwt_decode_cache[access_token] = jwt.decode(
            access_token, verify=False).get("user_id")
    return jwt_decode_cache[access_token]
