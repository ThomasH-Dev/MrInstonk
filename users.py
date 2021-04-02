import discord
import json


class MyUsers():

    @staticmethod
    def adduser(message):

        f = open("users.json")

        data_dict = json.load(f)

        f.close()

        print(data_dict)

        data_dict["userID"].append(message.author.id)

        print(data_dict)

        with open("users.json", "w") as outfile:
            json.dump(data_dict, outfile)

