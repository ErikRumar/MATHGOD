from Graphics import*
import time
import random

global count
global name
global gameon
global gametime
global menu
global t1
global lvl

gametime = 60


for win in range(1):
    win = GraphWin("win", 1000, 800)

    win.setCoords(0, 0, 1000, 800)
    win.setBackground("black")
    background = Image(Point(500, 400), "C:/Users/erik.rumarvaleskog/Pictures/epictunnel.gif")
    background.draw(win)
    
    descriptiontx = 500
    descriptionty = 100
    descriptiontext = Text(Point(descriptiontx, descriptionty), f"""        MATHGOD is a game where you have
one minute to solve as many math problems as possible within one minute.
        There are 6 different levels to play under 'Levels'.
    """)
    descriptiontext.setFill("white")
    descriptiontext.setStyle("bold")
    descriptiontext.setSize(16)


def start():
    global name

    namebx = 500
    nameby = 500
    namebox = Entry(Point(namebx, nameby), 10)
    namebox.setFill("white")
    namebox.setStyle("bold")
    namebox.setSize(35)

    nametx = 500
    namety = 650
    nametext = Text(Point(nametx, namety), "Choose Nickname:")
    nametext.setFill("white")
    nametext.setStyle("bold")
    nametext.setSize(36)

    namet2x = 500
    namet2y = 575
    nametext2 = Text(Point(namet2x, namet2y), "(max 20)")
    nametext2.setFill("white")
    nametext2.setStyle("bold")
    nametext2.setSize(16)

    nametext.draw(win)
    nametext2.draw(win)
    namebox.draw(win)
    descriptiontext.draw(win)

    keystring = ""

    while keystring != "Return" or len(namebox.getText()) > 20:
        keystring = win.getKey()
        if keystring == "slash":
            namebox.setText(previous_text)
            continue
        if len(namebox.getText()) > 20:
            namebox.setText(previous_text)
            continue
        if(keystring == "Return") and len(namebox.getText()) <= 20:
            name = namebox.getText()
        else:
            keystring = ""
        previous_text = namebox.getText()
    nametext.undraw()
    nametext2.undraw()
    namebox.undraw()

start()

def check_int(string):
    if string == "":
        whatis = False
        return whatis
    for x in string:
        if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
            continue
        else:
            whatis = False
            return whatis
    whatis = True
    return whatis

def countdown():
    global count
    
    countx = 500
    county = 650

    count1 = Text(Point(countx, county), "3")
    count1.setFill("white")
    count1.setStyle("bold")
    count1.setSize(35)

    count1.draw(win)
    time.sleep(0.6)

    time.sleep(0.6)
    count1.undraw()

    count2 = Text(Point(countx, county), "2")
    count2.setFill("white")
    count2.setStyle("bold")
    count2.setSize(35)
    
    count2.draw(win)
    time.sleep(0.6)

    time.sleep(0.6)
    count2.undraw()    

    count3 = Text(Point(countx, county), "1")
    count3.setFill("white")
    count3.setStyle("bold")
    count3.setSize(35)
    
    count3.draw(win)
    time.sleep(0.6)

    time.sleep(0.6)
    count3.undraw()

    return

def times(timelength):
    global gameon
    global t1
    t2 = float("{0:.2f}".format((time.time() - t1)))
    if t2 >= timelength:
        gameon = False
    timerx = 50
    timery = 800
    timer = Text(Point(timerx, timery), f"Time: {t2}")
    timer.setFill("white")
    timer.setStyle("bold")
    timer.setSize(35)
    timer.undraw()
    timer.draw(win)

def savescore(name, score):
    global lvl
    score = int(score)
    names = []
    scores = []
    place = -1

    if lvl == 1:

        with open("scoreboard1.txt", "r", encoding= "utf8") as list:
            newlist = []
            
            done = False
            
            for x in list.readlines():
                place +=1
                sc = ""
                nm = ""
                nm, sc = x.split("/")
                sc = int(sc)
                if sc <= score and done == False:
                    newlist.append(f"{name}/{score}")
                    names.append(name)
                    scores.append(score)
                    index = int(place)
                    done = True

                newlist.append(f"{nm}/{sc}")
                names.append(nm)
                scores.append(sc)
            if done == False:
                newlist.append(f"{name}/{score}")
                names.append(name)
                scores.append(score)
                index = int(place)
                done = True

        with open("scoreboard1.txt", "w", encoding= "utf8") as list:
            list.truncate()
            for y in newlist:
                list.write(f"{y}\n")
        return index
    
    if lvl == 2:
        with open("scoreboard2.txt", "r", encoding= "utf8") as list:
            newlist = []
            
            done = False
            
            for x in list.readlines():
                place +=1
                sc = ""
                nm = ""
                nm, sc = x.split("/")
                sc = int(sc)
                if sc <= score and done == False:
                    newlist.append(f"{name}/{score}")
                    names.append(name)
                    scores.append(score)
                    index = int(place)
                    done = True

                newlist.append(f"{nm}/{sc}")
                names.append(nm)
                scores.append(sc)
            if done == False:
                newlist.append(f"{name}/{score}")
                names.append(name)
                scores.append(score)
                index = int(place)
                done = True

        with open("scoreboard2.txt", "w", encoding= "utf8") as list:
            list.truncate()
            for y in newlist:
                list.write(f"{y}\n")
        return index
    
    if lvl == 3:
        with open("scoreboard3.txt", "r", encoding= "utf8") as list:
            newlist = []
            
            done = False
            
            for x in list.readlines():
                place +=1
                sc = ""
                nm = ""
                nm, sc = x.split("/")
                sc = int(sc)
                if sc <= score and done == False:
                    newlist.append(f"{name}/{score}")
                    names.append(name)
                    scores.append(score)
                    index = int(place)
                    done = True

                newlist.append(f"{nm}/{sc}")
                names.append(nm)
                scores.append(sc)
            if done == False:
                newlist.append(f"{name}/{score}")
                names.append(name)
                scores.append(score)
                index = int(place)
                done = True

        with open("scoreboard3.txt", "w", encoding= "utf8") as list:
            list.truncate()
            for y in newlist:
                list.write(f"{y}\n")
        return index
    
    if lvl == 4:
        with open("scoreboard4.txt", "r", encoding= "utf8") as list:
            newlist = []
            
            done = False
            
            for x in list.readlines():
                place +=1
                sc = ""
                nm = ""
                nm, sc = x.split("/")
                sc = int(sc)
                if sc <= score and done == False:
                    newlist.append(f"{name}/{score}")
                    names.append(name)
                    scores.append(score)
                    index = int(place)
                    done = True

                newlist.append(f"{nm}/{sc}")
                names.append(nm)
                scores.append(sc)
            if done == False:
                newlist.append(f"{name}/{score}")
                names.append(name)
                scores.append(score)
                index = int(place)
                done = True

        with open("scoreboard4.txt", "w", encoding= "utf8") as list:
            list.truncate()
            for y in newlist:
                list.write(f"{y}\n")
        return index
    
    if lvl == 5:
        with open("scoreboard5.txt", "r", encoding= "utf8") as list:
            newlist = []
            
            done = False
            
            for x in list.readlines():
                place +=1
                sc = ""
                nm = ""
                nm, sc = x.split("/")
                sc = int(sc)
                if sc <= score and done == False:
                    newlist.append(f"{name}/{score}")
                    names.append(name)
                    scores.append(score)
                    index = int(place)
                    done = True

                newlist.append(f"{nm}/{sc}")
                names.append(nm)
                scores.append(sc)
            if done == False:
                newlist.append(f"{name}/{score}")
                names.append(name)
                scores.append(score)
                index = int(place)
                done = True

        with open("scoreboard5.txt", "w", encoding= "utf8") as list:
            list.truncate()
            for y in newlist:
                list.write(f"{y}\n")
        return index

    
    if lvl == 6:
        with open("scoreboard6.txt", "r", encoding= "utf8") as list:
            newlist = []
            
            done = False
            
            for x in list.readlines():
                place +=1
                sc = ""
                nm = ""
                nm, sc = x.split("/")
                sc = int(sc)
                if sc <= score and done == False:
                    newlist.append(f"{name}/{score}")
                    names.append(name)
                    scores.append(score)
                    index = int(place)
                    done = True

                newlist.append(f"{nm}/{sc}")
                names.append(nm)
                scores.append(sc)
            if done == False:
                newlist.append(f"{name}/{score}")
                names.append(name)
                scores.append(score)
                index = int(place)
                done = True

        with open("scoreboard6.txt", "w", encoding= "utf8") as list:
            list.truncate()
            for y in newlist:
                list.write(f"{y}\n")
        return index


def end_of_game(name, score, index):
    global menu
    global lvl

    if lvl == 1:
        with open("scoreboard1.txt", "r", encoding= "utf8") as file:
            names = []
            points = []
            add = ""
            for x in file.readlines():
                nm = False
                sc = False
                for y in x:
                    if y == "/" and nm == False:
                        names.append(add)
                        add = ""
                        nm = True
                        continue
                    elif y == "\n":
                        points.append(int(add))
                        add = ""
                        continue
                    add += y
    
    if lvl == 2:
        with open("scoreboard2.txt", "r", encoding= "utf8") as file:
            names = []
            points = []
            add = ""
            for x in file.readlines():
                nm = False
                sc = False
                for y in x:
                    if y == "/" and nm == False:
                        names.append(add)
                        add = ""
                        nm = True
                        continue
                    elif y == "\n":
                        points.append(int(add))
                        add = ""
                        continue
                    add += y
    
    if lvl == 3:
        with open("scoreboard3.txt", "r", encoding= "utf8") as file:
            names = []
            points = []
            add = ""
            for x in file.readlines():
                nm = False
                sc = False
                for y in x:
                    if y == "/" and nm == False:
                        names.append(add)
                        add = ""
                        nm = True
                        continue
                    elif y == "\n":
                        points.append(int(add))
                        add = ""
                        continue
                    add += y
    
    if lvl == 4:
        with open("scoreboard4.txt", "r", encoding= "utf8") as file:
            names = []
            points = []
            add = ""
            for x in file.readlines():
                nm = False
                sc = False
                for y in x:
                    if y == "/" and nm == False:
                        names.append(add)
                        add = ""
                        nm = True
                        continue
                    elif y == "\n":
                        points.append(int(add))
                        add = ""
                        continue
                    add += y
    
    if lvl == 5:
        with open("scoreboard5.txt", "r", encoding= "utf8") as file:
            names = []
            points = []
            add = ""
            for x in file.readlines():
                nm = False
                sc = False
                for y in x:
                    if y == "/" and nm == False:
                        names.append(add)
                        add = ""
                        nm = True
                        continue
                    elif y == "\n":
                        points.append(int(add))
                        add = ""
                        continue
                    add += y

    if lvl == 6:
        with open("scoreboard6.txt", "r", encoding= "utf8") as file:
            names = []
            points = []
            add = ""
            for x in file.readlines():
                nm = False
                sc = False
                for y in x:
                    if y == "/" and nm == False:
                        names.append(add)
                        add = ""
                        nm = True
                        continue
                    elif y == "\n":
                        points.append(int(add))
                        add = ""
                        continue
                    add += y

    surpass_percentage = (1- float(index / len(names))) * 100
    surpass_percentage = "{:.2f}".format(surpass_percentage)

    nametextx = int(300)
    nametexty = int(450)
    scoretextx = int(700)
    scoretexty = int(550)
    if index < 10:
        scoretext = Text(Point(scoretextx, scoretexty), f"""


{points[0]}
{points[1]}
{points[2]}
{points[3]}
{points[4]}
{points[5]}
{points[6]}
{points[7]}
{points[8]}
{points[9]}
        """)
        scoretext.setTextColor("white")
        scoretext.setSize(28)
        scoretext.setStyle("bold")

        nametext = Text(Point(nametextx, nametexty+80), f"""

                                    Scoreboard  lvl {lvl}
{names[0]}
{names[1]}
{names[2]}
{names[3]}
{names[4]}
{names[5]}
{names[6]}
{names[7]}
{names[8]}
{names[9]}

        """)
        nametext.setTextColor("white")
        nametext.setSize(28)
        nametext.setStyle("bold")
    
    else:
        
        scoretext = Text(Point(scoretextx, scoretexty-80), f"""


{points[0]}
{points[1]}
{points[2]}
{points[3]}
{points[4]}
{points[5]}
{points[6]}
{points[7]}
{points[8]}
{points[9]}

{points[index-1]}
{score}
{points[index+1]}
        """)
        scoretext.setTextColor("white")
        scoretext.setSize(28)
        scoretext.setStyle("bold")

        nametext = Text(Point(nametextx, nametexty), f"""

                                    Scoreboard  lvl {lvl}
{names[0]}
{names[1]}
{names[2]}
{names[3]}
{names[4]}
{names[5]}
{names[6]}
{names[7]}
{names[8]}
{names[9]}
        ____________________________________________
{names[index-1]}
{name}
{names[index+1]}

        """)
        nametext.setTextColor("white")
        nametext.setSize(28)
        nametext.setStyle("bold")
    
    for _ in range(1):
        returnerx1 = int(400)
        returnerx2 = int(600)
        returnery1 = int(30)
        returnery2 = int(100)
        returner = Rectangle(Point(returnerx1, returnery1), Point(returnerx2, returnery2))
        returner.setFill("white")

        returnertextx = (returnerx1+returnerx2)//2
        returnertexty = (returnery1+returnery2)//2
        returnertext = Text(Point(returnertextx, returnertexty), "Return to Menu")
        returnertext.setFill("black")
        returnertext.setStyle("bold")
        returnertext.setSize(18)

        surpasstextx = 400
        surpasstexty = 200
        surpasstext = Text(Point(surpasstextx, surpasstexty), f"                    You surpassed {surpass_percentage} % of players")
        surpasstext.setFill("white")
        surpasstext.setStyle("bold")
        surpasstext.setSize(23)


    scoretext.draw(win)
    nametext.draw(win)
    returner.draw(win)
    returnertext.draw(win)
    surpasstext.draw(win)
    done = False

    c = win.getMouse()

    cx = c.getX()
    cy = c.getY()
    while done == False:
        if returnerx1 < cx < returnerx2 and returnery1< cy < returnery2:
            done = True
            menu = 0
            scoretext.undraw()
            nametext.undraw()
            returner.undraw()
            returnertext.undraw()
            surpasstext.undraw()
            return


def lvl1():
    global menu
    global t1
    global gametime
    global gameon

    keystring = ""
    gameon = True
    term = 7
    termdif = 5
    rounds = 1
    ans = False
    points = 0
    add = 1
    t1 = float(time.time())

    while gameon:

        term1 = random.randint((term-termdif) +rounds, term +rounds +termdif)
        term2 = random.randint((term-termdif) +rounds, term +rounds +termdif)
        sign = "+"

        for _ in range(1):
            leftx = termbegin
            lefty = termy
            left = Text(Point(leftx, lefty), f"{term1}")
            left.setFill("white")
            left.setStyle("bold")
            left.setSize(35)

            signx = termbegin + termspace
            signy = termy
            sign = Text(Point(signx, signy), f"{sign}")
            sign.setFill("white")
            sign.setStyle("bold")
            sign.setSize(35)

            rightx = signx + termspace
            righty = termy
            right = Text(Point(rightx, righty), f"{term2}")
            right.setFill("white")
            right.setStyle("bold")
            right.setSize(35)

            equalx = rightx + termspace
            equaly = termy
            equal = Text(Point(equalx, equaly), f"=")
            equal.setFill("white")
            equal.setStyle("bold")
            equal.setSize(35)

            pointx = 150
            pointy = 750
            point = Text(Point(pointx, pointy), f"Score: {points}")
            point.setFill("white")
            point.setStyle("bold")
            point.setSize(35)

            

            answerbx = 500
            answerby = 500
            answerbox = Entry(Point(answerbx, answerby), 10)
            answerbox.setFill("white")
            answerbox.setStyle("bold")
            answerbox.setSize(35)


        game_time_display.draw(win)
        
        left.draw(win)
        sign.draw(win)
        right.draw(win)
        equal.draw(win)
        answerbox.draw(win)
        point.draw(win)

        keystring = ""
        ans = False

        while ans == False:
            
            keystring = ""
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                left.undraw()
                sign.undraw()
                right.undraw()
                equal.undraw()
                answerbox.undraw()
                point.undraw()
                game_time_display.undraw()
                if (points - rounds) <= 0:
                    return 0
                return points - rounds
            
            while keystring != "Return":

                keystring = win.getKey()
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                if(keystring == "Return"):
                    if check_int(answerbox.getText()) == True:
                        answer = int(answerbox.getText())
                        if answer == term1 + term2:
                            ans = True
                        
                        else:
                            ans = False
                            keystring = ""
                    answerbox.setText("")
        points += rounds
        rounds += add
        add += 1
        termdif += 2
        answerbox.setText("")

        left.undraw()
        sign.undraw()
        right.undraw()
        equal.undraw()
        answerbox.undraw()
        point.undraw()
        game_time_display.undraw()
        if float(time.time()) - t1 >= gametime:
            gameon = False
            menu = 0
            if (points - rounds) <= 0:
                return 0
            return points - rounds

def lvl2():
    global menu
    global t1
    global gametime
    global gameon

    keystring = ""
    gameon = True
    term = 7
    termdif = 5
    rounds = 1
    ans = False
    points = 0
    add = 1
    t1 = float(time.time())

    while gameon:

        term2 = random.randint((term-termdif) +rounds, term +rounds)
        term1 = random.randint((term) +rounds, term +rounds +termdif)
        sign = "-"

        for _ in range(1):
            leftx = termbegin
            lefty = termy
            left = Text(Point(leftx, lefty), f"{term1}")
            left.setFill("white")
            left.setStyle("bold")
            left.setSize(35)

            signx = termbegin + termspace
            signy = termy
            sign = Text(Point(signx, signy), f"{sign}")
            sign.setFill("white")
            sign.setStyle("bold")
            sign.setSize(35)

            rightx = signx + termspace
            righty = termy
            right = Text(Point(rightx, righty), f"{term2}")
            right.setFill("white")
            right.setStyle("bold")
            right.setSize(35)

            equalx = rightx + termspace
            equaly = termy
            equal = Text(Point(equalx, equaly), f"=")
            equal.setFill("white")
            equal.setStyle("bold")
            equal.setSize(35)

            pointx = 150
            pointy = 750
            point = Text(Point(pointx, pointy), f"Score: {points}")
            point.setFill("white")
            point.setStyle("bold")
            point.setSize(35)

            

            answerbx = 500
            answerby = 500
            answerbox = Entry(Point(answerbx, answerby), 10)
            answerbox.setFill("white")
            answerbox.setStyle("bold")
            answerbox.setSize(35)

        game_time_display.draw(win)
        left.draw(win)
        sign.draw(win)
        right.draw(win)
        equal.draw(win)
        answerbox.draw(win)
        point.draw(win)

        keystring = ""
        ans = False

        while ans == False:
            
            keystring = ""
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                left.undraw()
                sign.undraw()
                right.undraw()
                equal.undraw()
                answerbox.undraw()
                point.undraw()
                game_time_display.undraw()
                if (points - rounds) <= 0:
                    return 0
                return points - rounds
            
            while keystring != "Return":

                keystring = win.getKey()
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                if(keystring == "Return"):
                    if check_int(answerbox.getText()) == True:
                        answer = int(answerbox.getText())
                        if answer == term1 - term2:
                            ans = True
                        
                        else:
                            ans = False
                            keystring = ""
                    answerbox.setText("")
        points += rounds
        rounds += add
        add += 1
        termdif += 2
        answerbox.setText("")

        left.undraw()
        sign.undraw()
        right.undraw()
        equal.undraw()
        answerbox.undraw()
        point.undraw()
        game_time_display.undraw()
        if float(time.time()) - t1 >= gametime:
            gameon = False
            menu = 0
            if (points - rounds) <= 0:
                return 0
            return points - rounds

def lvl3():
    global menu
    global t1
    global gametime
    global gameon

    keystring = ""
    gameon = True
    term = 7
    termdif = 2
    rounds = 1
    ans = False
    points = 0
    add = 1
    t1 = float(time.time())


    while gameon:

        term2 = random.randint((term) -5, term +add//2)
        term1 = term2*(random.randint(2, (term+add)))
        sign = "/"

        for _ in range(1):
            leftx = termbegin
            lefty = termy
            left = Text(Point(leftx, lefty), f"{term1}")
            left.setFill("white")
            left.setStyle("bold")
            left.setSize(35)

            signx = termbegin + termspace
            signy = termy
            sign = Text(Point(signx, signy), f"{sign}")
            sign.setFill("white")
            sign.setStyle("bold")
            sign.setSize(35)

            rightx = signx + termspace
            righty = termy
            right = Text(Point(rightx, righty), f"{term2}")
            right.setFill("white")
            right.setStyle("bold")
            right.setSize(35)

            equalx = rightx + termspace
            equaly = termy
            equal = Text(Point(equalx, equaly), f"=")
            equal.setFill("white")
            equal.setStyle("bold")
            equal.setSize(35)

            pointx = 150
            pointy = 750
            point = Text(Point(pointx, pointy), f"Score: {points}")
            point.setFill("white")
            point.setStyle("bold")
            point.setSize(35)

            

            answerbx = 500
            answerby = 500
            answerbox = Entry(Point(answerbx, answerby), 10)
            answerbox.setFill("white")
            answerbox.setStyle("bold")
            answerbox.setSize(35)

        game_time_display.draw(win)
        left.draw(win)
        sign.draw(win)
        right.draw(win)
        equal.draw(win)
        answerbox.draw(win)
        point.draw(win)

        keystring = ""
        ans = False

        while ans == False:
            
            keystring = ""
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                left.undraw()
                sign.undraw()
                right.undraw()
                equal.undraw()
                answerbox.undraw()
                point.undraw()
                game_time_display.undraw()
                if (points - rounds) <= 0:
                    return 0
                return points - rounds
            
            while keystring != "Return":

                keystring = win.getKey()
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                if(keystring == "Return"):
                    if check_int(answerbox.getText()) == True:
                        answer = int(answerbox.getText())
                        if answer == term1/term2:
                            ans = True
                        
                        else:
                            ans = False
                            keystring = ""
                    answerbox.setText("")
        points += rounds
        rounds += add
        add += 1
        termdif += 1
        answerbox.setText("")

        left.undraw()
        sign.undraw()
        right.undraw()
        equal.undraw()
        answerbox.undraw()
        point.undraw()
        game_time_display.undraw()
        if float(time.time()) - t1 >= gametime:
            gameon = False
            menu = 0
            if (points - rounds) <= 0:
                return 0
            return points - rounds

def lvl4():
    global menu
    global t1
    global gametime
    global gameon

    keystring = ""
    gameon = True
    term = 5
    termdif = 2
    rounds = 1
    ans = False
    points = 0
    add = 1
    t1 = float(time.time())

    while gameon:

        term2 = random.randint((term) -1, term +add)
        term1 = random.randint((term) -1, term +add)
        sign = "x"

        for _ in range(1):
            leftx = termbegin
            lefty = termy
            left = Text(Point(leftx, lefty), f"{term1}")
            left.setFill("white")
            left.setStyle("bold")
            left.setSize(35)

            signx = termbegin + termspace
            signy = termy
            sign = Text(Point(signx, signy), f"{sign}")
            sign.setFill("white")
            sign.setStyle("bold")
            sign.setSize(35)

            rightx = signx + termspace
            righty = termy
            right = Text(Point(rightx, righty), f"{term2}")
            right.setFill("white")
            right.setStyle("bold")
            right.setSize(35)

            equalx = rightx + termspace
            equaly = termy
            equal = Text(Point(equalx, equaly), f"=")
            equal.setFill("white")
            equal.setStyle("bold")
            equal.setSize(35)

            pointx = 150
            pointy = 750
            point = Text(Point(pointx, pointy), f"Score: {points}")
            point.setFill("white")
            point.setStyle("bold")
            point.setSize(35)

            

            answerbx = 500
            answerby = 500
            answerbox = Entry(Point(answerbx, answerby), 10)
            answerbox.setFill("white")
            answerbox.setStyle("bold")
            answerbox.setSize(35)
        game_time_display.draw(win)
        left.draw(win)
        sign.draw(win)
        right.draw(win)
        equal.draw(win)
        answerbox.draw(win)
        point.draw(win)

        keystring = ""
        ans = False

        while ans == False:
            
            keystring = ""
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                left.undraw()
                sign.undraw()
                right.undraw()
                equal.undraw()
                answerbox.undraw()
                point.undraw()
                game_time_display.undraw()
                if (points - rounds) <= 0:
                    return 0
                return points - rounds
            
            while keystring != "Return":

                keystring = win.getKey()
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                if(keystring == "Return"):
                    if check_int(answerbox.getText()) == True:
                        answer = int(answerbox.getText())
                        if answer == term1 * term2:
                            ans = True
                        
                        else:
                            ans = False
                            keystring = ""
                    answerbox.setText("")
        points += rounds
        rounds += add
        add += 1
        termdif += 1
        answerbox.setText("")

        left.undraw()
        sign.undraw()
        right.undraw()
        equal.undraw()
        answerbox.undraw()
        point.undraw()
        game_time_display.undraw()
        if float(time.time()) - t1 >= gametime:
            gameon = False
            menu = 0
            if (points - rounds) <= 0:
                return 0
            return points - rounds

def lvl5():
    global menu
    global t1
    global gametime
    global gameon

    t1 = float(time.time())
    points = 0
    rounds = 1
    add = 1

    while True:
        operation = random.randint(0, 3)

        if operation == 0:

            keystring = ""
            gameon = True
            term = 7
            termdif = 5
            ans = False

            term1 = random.randint((term-termdif) +rounds, term +rounds +termdif)
            term2 = random.randint((term-termdif) +rounds, term +rounds +termdif)
            sign = "+"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            game_time_display.draw(win)
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if (points - rounds) <= 0:
                            return 0
                        return points - rounds
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1 + term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 2
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if (points - rounds) <= 0:
                    return 0
                return points - rounds

        if operation == 1:
            keystring = ""
            gameon = True
            term = 7
            termdif = 5
            ans = False
            term2 = random.randint((term-termdif) +rounds, term +rounds)
            term1 = random.randint((term) +rounds, term +rounds +termdif)
            sign = "-"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)
            game_time_display.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if (points - rounds) <= 0:
                            return 0
                        return points - rounds
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1 - term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 2
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if (points - rounds) <= 0:
                    return 0
                return points - rounds
        
        if operation == 2:
            keystring = ""
            gameon = True
            term = 7
            termdif = 2
            ans = False
            term2 = random.randint((term) -5, term +add//2)
            term1 = term2*(random.randint(2, (term+add)))
            sign = "/"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)
            game_time_display.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if (points - rounds) <= 0:
                            return 0
                        return points - rounds
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1/term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 1
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if (points - rounds) <= 0:
                    return 0
                return points - rounds

        if operation == 3:
            keystring = ""
            gameon = True
            term = 5
            termdif = 2
            ans = False
            term2 = random.randint((term) -1, term +add)
            term1 = random.randint((term) -1, term +add)
            sign = "x"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)
            game_time_display.undraw()

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if (points - rounds) <= 0:
                        return 0
                    return points - rounds
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if (points - rounds) <= 0:
                            return 0
                        return points - rounds
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1 * term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 1
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if (points - rounds) <= 0:
                    return 0
                return points - rounds

def lvl6():
    global menu
    global t1
    global gametime
    global gameon

    t1 = float(time.time())
    points = 0
    rounds = 1
    add = 1

    while True:
        operation = random.randint(0, 3)

        if operation == 0:

            keystring = ""
            gameon = True
            term = 504833
            termdif = 309855
            ans = False

            term1 = random.randint((term-termdif) +rounds, term +rounds +termdif)
            term2 = random.randint((term-termdif) +rounds, term +rounds +termdif)
            sign = "+"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            game_time_display.draw(win)
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if points <= 0:
                        return 0
                    return points
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if points <= 0:
                            return 0
                        return points
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1 + term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 2
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if points <= 0:
                    return 0
                return points

        if operation == 1:
            keystring = ""
            gameon = True
            term = 940395
            termdif = 55474
            ans = False
            term2 = random.randint((term-termdif) +rounds, term +rounds)
            term1 = random.randint((term) +rounds, term +rounds +termdif)
            sign = "-"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            game_time_display.draw(win)
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if points <= 0:
                        return 0
                    return points
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if points <= 0:
                            return 0
                        return points
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1 - term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 2
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if points <= 0:
                    return 0
                return points
        
        if operation == 2:
            keystring = ""
            gameon = True
            term = 357
            termdif = 334
            ans = False
            term2 = random.randint((term) -termdif, term +add//2)
            term1 = term2*(random.randint(2, (term)))
            sign = "/"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            game_time_display.draw(win)
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if points <= 0:
                        return 0
                    return points
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if points <= 0:
                            return 0
                        return points
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1/term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 1
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if points <= 0:
                    return 0
                return points

        if operation == 3:
            keystring = ""
            gameon = True
            term = 357
            termdif = 294
            ans = False
            term2 = random.randint((term) -termdif, term +termdif +add)
            term1 = random.randint((term) -termdif, term +termdif +add)
            sign = "x"

            for _ in range(1):
                leftx = termbegin
                lefty = termy
                left = Text(Point(leftx, lefty), f"{term1}")
                left.setFill("white")
                left.setStyle("bold")
                left.setSize(35)

                signx = termbegin + termspace
                signy = termy
                sign = Text(Point(signx, signy), f"{sign}")
                sign.setFill("white")
                sign.setStyle("bold")
                sign.setSize(35)

                rightx = signx + termspace
                righty = termy
                right = Text(Point(rightx, righty), f"{term2}")
                right.setFill("white")
                right.setStyle("bold")
                right.setSize(35)

                equalx = rightx + termspace
                equaly = termy
                equal = Text(Point(equalx, equaly), f"=")
                equal.setFill("white")
                equal.setStyle("bold")
                equal.setSize(35)

                pointx = 150
                pointy = 750
                point = Text(Point(pointx, pointy), f"Score: {points}")
                point.setFill("white")
                point.setStyle("bold")
                point.setSize(35)

                

                answerbx = 500
                answerby = 500
                answerbox = Entry(Point(answerbx, answerby), 10)
                answerbox.setFill("white")
                answerbox.setStyle("bold")
                answerbox.setSize(35)
            game_time_display.draw(win)
            left.draw(win)
            sign.draw(win)
            right.draw(win)
            equal.draw(win)
            answerbox.draw(win)
            point.draw(win)

            keystring = ""
            ans = False

            while ans == False:
                
                keystring = ""
                if float(time.time()) - t1 >= gametime:
                    gameon = False
                    menu = 0
                    left.undraw()
                    sign.undraw()
                    right.undraw()
                    equal.undraw()
                    answerbox.undraw()
                    point.undraw()
                    game_time_display.undraw()
                    if points <= 0:
                        return 0
                    return points
                
                while keystring != "Return":

                    keystring = win.getKey()
                    if float(time.time()) - t1 >= gametime:
                        gameon = False
                        menu = 0
                        left.undraw()
                        sign.undraw()
                        right.undraw()
                        equal.undraw()
                        answerbox.undraw()
                        point.undraw()
                        game_time_display.undraw()
                        if points <= 0:
                            return 0
                        return points
                    if(keystring == "Return"):
                        if check_int(answerbox.getText()) == True:
                            answer = int(answerbox.getText())
                            if answer == term1 * term2:
                                ans = True
                            
                            else:
                                ans = False
                                keystring = ""
                        answerbox.setText("")
            points += rounds
            rounds += add
            add += 1
            termdif += 1
            answerbox.setText("")

            left.undraw()
            sign.undraw()
            right.undraw()
            equal.undraw()
            answerbox.undraw()
            point.undraw()
            game_time_display.undraw()
            if float(time.time()) - t1 >= gametime:
                gameon = False
                menu = 0
                if points <= 0:
                    return 0
                return points

menu = 0

difspace = int(40)
difbegin = int(75)

termbegin = 300
termspace = 100
termy = 650
t2 = int(0)

for menu_and_options_objects in range(1):

    titlex = int(500)
    titley = int(650)
    title = Text(Point(titlex, titley), "MATHGOD")
    title.setTextColor("white")
    title.setSize(36)
    title.setStyle("bold")

    nicknametx = int(500)
    nicknamety = int(550)
    nicknametext = Text(Point(nicknametx, nicknamety), f"{name}")
    nicknametext.setFill("white")
    nicknametext.setSize(32)
    nicknametext.setStyle("bold")

    nicknameentryx = nicknametx
    nicknameentryy = nicknamety
    nicknameentry = Entry(Point(nicknameentryx, nicknameentryy), 20)
    nicknameentry.setFill("white")
    nicknameentry.setSize(32)
    nicknameentry.setText(name)
    nicknameentry.setTextColor("black")
    nicknameentry.setStyle("bold")

    playbx1 = int(400)
    playbx2 = int(600)
    playby1 = int(400)
    playby2 = int(500)
    playbox = Rectangle(Point(400, 400), Point(600, 500))
    playbox.setFill("white")

    playtx = int(500)
    playty = int(450)
    playtext = Text(Point(playtx, playty), "Play")
    playtext.setFill("black")
    playtext.setSize(32)
    playtext.setStyle("bold")

    levelbx1 = int(400)
    levelbx2 = int(600)
    levelby1 = int(270)
    levelby2 = int(330)
    levelbox = Rectangle(Point(levelbx1, levelby1), Point(levelbx2, levelby2))
    levelbox.setFill("white")

    leveltx = int(500)
    levelty = int(300)
    leveltext = Text(Point(leveltx, levelty), "Levels")
    leveltext.setFill("black")
    leveltext.setSize(32)
    leveltext.setStyle("bold")






    menx1 = int(400)
    menx2 = int(600)
    meny1 = int(270)
    meny2 = int(330)
    men = Rectangle(Point(menx1, meny1), Point(menx2, meny2))
    men.setFill("white")

    mentx = int(500)
    menty = int(300)
    mentext = Text(Point(mentx, menty), "Menu")
    mentext.setFill("black")
    mentext.setSize(32)
    mentext.setStyle("bold")




    dif1x1 = int(difbegin)
    dif1x2 = dif1x1 + 100
    dif1y1 = int(650)
    dif1y2 = int(700)
    dif1 = Rectangle(Point(dif1x1, dif1y1), Point(dif1x2, dif1y2))
    dif1.setFill("grey")

    dif1tx = dif1x2 -50
    dif1ty = int(675)
    dif1text = Text(Point(dif1tx, dif1ty), "Level 1")
    dif1text.setFill("black")
    dif1text.setSize(20)
    dif1text.setStyle("bold")


    dif2x1 = dif1x2 + difspace
    dif2x2 = dif2x1 + 100
    dif2y1 = int(650)
    dif2y2 = int(700)
    dif2 = Rectangle(Point(dif2x1, dif2y1), Point(dif2x2, dif2y2))
    dif2.setFill("white")

    dif2tx = dif2x2 -50
    dif2ty = int(675)
    dif2text = Text(Point(dif2tx, dif2ty), "Level 2")
    dif2text.setFill("black")
    dif2text.setSize(20)
    dif2text.setStyle("bold")


    dif3x1 = dif2x2 + difspace
    dif3x2 = dif3x1 + 100
    dif3y1 = int(650)
    dif3y2 = int(700)
    dif3 = Rectangle(Point(dif3x1, dif3y1), Point(dif3x2, dif3y2))
    dif3.setFill("white")

    dif3tx = dif3x2 -50
    dif3ty = int(675)
    dif3text = Text(Point(dif3tx, dif3ty), "Level 3")
    dif3text.setFill("black")
    dif3text.setSize(20)
    dif3text.setStyle("bold")


    dif4x1 = dif3x2 + difspace
    dif4x2 = dif4x1 +100
    dif4y1 = int(650)
    dif4y2 = int(700)
    dif4 = Rectangle(Point(dif4x1, dif4y1), Point(dif4x2, dif4y2))
    dif4.setFill("white")

    dif4tx = dif4x2 - 50
    dif4ty = int(675)
    dif4text = Text(Point(dif4tx, dif4ty), "Level 4")
    dif4text.setFill("black")
    dif4text.setSize(20)
    dif4text.setStyle("bold")


    dif5x1 = dif4x2 + difspace
    dif5x2 = dif5x1 + 100
    dif5y1 = int(650)
    dif5y2 = int(700)
    dif5 = Rectangle(Point(dif5x1, dif5y1), Point(dif5x2, dif5y2))
    dif5.setFill("white")

    dif5tx = dif5x2 -50
    dif5ty = int(675)
    dif5text = Text(Point(dif5tx, dif5ty), "Level 5")
    dif5text.setFill("black")
    dif5text.setSize(20)
    dif5text.setStyle("bold")

    dif6x1 = dif5x2 + difspace
    dif6x2 = dif6x1 + 100
    dif6y1 = int(650)
    dif6y2 = int(700)
    dif6 = Rectangle(Point(dif6x1, dif6y1), Point(dif6x2, dif6y2))
    dif6.setFill("white")

    dif6tx = dif6x2 -50
    dif6ty = int(675)
    dif6text = Text(Point(dif6tx, dif6ty), "Extreme")
    dif6text.setFill("black")
    dif6text.setSize(18)
    dif6text.setStyle("bold")




    desc1x = dif1x2 -50
    desc1y = int(600)
    desc1text = Text(Point(desc1x, desc1y), "Only Addition")
    desc1text.setFill("white")
    desc1text.setSize(13)
    desc1text.setStyle("bold")

    desc2x = dif2x2 -50
    desc2y = int(600)
    desc2text = Text(Point(desc2x, desc2y), "Only Subtraction")
    desc2text.setFill("white")
    desc2text.setSize(13)
    desc2text.setStyle("bold")

    desc3x = dif3x2 -50
    desc3y = int(600)
    desc3text = Text(Point(desc3x, desc3y), "Only Division")
    desc3text.setFill("white")
    desc3text.setSize(13)
    desc3text.setStyle("bold")

    desc4x = dif4x2 -50
    desc4y = int(600)
    desc4text = Text(Point(desc4x, desc4y), "Only Multiplication")
    desc4text.setFill("white")
    desc4text.setSize(13)
    desc4text.setStyle("bold")

    desc5x = dif5x2 -50
    desc5y = int(600)
    desc5text = Text(Point(desc5x, desc5y), "Mixed")
    desc5text.setFill("white")
    desc5text.setSize(13)
    desc5text.setStyle("bold")

    desc6x = dif6x2 -50
    desc6y = int(600)
    desc6text = Text(Point(desc6x, desc6y), "Nightmare mode")
    desc6text.setFill("white")
    desc6text.setSize(13)
    desc6text.setStyle("bold")

for gameplay_objects in range(1):

    errorx = 500
    errory = 650
    error = Text(Point(errorx, errory), "ERROR")
    error.setFill("white")
    error.setStyle("bold")
    error.setSize(36)

    countx = 500
    county = 650
    count = Text(Point(countx, county), "3")
    count.setFill("white")
    count.setStyle("bold")
    count.setSize(35)

    answerbx = 500
    answerby = 500
    answerbox = Entry(Point(answerbx, answerby), 10)
    answerbox.setFill("white")
    answerbox.setStyle("bold")
    answerbox.setSize(35)

    game_time_displayx = 725
    game_time_displayy = 725
    game_time_display = Text(Point(game_time_displayx, game_time_displayy), "1 minute, the clock is ticking")
    game_time_display.setFill("white")
    game_time_display.setStyle("bold")
    game_time_display.setSize(22)


def main():
    global name
    global lvl
    alreadydrawn0 = 0
    alreadydrawn1 = 0
    alreadydrawn2 = 0
    lvl = 1
    menu = 0
    while True:


        while menu == 0:

            while alreadydrawn0 == 0:
                playbox.draw(win)
                playtext.draw(win)
                levelbox.draw(win)
                leveltext.draw(win)
                title.draw(win)
                nicknametext.draw(win)
                alreadydrawn0 = 1
            c = win.getMouse()
            cx = c.getX()
            cy = c.getY()
            if playbx1 < cx < playbx2 and playby1< cy < playby2:
                menu = 1
                playbox.undraw()
                playtext.undraw()
                levelbox.undraw()
                leveltext.undraw()
                title.undraw()
                nicknametext.undraw()
                alreadydrawn0 = 0
            if levelbx1 < cx < levelbx2 and levelby1< cy < levelby2:
                menu = 2
                playbox.undraw()
                playtext.undraw()
                levelbox.undraw()
                leveltext.undraw()
                title.undraw()
                nicknametext.undraw()
                alreadydrawn0 = 0
            if nicknametx-70 < cx < nicknametx+70 and nicknamety-50 < cy < nicknamety+50:
                nicknameentry.draw(win)
                key = "sfg"
                while (nicknametx-170 < cx < nicknametx+170 and nicknamety-100 < cy < nicknamety+100) and key != "Return":
                    new_name = nicknameentry.getText()
                    if len(new_name) > 20:
                        text = nicknameentry.getText()
                        nicknameentry.setText(text[:len(text)-1])

                    key = win.getKey()
                    if key == "Return":
                        break

                    if len(new_name) > 20:
                        text = nicknameentry.getText()
                        nicknameentry.setText(text[:len(text)-1])



                    

                nicknameentry.undraw()
                new_nickname = nicknameentry.getText()
                name = new_nickname
                nicknametext.setText(new_nickname)


            else:
                pass


        while menu == 2:

            while alreadydrawn2 == 0:

                men.draw(win)
                mentext.draw(win)
                dif1.draw(win)
                dif1text.draw(win)
                dif2.draw(win)
                dif2text.draw(win)
                dif3.draw(win)
                dif3text.draw(win)
                dif4.draw(win)
                dif4text.draw(win)
                dif5.draw(win)
                dif6.draw(win)
                dif6text.draw(win)
                dif5text.draw(win)
                desc1text.draw(win)
                desc2text.draw(win)
                desc3text.draw(win)
                desc4text.draw(win)
                desc5text.draw(win)
                desc6text.draw(win)

                alreadydrawn2 = 1
            
            c = win.getMouse()

            cx = c.getX()
            cy = c.getY()

            if menx1 < cx < menx2 and meny1< cy < meny2:
                menu = 0

                men.undraw()
                mentext.undraw()
                dif1.undraw()
                dif1text.undraw()
                dif2.undraw()
                dif2text.undraw()
                dif3.undraw()
                dif3text.undraw()
                dif4.undraw()
                dif4text.undraw()
                dif5.undraw()
                dif6text.undraw()
                dif6.undraw()
                dif5text.undraw()
                desc1text.undraw()
                desc2text.undraw()
                desc3text.undraw()
                desc4text.undraw()
                desc5text.undraw()
                desc6text.undraw()

                alreadydrawn2 = 0
            
            for x in range(1):

                if dif1x1 < cx < dif1x2 and dif1y1< cy < dif1y2:
                    dif1.setFill("grey")
                    dif2.setFill("white")
                    dif3.setFill("white")
                    dif4.setFill("white")
                    dif5.setFill("white")
                    dif6.setFill("white")
                    lvl = 1

                if dif2x1 < cx < dif2x2 and dif2y1< cy < dif2y2:
                    dif1.setFill("white")
                    dif2.setFill("grey")
                    dif3.setFill("white")
                    dif4.setFill("white")
                    dif5.setFill("white")
                    dif6.setFill("white")
                    lvl = 2

                if dif3x1 < cx < dif3x2 and dif3y1< cy < dif3y2:
                    dif1.setFill("white")
                    dif2.setFill("white")
                    dif3.setFill("grey")
                    dif4.setFill("white")
                    dif5.setFill("white")
                    dif6.setFill("white")
                    lvl = 3
                    
                if dif4x1 < cx < dif4x2 and dif4y1< cy < dif4y2:
                    dif1.setFill("white")
                    dif2.setFill("white")
                    dif3.setFill("white")
                    dif4.setFill("grey")
                    dif5.setFill("white")
                    dif6.setFill("white")
                    lvl = 4

                if dif5x1 < cx < dif5x2 and dif5y1< cy < dif5y2:
                    dif1.setFill("white")
                    dif2.setFill("white")
                    dif3.setFill("white")
                    dif4.setFill("white")
                    dif5.setFill("grey")
                    dif6.setFill("white")
                    lvl = 5

                if dif6x1 < cx < dif6x2 and dif6y1< cy < dif6y2:
                    dif1.setFill("white")
                    dif2.setFill("white")
                    dif3.setFill("white")
                    dif4.setFill("white")
                    dif5.setFill("white")
                    dif6.setFill("grey")
                    lvl = 6


            else:
                pass


        while menu == 1:

            countdown()

            descriptiontext.undraw()
            if lvl == 1:
                score = lvl1()
            if lvl == 2:
                score = lvl2()
            if lvl == 3:
                score = lvl3()
            if lvl == 4:
                score = lvl4()
            if lvl == 5:
                score = lvl5()
            if lvl == 6:
                score = lvl6()
            time.sleep(2)
            index = savescore(name, score)
            end_of_game(name, score, index)
            descriptiontext.draw(win)
            menu = 0



if __name__ == '__main__':
    main()