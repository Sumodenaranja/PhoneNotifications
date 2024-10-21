from SendMessage import SendMessage
from datetime import datetime
from datetime import date
import json

path = "Phone Notifications/data.json"
messageSender = SendMessage()
number = 0

def readJson(path):
    with open(path) as file:
        data = json.load(file)
        return data

def writeJson(path):
    with open(path, "w") as file:
        json.dump(data, file)
    
def theSender(condition):
    if condition == "n":
        if number  == completedTasks:
            messageSender.send(possibleMessages[2])
        elif number > completedTasks:
            messageSender.send(possibleMessages[3])
        else:
            messageSender.send(possibleMessages[1])
    elif condition == "y":
        messageSender.send(possibleMessages[4])

def mainMenu():
    n = input("Have you completed a task? (y/n)")
    if n == "n":
        theSender("n")
    elif n == "y":
        print("Updated the score")
        data["TasksCompleted"] = str(int(data["TasksCompleted"]) + 1)  # Increment completed tasks
        writeJson(path)
        theSender("y")

data = readJson(path)
 
startDate = data["StartDate"]
startDate = datetime.strptime(startDate, "%Y-%m-%d").date()
completedTasks = int(data["TasksCompleted"])
currentDate = date.today()

number = (currentDate - startDate).days
number = number - (number//7)*2

possibleMessages = {
    1:"You are " + str(completedTasks-number) + " ahead, good job!",
    2:"You are on track, you should still do one more assignment just to be sure!",
    3:"You are " + str(number-completedTasks) + " behind. You should really get to studying",
    4:"Good job completing a task!"
}

mainMenu()