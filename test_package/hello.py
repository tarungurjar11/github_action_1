import os

def envv():
    for key, value in os.environ.items():
        print(key, " = ", value)