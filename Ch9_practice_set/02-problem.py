import random
def gamefunc():
    print("you are playing a game....")
    score=random.randint(1,62)
 # fetch the highscore
    with open("hiscore.txt","r") as f:
     hiscore=f.read()
     if(hiscore!=""):
        hiscore=int(hiscore)
     else:
        hiscore=0
    print(f"you score is: {score}")
    if(score>hiscore):
      #  write this hiscore to the file
     with open("hiscore.txt","w") as f:
        f.write(str(score))

gamefunc()