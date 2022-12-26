import os
import openai
from Cred import tokens 
# value for env variable
key = tokens.TOKEN_OPENAI
# openai.api_key_path = os.get
print(key)