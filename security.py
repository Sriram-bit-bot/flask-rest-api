from models.user import UserModel

# users =[
#     User(1,'bob','1234')
# ]

# username_mapping ={u.username: u for u in users}
# userid_mapping ={u.id: u for u in users}

# username_mapping ={
#     'bob':{
#             'id':1,
#             'Username':'bob',
#             'password':'1234'        
#         }      
# }

# userid_mapping ={
#     1:{
#         'id':1,
#         'Username':'bob',
#         'password':'1234'         
#     }
# }
# We are creating these mappings so as to aviod looping through the lists again and again

def authenticate(username, password):
    user =UserModel.find_by_username(username)
# Gives None if the username is not present. This cannot be done using square brackets
    if user and user.password == password:
        return user

def identity(payload):
#Identity function is unique to flask-JWT, it takes in a payload and payload is the contents of the JWT token
    user_id =payload['identity']
    return UserModel.find_by_id(user_id)