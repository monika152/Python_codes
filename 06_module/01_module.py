from greetings import*
# Caller - App -Consumer
print("welcome in Restaurant Acasa")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("please choose your language:")
print("[1] DE")
print("[2] EN")
print("[3] SP")
print("[4] CN")
user_lang = int(input(">"))
print()


if user_lang == 1: # DE
    greeting_de()
elif user_lang == 2: # EN
    greeting_en()
elif user_lang == 3: # SP
    greeting_sp()
elif user_lang == 4: # CN
    greeting_cn()
else:
    print("The language is not avaible . we will continue in ENGLISH")
    greeting_en()