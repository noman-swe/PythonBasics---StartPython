def greetHello():
    print("Hello")


def greetings(name, greetingsPeriod):
    #  print("Hello " + name)
    print("Good " + greetingsPeriod + " " + name)


print("Practicing Function")  # this is printing before the greetings function because of the function has called later
greetings("Noman", "Morning")
greetings("Shanto", "Evening")
greetings("Shbily", "Night")


#  Letter Generator demo
def letterGenerator(name, date):
    letterDescrip = f"Hi Mam. \n I'm {name}. i am sick that's why i can't come to school on {date}"
    print(letterDescrip)


letterGenerator("Shakil", "11-Nov-2023")

'''Return type Function Practice'''


def average(a, b):
    return (a + b) / 2


print(average(21, 54))
