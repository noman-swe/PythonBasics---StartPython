# Almost any value is evaluated to True if it has some sort of content.
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool("Noman"))
print(bool(130))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# all these returns True Value
# in Boolean almost any value is evaluated to True if it has some sort of content.


# but Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Functions can Return a Boolean
def myFunction():
    return True


print(myFunction())
