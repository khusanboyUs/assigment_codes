#decorators

user={'username':'Dawid','role':'user'}


def my_decorator(role):
    def check_access(func):
        def wrapper(platform):
            if user['role'] == role:
                return func(platform)
            else:
                return 'Access Denied!'
        return wrapper
    return check_access

@my_decorator('superuser')
def my_permission(platform):
    return f'Access Granted for {platform}'   

print(my_permission('Google Meets'))