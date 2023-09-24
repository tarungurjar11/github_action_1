import os

def check():
    print("hello")
    for key, value in os.environ.items():
        print(key + " = " + value)