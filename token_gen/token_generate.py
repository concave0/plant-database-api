import jwt 

class TokenGenerate: 
  def generate_jwt_token(payload, secret, algorithm='HS256'):
      token = jwt.encode(payload, secret, algorithm=algorithm)
      return token

