import os
from pathlib import Path
os.chdir(Path(__file__).parent)

from databaseManager import DatabaseManager

db = DatabaseManager("./resturant.db")


def app():
    db.add_food(("Pizza Fungi",4))

    food_list = db.get_list_foods()

    for food in food_list:
        print(food)


app()
