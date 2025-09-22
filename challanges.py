countdown = 10

while countdown != 0:
    print(countdown)
    countdown = countdown - 1


consent = True
print("Im gonna tickle your feet....")
while consent == True:
    reply = input("Tickle!!!! ").lower
    if reply == "no" or reply == "stop":
        consent == False
