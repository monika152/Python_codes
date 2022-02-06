from greeting import*


def app():
    print("This is my app")
    greeting_1("Thomas")
    greeting_2("Thomas")
    greeting_3("Thomas")


    # print(__file__) # Absolute Path of current Python file
    # print(__name__) # the first runned python file

if __name__ == "__main__":  # True
    app()