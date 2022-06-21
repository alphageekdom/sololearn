text = input()

def uppercase_decorator(func):
    def wrapper(text):
        res = func(text)
        modified = res.upper()
        return modified
    return wrapper


@uppercase_decorator
def display_text(text):
    return(text)

print(display_text(text))