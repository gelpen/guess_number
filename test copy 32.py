def obfuscator(func):
    def wrapper():
        data = func()
        if 'name' in data:
            name = data['name']
            obfuscated_name = name[0] + '*' * (len(name) - 2) + name[-1]
            data['name'] = obfuscated_name

        if 'password' in data:
            password = data['password']
            obfuscated_password = '*' * len(password)
            data['password'] = obfuscated_password

        return data

    return wrapper

# Пример использования
@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }

print(get_credentials())
