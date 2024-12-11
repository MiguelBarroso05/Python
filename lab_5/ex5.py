users = [
    {"username": "admin", "password": "admin123"},
    {"username": "admin", "password": "admin123"},
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "guest", "password": "guest123"},
]
username_client = input("Enter your username: ")
password_client = input("Enter your password: ")

if any(user["username"] == username_client and user["password"] == password_client for user in users):
    print("Welcome back!")
else:
    print("Credentials invalids.")

"""
Como pode guardar os utilizadores de forma segura, evitando o uso direto de palavras-passe em
texto simples?


Para guardar as palavras-passe de forma segura, deve-se usar técnicas de hashing, como bcrypt ou Argon2, 
em vez de armazená-las em texto simples. Isso garante que mesmo que a base de dados seja comprometida, 
as palavras-passe não sejam acessíveis.

Como poderia melhorar este sistema de login para suportar funcionalidades como a recuperação de
senha ou múltiplas tentativas?

Para melhorar o sistema de login, pode-se implementar um limite de tentativas falhadas para prevenir 
ataques de força bruta, e permitir a recuperação de senha através de um link enviado ao e-mail do 
utilizador, onde o utilizador pode redefinir a senha.
"""