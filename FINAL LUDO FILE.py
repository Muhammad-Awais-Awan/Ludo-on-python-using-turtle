import turtle
import random
import os
import sys 
#import picture of ludo
sn=turtle.Screen()
sn.title("ludo game")
sn.screensize(490,490)
sn.bgcolor("black")
#load=sn.bgpic("load.gif")
while True:
   chooseNumberOfPlayers=eval(input("Choose the number of players")) 
   if  chooseNumberOfPlayers<2 or  chooseNumberOfPlayers>4:
       print("only 2,3 or 4 players can play ludo")
       continue
   else:
       
       break
    


##########################      PAWNS    ###########################
##########################               ###########################


def fourplayers():
            NameOfRedPlayer= input("ENTER red player name")
            NameOfBluePlayer= input("ENTER blue player name")
            NameOfYellowPlayer= input("ENTER yellow player name")
            NameOfGreenPlayer= input("ENTER Green player name")
            redname=turtle.Turtle()
            redname.penup()
            redname.color("firebrick")
            redname.goto(120,210)
            redname.write(NameOfRedPlayer,font=('Arial',30))
            redname.hideturtle()
            bluename=turtle.Turtle()
            bluename.penup()
            bluename.color("navy")
            bluename.goto(120,-230)
            bluename.write(NameOfBluePlayer,font=('Arial',30))
            bluename.hideturtle()
            yellowname=turtle.Turtle()
            yellowname.penup()
            yellowname.color("darkorange")
            yellowname.goto(-190,-230)
            yellowname.write(NameOfYellowPlayer,font=('Arial',30))
            yellowname.hideturtle()
            greenname=turtle.Turtle()
            greenname.penup()
            greenname.color("spring green")
            greenname.goto(-200,220)
            greenname.write(NameOfGreenPlayer,font=('Arial',30))
            greenname.hideturtle()
            #PAWN OF RED
            #r1
            '''pr11=turtle.Turtle()
            pr11.shape("square")
            pr11.shapesize(5,5)
            pr11.color("blue")
            pr11.goto(139,139)'''
            pr1= turtle.Turtle()
            pr1.shape("circle")
            pr1.color("firebrick")
            pr1.penup()
            pr1.speed(10000)
            pr1.setpos(180,180)


            #pr1.write(1, font=('Arial',16), align=('center'))
            #pr1.stamp()
            #pr1.hideturtle()


            #r2
            pr2=turtle.Turtle()
            pr2.shape("square")
            pr2.color("firebrick")
            pr2.penup()
            pr2.speed(100)
            pr2.setpos(180,115)
            #r3
            pr3=turtle.Turtle()
            pr3.shape("triangle")
            pr3.color("firebrick")
            pr3.penup()
            pr3.speed(100)
            pr3.setpos(115,115)
            #r4
            pr4=turtle.Turtle()
            pr4.shape("turtle")
            pr4.color("firebrick")
            pr4.penup()
            pr4.speed(100)
            pr4.setpos(115,180)


            #PAWN OF BLUE
            #b1
            pb1= turtle.Turtle()
            pb1.shape("circle")
            pb1.color("navy")
            pb1.penup()
            pb1.speed(100)
            pb1.setpos(180,-180)
            #b2
            pb2= turtle.Turtle()
            pb2.shape("square")
            pb2.color("navy")
            pb2.penup()
            pb2.speed(100)
            pb2.setpos(180,-115)
            #b3
            pb3= turtle.Turtle()
            pb3.shape("triangle")
            pb3.color("navy")
            pb3.penup()
            pb3.speed(100)
            pb3.setpos(115,-115)
            #b4
            pb4= turtle.Turtle()
            pb4.shape("turtle")
            pb4.color("navy")
            pb4.penup()
            pb4.speed(100)
            pb4.setpos(115,-180)


            #PAWN OF YELLOW
            #y1
            py1= turtle.Turtle()
            py1.shape("circle")
            py1.color("darkorange")
            py1.penup()
            py1.speed(100)
            py1.setpos(-180,-180)
            #y2
            py2= turtle.Turtle()
            py2.shape("square")
            py2.color("darkorange")
            py2.penup()
            py2.speed(100)
            py2.setpos(-180,-115)
            #y3
            py3= turtle.Turtle()
            py3.shape("triangle")
            py3.color("darkorange")
            py3.penup()
            py3.speed(100)
            py3.setpos(-115,-115)
            #y4
            py4= turtle.Turtle()
            py4.shape("turtle")
            py4.color("darkorange")
            py4.penup()
            py4.speed(100)
            py4.setpos(-115,-180)


            #PAWN OF GREEN
            #g1
            pg1= turtle.Turtle()
            pg1.shape("circle")
            pg1.color("spring green")
            pg1.penup()
            pg1.speed(100)
            pg1.setpos(-180,180)
            #g2
            pg2= turtle.Turtle()
            pg2.shape("square")
            pg2.color("spring green")
            pg2.penup()
            pg2.speed(100)
            pg2.setpos(-180,115)
            #g3
            pg3= turtle.Turtle()
            pg3.shape("triangle")
            pg3.color("spring green")
            pg3.penup()
            pg3.speed(100)
            pg3.setpos(-115,115)
            #g4
            pg4= turtle.Turtle()
            pg4.shape("turtle")
            pg4.color("spring green")
            pg4.penup()
            pg4.speed(100)
            pg4.setpos(-115,180)

            ###########################       STOP               ##################
            ###########################       BOXES              ##################   

            #STOP BOXES OF RED########
            #RED TEAM COLUMN #1
            r1=turtle.Turtle()
            r1.speed(100)
            r1.shape("square")
            r1.shapesize(1.4,1.5)
            r1.color("white")
            r1.penup()
            k=r1.setpos(-36,67)



            #RED TEAM COLUMN #1
            r2=turtle.Turtle()
            r2.speed(100)
            r2.shape("square")
            r2.shapesize(1.4,1.5)
            r2.color("white")
            r2.penup()
            k=r2.setpos(-36,99)

            #RED TEAM COLUMN #1
            r3=turtle.Turtle()
            r3.speed(100)
            r3.shape("square")
            r3.shapesize(1.4,1.5)
            r3.color("white")
            r3.penup()
            k=r3.setpos(-36,132)

            #RED TEAM COLUMN #1
            r4=turtle.Turtle()
            r4.speed(100)
            r4.shape("square")
            r4.shapesize(1.4,1.5)
            r4.color("red")
            r4.penup()
            k=r4.setpos(-36,164)

            #RED TEAM COLUMN #1
            r5=turtle.Turtle()
            r5.speed(100)
            r5.shape("square")
            r5.shapesize(1.4,1.5)
            r5.color("white")
            r5.penup()
            k=r5.setpos(-36,197)

            #RED TEAM COLUMN #1
            r6=turtle.Turtle()
            r6.speed(100)
            r6.shape("square")
            r6.shapesize(1.4,1.5)
            r6.color("white")
            r6.penup()
            k=r6.setpos(-36,230)

            #RED TEAM COLUMN #2
            r7=turtle.Turtle()
            r7.speed(100)
            r7.shape("square")
            r7.shapesize(1.4,1.5)
            r7.color("red")
            r7.penup()
            k=r7.setpos(-2,67)

            #RED TEAM COLUMN #2
            r8=turtle.Turtle()
            r8.speed(100)
            r8.shape("square")
            r8.shapesize(1.4,1.5)
            r8.color("red")
            r8.penup()
            k=r8.setpos(-2,99)

            #RED TEAM COLUMN #2
            r9=turtle.Turtle()
            r9.speed(100)
            r9.shape("square")
            r9.shapesize(1.4,1.5)
            r9.color("red")
            r9.penup()
            k=r9.setpos(-2,132)

            #RED TEAM COLUMN #2
            r10=turtle.Turtle()
            r10.speed(100)
            r10.shape("square")
            r10.shapesize(1.4,1.5)
            r10.color("red")
            r10.penup()
            k=r10.setpos(-2,164)

            #RED TEAM COLUMN #2
            r11=turtle.Turtle()
            r11.speed(100)
            r11.shape("square")
            r11.shapesize(1.4,1.5)
            r11.color("red")
            r11.penup()
            k=r11.setpos(-2,197)

            #RED TEAM COLUMN #2
            r12=turtle.Turtle()
            r12.speed(100)
            r12.shape("square")
            r12.shapesize(1.4,1.5)
            r12.color("white")
            r12.penup()
            k=r12.setpos(-2,230)

            #RED TEAM COLUMN #3
            r13=turtle.Turtle()
            r13.speed(100)
            r13.shape("square")
            r13.shapesize(1.4,1.5)
            r13.color("white")
            r13.penup()
            k=r13.setpos(33,67)



            #RED TEAM COLUMN #3
            r14=turtle.Turtle()
            r14.speed(100)
            r14.shape("square")
            r14.shapesize(1.4,1.5)
            r14.color("white")
            r14.penup()
            k=r14.setpos(33,99)

            #RED TEAM COLUMN #3
            r15=turtle.Turtle()
            r15.speed(100)
            r15.shape("square")
            r15.shapesize(1.4,1.5)
            r15.color("white")
            r15.penup()
            k=r15.setpos(33,132)

            #RED TEAM COLUMN #3
            r16=turtle.Turtle()
            r16.speed(100)
            r16.shape("square")
            r16.shapesize(1.4,1.5)
            r16.color("white")
            r16.penup()
            k=r16.setpos(33,164)

            #RED TEAM COLUMN #3
            r17=turtle.Turtle()
            r17.speed(100)
            r17.shape("square")
            r17.shapesize(1.4,1.5)
            r17.color("red")
            r17.penup()
            k=r17.setpos(33,197)

            #RED TEAM COLUMN #3
            r18=turtle.Turtle()
            r18.speed(100)
            r18.shape("square")
            r18.shapesize(1.4,1.5)
            r18.color("white")
            r18.penup()
            k=r18.setpos(33,230)

            ######### STOP BOXES FOR BLUE COLOR ################

            #BLUE TEAM COLUMN 1
            b1=turtle.Turtle()
            b1.speed(100)
            b1.shape("square")
            b1.shapesize(1.5,1.4)
            b1.color("white")
            b1.penup()
            k=b1.setpos(64,36)

            #BLUE TEAM COLUMN 1
            b2=turtle.Turtle()
            b2.speed(100)
            b2.shape("square")
            b2.shapesize(1.5,1.4)
            b2.color("white")
            b2.penup()
            k=b2.setpos(96,36)


            #BLUE TEAM COLUMN 1
            b3=turtle.Turtle()
            b3.speed(100)
            b3.shape("square")
            b3.shapesize(1.5,1.4)
            b3.color("white")
            b3.penup()
            k=b3.setpos(129,36)


            #BLUE TEAM COLUMN 1
            b4=turtle.Turtle()
            b4.speed(100)
            b4.shape("square")
            b4.shapesize(1.5,1.4)
            b4.color("sky blue")
            b4.penup()
            k=b4.setpos(161,36)


            #BLUE TEAM COLUMN 1
            b5=turtle.Turtle()
            b5.speed(100)
            b5.shape("square")
            b5.shapesize(1.5,1.4)
            b5.color("white")
            b5.penup()
            k=b5.setpos(194,36)


            #BLUE TEAM COLUMN 1
            b6=turtle.Turtle()
            b6.speed(100)
            b6.shape("square")
            b6.shapesize(1.5,1.4)
            b6.color("white")
            b6.penup()
            k=b6.setpos(227,36)


            #BLUE TEAM COLUMN #2
            b7=turtle.Turtle()
            b7.speed(100)
            b7.shape("square")
            b7.shapesize(1.5,1.4)
            b7.color("sky blue")
            b7.penup()
            k=b7.setpos(64,1)


            #BLUE TEAM COLUMN #2
            b8=turtle.Turtle()
            b8.speed(100)
            b8.shape("square")
            b8.shapesize(1.5,1.4)
            b8.color("sky blue")
            b8.penup()
            k=b8.setpos(96,1)


            #BLUE TEAM COLUMN #2
            b9=turtle.Turtle()
            b9.speed(100)
            b9.shape("square")
            b9.shapesize(1.5,1.4)
            b9.color("sky blue")
            b9.penup()
            k=b9.setpos(129,1)


            #BLUE TEAM COLUMN #2
            b10=turtle.Turtle()
            b10.speed(100)
            b10.shape("square")
            b10.shapesize(1.5,1.4)
            b10.color("sky blue")
            b10.penup()
            k=b10.setpos(162,1)


            #BLUE TEAM COLUMN #2
            b11=turtle.Turtle()
            b11.speed(100)
            b11.shape("square")
            b11.shapesize(1.5,1.4)
            b11.color("sky blue")
            b11.penup()
            k=b11.setpos(195,1)


            #BLUE TEAM COLUMN #2
            b12=turtle.Turtle()
            b12.speed(100)
            b12.shape("square")
            b12.shapesize(1.5,1.4)
            b12.color("white")
            b12.penup()
            k=b12.setpos(227,1)



            #BLUE TEAM COLUMN 3
            b13=turtle.Turtle()
            b13.speed(100)
            b13.shape("square")
            b13.shapesize(1.5,1.4)
            b13.color("white")
            b13.penup()
            k=b13.setpos(64,-33)


            #BLUE TEAM COLUMN 3
            b14=turtle.Turtle()
            b14.speed(100)
            b14.shape("square")
            b14.shapesize(1.5,1.4)
            b14.color("white")
            b14.penup()
            k=b14.setpos(97,-33)



            #BLUE TEAM COLUMN 3
            b15=turtle.Turtle()
            b15.speed(100)
            b15.shape("square")
            b15.shapesize(1.5,1.4)
            b15.color("white")
            b15.penup()
            k=b15.setpos(129,-33)



            #BLUE TEAM COLUMN 3
            b16=turtle.Turtle()
            b16.speed(100)
            b16.shape("square")
            b16.shapesize(1.5,1.4)
            b16.color("white")
            b16.penup()
            k=b16.setpos(161,-33)



            #BLUE TEAM COLUMN 3
            b17=turtle.Turtle()
            b17.speed(100)
            b17.shape("square")
            b17.shapesize(1.5,1.4)
            b17.color("sky blue")
            b17.penup()
            k=b17.setpos(194,-33)



            #BLUE TEAM COLUMN 3
            b18=turtle.Turtle()
            b18.speed(100)
            b18.shape("square")
            b18.shapesize(1.5,1.4)
            b18.color("white")
            b18.penup()
            k=b18.setpos(227,-33)


            #STOP BOXES OF YELLOW#######

            #yellow team column #1
            y1=turtle.Turtle()
            y1.speed(100)
            y1.shape("square")
            y1.shapesize(1.4,1.5)
            y1.color("white")
            y1.penup()
            k=y1.setpos(33,-67)



            #yellow team column #1
            y2=turtle.Turtle()
            y2.speed(100)
            y2.shape("square")
            y2.shapesize(1.4,1.5)
            y2.color("white")
            y2.penup()
            k=y2.setpos(33,-99)

            #yellow team column #1
            y3=turtle.Turtle()
            y3.speed(100)
            y3.shape("square")
            y3.shapesize(1.4,1.5)
            y3.color("white")
            y3.penup()
            k=y3.setpos(33,-132)

            #yellow team column #1
            y4=turtle.Turtle()
            y4.speed(100)
            y4.shape("square")
            y4.shapesize(1.4,1.5)
            y4.color("yellow")
            y4.penup()
            k=y4.setpos(33,-164)

            #yellow team column #1
            y5=turtle.Turtle()
            y5.speed(100)
            y5.shape("square")
            y5.shapesize(1.4,1.5)
            y5.color("white")
            y5.penup()
            k=y5.setpos(33,-197)

            #yellow team column #1
            y6=turtle.Turtle()
            y6.speed(100)
            y6.shape("square")
            y6.shapesize(1.4,1.5)
            y6.color("white")
            y6.penup()
            k=y6.setpos(33,-230)

            #yellow team column #2
            y7=turtle.Turtle()
            y7.speed(100)
            y7.shape("square")
            y7.shapesize(1.4,1.5)
            y7.color("yellow")
            y7.penup()
            k=y7.setpos(-2,-67)

            #yellow team column #2
            y8=turtle.Turtle()
            y8.speed(100)
            y8.shape("square")
            y8.shapesize(1.4,1.5)
            y8.color("yellow")
            y8.penup()
            k=y8.setpos(-2,-99)

            #yellow team column #2
            y9=turtle.Turtle()
            y9.speed(100)
            y9.shape("square")
            y9.shapesize(1.4,1.5)
            y9.color("yellow")
            y9.penup()
            k=y9.setpos(-2,-132)

            #yellow team column #2
            y10=turtle.Turtle()
            y10.speed(100)
            y10.shape("square")
            y10.shapesize(1.4,1.5)
            y10.color("yellow")
            y10.penup()
            k=y10.setpos(-2,-164)

            #yellow team column #2
            y11=turtle.Turtle()
            y11.speed(100)
            y11.shape("square")
            y11.shapesize(1.4,1.5)
            y11.color("yellow")
            y11.penup()
            k= y11.setpos(-2,-197)

            #yellow team column #2
            y12=turtle.Turtle()
            y12.speed(100)
            y12.shape("square")
            y12.shapesize(1.4,1.5)
            y12.color("white")
            y12.penup()
            k=y12.setpos(-2,-230)



            #yellow team column #3
            y13=turtle.Turtle()
            y13.speed(100)
            y13.shape("square")
            y13.shapesize(1.4,1.5)
            y13.color("white")
            y13.penup()
            k=y13.setpos(-36,-67)



            #yellow team column #3
            y14=turtle.Turtle()
            y14.speed(100)
            y14.shape("square")
            y14.shapesize(1.4,1.5)
            y14.color("white")
            y14.penup()
            k=y14.setpos(-36,-99)

            #yellow team column #3
            y15=turtle.Turtle()
            y15.speed(100)
            y15.shape("square")
            y15.shapesize(1.4,1.5)
            y15.color("white")
            y15.penup()
            k=y15.setpos(-36,-132)

            #yellow team column #3
            y16=turtle.Turtle()
            y16.speed(100)
            y16.shape("square")
            y16.shapesize(1.4,1.5)
            y16.color("white")
            y16.penup()
            k=y16.setpos(-36,-164)

            #yellow team column #3
            y17=turtle.Turtle()
            y17.speed(100)
            y17.shape("square")
            y17.shapesize(1.4,1.5)
            y17.color("yellow")
            y17.penup()
            k=y17.setpos(-36,-197)

            #yellow team column #3
            y18=turtle.Turtle()
            y18.speed(100)
            y18.shape("square")
            y18.shapesize(1.4,1.5)
            y18.color("white")
            y18.penup()
            k=y18.setpos(-36,-230)



            ########### STOP BOXES FOR GREEN ############

            #GREEN TEAM COLUMN #1
            g1=turtle.Turtle()
            g1.speed(100)
            g1.shape("square")
            g1.shapesize(1.5,1.4)
            g1.color("white")
            g1.penup()
            k=g1.setpos(-67,-33)

            #GREEN TEAM COLUMN #1
            g2=turtle.Turtle()
            g2.speed(100)
            g2.shape("square")
            g2.shapesize(1.5,1.4)
            g2.color("white")
            g2.penup()
            k=g2.setpos(-99,-33)


            #GREEN TEAM COLUMN #1
            g3=turtle.Turtle()
            g3.speed(100)
            g3.shape("square")
            g3.shapesize(1.5,1.4)
            g3.color("white")
            g3.penup()
            k=g3.setpos(-132,-33)


            #GREEN TEAM COLUMN #1
            g4=turtle.Turtle()
            g4.speed(100)
            g4.shape("square")
            g4.shapesize(1.5,1.4)
            g4.color("dark green")
            g4.penup()
            k=g4.setpos(-164,-33)


            #GREEN TEAM COLUMN #1
            g5=turtle.Turtle()
            g5.speed(100)
            g5.shape("square")
            g5.shapesize(1.5,1.4)
            g5.color("white")
            g5.penup()
            k=g5.setpos(-197,-33)


            #GREEN TEAM COLUMN #1
            g6=turtle.Turtle()
            g6.speed(100)
            g6.shape("square")
            g6.shapesize(1.5,1.4)
            g6.color("white")
            g6.penup()
            k=g6.setpos(-230,-33)


            #GREEN TEAM COLUMN #2
            g7=turtle.Turtle()
            g7.speed(100)
            g7.shape("square")
            g7.shapesize(1.5,1.4)
            g7.color("dark green")
            g7.penup()
            k=g7.setpos(-67,1)


            #GREEN TEAM COLUMN #2
            g8=turtle.Turtle()
            g8.speed(100)
            g8.shape("square")
            g8.shapesize(1.5,1.4)
            g8.color("dark green")
            g8.penup()
            k=g8.setpos(-99,1)


            #GREEN TEAM COLUMN #2
            g9=turtle.Turtle()
            g9.speed(100)
            g9.shape("square")
            g9.shapesize(1.5,1.4)
            g9.color("dark green")
            g9.penup()
            k=g9.setpos(-132,1)


            #GREEN TEAM COLUMN #2
            g10=turtle.Turtle()
            g10.speed(100)
            g10.shape("square")
            g10.shapesize(1.5,1.4)
            g10.color("dark green")
            g10.penup()
            k=g10.setpos(-164,1)


            #GREEN TEAM COLUMN #2
            g11=turtle.Turtle()
            g11.speed(100)
            g11.shape("square")
            g11.shapesize(1.5,1.4)
            g11.color("dark green")
            g11.penup()
            k=g11.setpos(-197,1)


            #GREEN TEAM COLUMN #2
            g12=turtle.Turtle()
            g12.speed(100)
            g12.shape("square")
            g12.shapesize(1.5,1.4)
            g12.color("white")
            g12.penup()
            k=g12.setpos(-230,1)




            #GREEN TEAM COLUMN #3
            g13=turtle.Turtle()
            g13.speed(100)
            g13.shape("square")
            g13.shapesize(1.5,1.4)
            g13.color("white")
            g13.penup()
            k=g13.setpos(-67,36)

            #GREEN TEAM COLUMN #3
            g14=turtle.Turtle()
            g14.speed(100)
            g14.shape("square")
            g14.shapesize(1.5,1.4)
            g14.color("white")
            g14.penup()
            k=g14.setpos(-99,36)


            #GREEN TEAM COLUMN #3
            g15=turtle.Turtle()
            g15.speed(100)
            g15.shape("square")
            g15.shapesize(1.5,1.4)
            g15.color("white")
            g15.penup()
            k=g15.setpos(-132,36)


            #GREEN TEAM COLUMN #3
            g16=turtle.Turtle()
            g16.speed(100)
            g16.shape("square")
            g16.shapesize(1.5,1.4)
            g16.color("white")
            g16.penup()
            k=g16.setpos(-164,36)


            #GREEN TEAM COLUMN #3
            g17=turtle.Turtle()
            g17.speed(100)
            g17.shape("square")
            g17.shapesize(1.5,1.4)
            g17.color("dark green")
            g17.penup()
            k=g17.setpos(-197,36)


            #GREEN TEAM COLUMN #3
            g18=turtle.Turtle()
            g18.speed(100)
            g18.shape("square")
            g18.shapesize(1.5,1.4)
            g18.color("white")
            g18.penup()
            k=g18.setpos(-230,36)

            #################################### DICE  ##############################
            ####################################       ##############################
            #lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7]
            end=turtle.Turtle()
            end.shape("square")
            end.shapesize(4,4)
            end.goto(0,0)
            '''dice=turtle.Turtle()
            dice.shape("square")
            dice.color("grey")
            dice.speed(0)
            dice.shapesize(2,4)
            dice.penup()
            dice.goto(250,-250)
            #dice.write("CLICKHERE")'''
            '''clickHere = turtle.Turtle()
            clickHere.penup()
            clickHere.goto(250,-250)
            clickHere.write("CLICK HERE")'''
                            #LOGIC OF DICE
            '''a=turtle.Turtle()
            d=turtle.Turtle()'''
            dicenumber=turtle.Turtle()
            dicenumber.hideturtle()
            #positionpr1=int(1)
            #positionpr2=int(1)
            #positionpr3=int(1)
            i=0
            re1=0
            re2=0
            re3=0
            re4=0
            ye1=0
            ye2=0
            ye3=0
            ye4=0
            gr1=0
            gr2=0
            gr3=0
            gr4=0
            bl1=0
            bl2=0
            bl3=0
            bl4=0
            cr1=0
            cr2=0
            cr3=0
            cr4=0
            cy1=0
            cy2=0
            cy3=0
            cy4=0
            cg1=0
            cg2=0
            cg3=0
            cg4=0
            cb1=0
            cb2=0
            cb3=0
            cb4=0
            turns=0
            b=0
            y=0
            r=0
            z=0
            n=0
            forgreen=4
            forred=4
            forblue=4
            foryellow=4
            ################################ LISTS OF PATHS #############################################################

            lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7,end]
            
            lrob=[pb1,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b11,b10,b9,b8,b7,end]
            lroy=[py1,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y11,y10,y9,y8,y7,end]
            lrog=[pg1,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g11,g10,g9,g8,g7,end]
            ####################### LISTS OF positions  ###############################################

            pr4_position=[lrop[re4],lrop[re4+n]]
            pr3_position=[lrop[re3],lrop[re3+n]]
            pr2_position=[lrop[re2],lrop[re2+n]]
            pr1_position=[lrop[re1],lrop[re1+n]]
            py4_position=[lroy[ye4],lroy[ye4+n]]
            py3_position=[lroy[ye3],lroy[ye3+n]]
            py2_position=[lroy[ye2],lroy[ye2+n]]
            py1_position=[lroy[ye1],lroy[ye1+n]]
            pb4_position=[lrob[bl4],lrob[bl4+n]]
            pb3_position=[lrob[bl3],lrob[bl3+n]]
            pb2_position=[lrob[bl2],lrob[bl2+n]]
            pb1_position=[lrob[bl1],lrob[bl1+n]]
            pg1_position=[lrog[gr1],lrog[gr1+n]]
            pg2_position=[lrog[gr2],lrog[gr2+n]]
            pg3_position=[lrog[gr3],lrog[gr3+n]]
            pg4_position=[lrog[gr4],lrog[gr4+n]]                                

            
            while z<1000:
                
             #-----------------------------------GREEN---------------------------------------#   
                 while z<1000:          
                        dicenumber.clear()
                        n=int (random.randint(1,6))
                        
                        #lrog=[pg1,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g11,g10,g9,g8,g7,end]
                        print("GREEN TURN")
                        dicenumber.color('green')
                        #style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        dicenumber.hideturtle()
                        
                        a=eval(input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
                        
            ############################################ PG1 ######################################
                        if( n==6 or cg1>0):
                            cg1+=1
                            if cg1==1:  
                               pg1.goto(lrog[1].pos())
                               gr1+=1
                               cg1+=1
                               continue
                            if (a==1)and (cg1>0):
                               pg1_position=[lrog[gr1],lrog[gr1+n]]
            #lrog=[pg1,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g11,g10,g9,g8,g7,end]
                        
                               pg1.onclick(pg1.goto(pg1_position[1].pos()))
                               #sn.delay(150)
                               gr1=gr1+n
                               
                               if pg1_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pg1_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pg1_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pg1_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif pg1_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pg1_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pg1_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pg1_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               elif pg1_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pg1_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pg1_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pg1_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  gr1 >= 58 or gr2>=58 or gr3>=58 or gr4>=58  :
                                   sys.exit()
                                   print(NameOfGreenPlayer + " Won the game")
                                       
                               if n==6:
                                   continue
                             
                               break
            ##################################################### PG2  ##################################       
                        if n==6 or cg2>0:
                            cg2+=1
                            if cg2==1:
                               pg2.goto(lrog[1].pos())
                               gr2+=1
                               cg2+=1
                               continue
                            if (a==2)and (cg2>0):
                               pg2_position=[lrog[gr2],lrog[gr2+n]]
                               pg2.onclick(pg2.goto(pg2_position[1].pos()))
                               #sn.delay(150)
                               gr2=gr2+n
                               if pg2_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pg2_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pg2_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pg2_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif pg2_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pg2_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pg2_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pg2_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               elif pg2_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pg2_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pg2_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pg2_position[1]== pr4_postion[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  gr1 >= 58 or gr2>=58 or gr3>=58 or gr4>=58  :
                                   sys.exit()
                                   print(NameOfGreenPlayer + " Won the game")
                                       
                               if n==6:
                                   continue
                               break
                           ############################### PG3 #######################
                        if n==6 or cg3>0:
                            cg3+=1
                            if cg3==1:
                               pg3.goto(lrog[1].pos())
                               gr3+=1
                               cg3+=1
                               continue
                            if (a==3)and (cg3>0):
                               pg3_position=[lrog[gr3],lrog[gr3+n]]
                               pg3.onclick(pg3.goto(pg3_position[1].pos()))
                               #sn.delay(150)
                               gr3=gr3+n
                               if pg3_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pg3_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pg3_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pg3_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif pg3_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pg3_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pg3_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pg3_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               elif pg3_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pg3_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pg3_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pg3_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  gr1 >= 58 or gr2>=58 or gr3>=58 or gr4>=58  :
                                   print(NameOfGreenPlayer + " Won the game")
                                   sys.exit()
                                   
                                       
                                   
                               if n==6:
                                   continue 
                               break
                           ###################################  PG4 ##############################
                        if n==6 or cg4>0:
                            cg4+=1
                            if cg4==1:
                               pg4.goto(lrog[1].pos())
                               gr4+=1
                               cg4+=1
                               continue
                            if (a==4)and (cg4>0):
                               pg4_position=[lrog[gr4],lrog[gr4+n]]
                               pg4.onclick(pg4.goto(pg4_position[1].pos()))
                               #sn.delay(150)
                               gr4=gr4+n
                               if pg4_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pg4_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pg4_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pg4_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif pg4_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pg4_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pg4_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pg4_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               elif pg4_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pg4_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pg4_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pg4_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  gr1 >= 58 or gr2>=58 or gr3>=58 or gr4>=58  :
                                   sys.exit()
                                   print(NameOfGreenPlayer + " Won the game")
                                       
                               if n==6:
                                   continue
                               break
                        #if (pg1_position[1]==end):
                            #print("GREEN TEAM WON")
                        break
            #-----------------------------------------RED-----------------------------------------
                 while z<100:        

                        dicenumber.clear()
                        n=int(random.randint(1,6))
                        
                        #lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7,end]
                            
                            
                        print("rrrr")
                        dicenumber.color('red')
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        sn.delay(250)
                        dicenumber.hideturtle()
                        #sn.delay(250)
                        r=eval(input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
            ################################## PR1 ####################################
                        if n==6 or cr1>0:
                            cr1+=1
                            if cr1==1:
                               pr1.goto(lrop[1].pos())
                               re1+=1
                               cr1+=1
                               continue
                            if (r==1)and (cr1>0):
                               pr1_position=[lrop[re1],lrop[re1+n]]
                               pr1.onclick(pr1.goto(pr1_position[1].pos()))
                               re1=re1+n
                               if pr1_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                               elif pr1_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                               elif pr1_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                               elif pr1_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                               elif pr1_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pr1_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pr1_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pr1_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                   sys.exit()
                                   print(NameOfRedPlayer + " Won the game")
                                       
                               if n==6:
                                    continue
                               break
                           ##############################################  PR2 #######################################
                        if n==6 or cr2>0:
                            cr2+=1
                            if cr2==1:
                               pr2.goto(lrop[1].pos())
                               re2+=1
                               cr2+=1
                               continue
                            if (r==2)and (cr2>0):
                                 pr2_position=[lrop[re2],lrop[re2+n]]
                                 pr2.onclick(pr2.goto(pr2_position[1].pos()))
                                 re2=re2+n
                                 if pr2_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif pr2_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif pr2_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif pr2_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif pr2_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pr2_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pr2_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pr2_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                   sys.exit()
                                   print(NameOfRedPlayer + " Won the game")
                                       
                                 if n==6:
                                    continue
                                 break
                 ######################################  PR3 #######################################               
                        if n==6 or cr3>0:
                            cr3+=1
                            if cr3==1:
                               pr3.goto(lrop[1].pos())
                               re3+=1
                               cr3+=1
                               continue
                            if (r==3)and (cr3>0):
                                 pr3_position=[lrop[re3],lrop[re3+n]]
                                 pr3.onclick(pr1.goto(pr3_position[1].pos()))
                                 re3=re3+n
                                 if pr3_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif pr3_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif pr3_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif pr3_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif pr3_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pr3_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pr3_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pr3_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                   sys.exit()
                                   print(NameOfRedPlayer + " Won the game")
                                       
                                 if n==6:
                                    continue
                                 break
             ######################################## PR4 ####################################
                        if n==6 or cr4>0:
                            cr4+=1
                            
                                
                            if cr4==1:
                               pr4.goto(lrop[1].pos())
                               re4+=1
                               cr4+=1
                               continue
                           
                             
                            if (r==4)and (cr4>0):
                                 pr4_position=[lrop[re4],lrop[re4+n]]
                                 pr4.onclick(pr1.goto(pr4_position[1].pos()))
                                 re4=re4+n
                                 if pr4_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif pr4_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif pr4_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif pr4_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif pr4_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pr4_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pr4_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pr4_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                   sys.exit()
                                   print(NameOfRedPlayer + " Won the game")
                                       
                                 if n==6:
                                    continue
                                 break
                            
                        break   
            #-----------------------------------------  BLUE   -----------------------------------------#          
                  
                 while(z<100):
                        dicenumber.clear()
                        n=int (random.randint(1,6))
                        #lrob=[pb1,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b11,b10,b9,b8,b7,end]
                        print("bbbb")
                        dicenumber.color('blue')
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        dicenumber.hideturtle()
                        b=eval (input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
            ########################################################  PB1  ################################################
                        if n==6 or cb1>0:
                            cb1+=1
                            if cb1==1:
                               pb1.goto(lrob[1].pos())
                               bl1+=1
                               cb1+=1
                               continue
                            if (b==1)and (cb1>0):
                               pb1_position=[lrob[bl1],lrob[bl1+n]]
                               pb1.onclick(pb1.goto(pb1_position[1].pos()))
                               #sn.delay(150)
                               bl1=bl1+n
                               if pb1_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                               elif pb1_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                               elif pb1_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                               elif pb1_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                               elif pb1_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                   sys.exit()
                                   print(NameOfBluePlayer + " Won the game")
                                       
                               if n==6:
                                   continue
                               break
              ########################################### PB2 ####################################             
                        if n==6 or cb2>0:
                            cb2+=1
                            if cb2==1:
                               pb2.goto(lrob[1].pos())
                               bl2+=1
                               cb2+=1
                               continue
                            if (b==2)and (cb2>0):
                                 pb2_position=[lrob[bl2],lrob[bl2+n]]
                                 pb2.onclick(pb2.goto(pb2_position[1].pos()))
                                 #sn.delay(150)
                                 bl2=bl2+n
                                 if pb2_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif pb2_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif pb2_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif pb2_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif pb2_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                   sys.exit()
                                   print(NameOfBluePlayer + " Won the game")
                                       
                                 if n==6:
                                   continue
                                 break
                        if n==6 or cb3>0:
                            cb3+=1
                            if cb3==1:
                               pb3.goto(lrob[1].pos())
                               bl3+=1
                               cb3+=1
                               continue
                            if (b==3)and (cb3>0):
                                 pb3_position=[lrob[bl3],lrob[bl3+n]]
                                 pb3.onclick(pb3.goto(pb3_position[1].pos()))
                                 #sn.delay(150)
                                 bl3=bl3+n
                                 if pb3_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif pb3_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif pb3_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif pb3_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif pb3_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                    sys.exit()
                                    print(NameOfBluePlayer + " Won the game")
                                       
                                 if n==6:
                                     
                                    continue
                               
                                 break
                      ######################################### PB 4 ##################################          
                        if n==6 or cb4>0:
                            cb4+=1
                            if cb4==1:
                               pb4.goto(lrob[1].pos())
                               bl4+=1
                               cb4+=1
                               continue
                            if (b==4)and (cb4>0):
                                 pb4_position=[lrob[bl4],lrob[bl4+n]]
                                 pb4.onclick(pb4.goto(pb4_position[1].pos()))
                                 #sn.delay(150)
                                 bl4=bl4+n
                                 if pb4_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif pb4_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif pb4_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif pb4_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif pb4_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                   sys.exit()
                                   print(NameOfBluePlayer + " Won the game")
                                       
                                   
                                   
                                 if n==6:
                                   continue
                                 break
                        break
                        '''if (pb1_position[1]==end):
                            print("BLUE TEAM WON")
                        break'''
                        #redroll()
            #--------------------------------------------------   YELLOW   ------------------------------------------------#        
                #def yellowroll():
                 while z<100:
                        dicenumber.clear()
                        n=int (random.randint(1,6))
                        print("yyyy")
                        dicenumber.color('yellow')
                        #lroy=[py1,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y11,y10,y9,y8,y7,end]
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        dicenumber.hideturtle()
                        
                        sn.delay(150)
                        y=eval(input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
                        if n==6 or cy1>0:
                            cy1+=1
                            if cy1==1:
                               py1.goto(lroy[1].pos())
                               ye1+=1
                               cy1+=1
                               continue
                            if (y==1)and (cy1>0):
                               py1_position=[lroy[ye1],lroy[ye1+n]]
                               py1.onclick(py1.goto(py1_position[1].pos()))
                               ye1=ye1+n
                               if py1_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                               elif py1_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                               elif py1_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                               elif py1_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                               elif py1_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif py1_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif py1_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif py1_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                   sys.exit()
                                   print(NameOfYellowPlayer + " Won the game")
                                       
                                   
                               if n==6:
                                    continue
                               break
                        if n==6 or cy2>0:
                            cy2+=1
                            if cy2==1:
                               py2.goto(lroy[1].pos())
                               ye2+=1
                               cy2+=1
                               continue
                            if (y==2)and (cy2>0):
                                 py2_position=[lroy[ye2],lroy[ye2+n]]
                                 py2.onclick(py2.goto(py2_position[1].pos()))
                                 ye2=ye2+n
                                 if py2_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif py2_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif py2_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif py2_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif py2_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif py2_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif py2_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif py2_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    sys.exit()
                                    print(NameOfYellowPlayer + " Won the game")
                                       
                                 if n==6:
                                    continue
                                 break
                        if n==6 or cy3>0:
                            cy3+=1
                            if cy3==1:
                               py3.goto(lroy[1].pos())
                               ye3+=1
                               cy3+=1
                               continue
                            if (y==3)and (cy3>0):
                                 py3_position=[lroy[ye3],lroy[ye3+n]]
                                 py3.onclick(py3.goto(py3_position[1].pos()))
                                 ye3=ye3+n
                                 if py3_position[1]== pg1_position[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif py3_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif py3_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif py3_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif py3_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif py3_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif py3_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif py3_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    sys.exit()
                                    print(NameOfYellowPlayer + " Won the game")
                                       
                                 if n==6:
                                    continue
                                 break
                        if n==6 or cy4>0:
                            cy4+=1
                            if cy4==1:
                               py4.goto(lroy[1].pos())
                               ye4+=1
                               cy4+=1
                               continue
                            if (y==4)and (cy4>0):
                                 py4_position=[lroy[ye4],lroy[ye4+n]]
                                 py4.onclick(py4.goto(py4_position[1].pos()))
                                 ye4=ye4+n
                                 if py4_position[1]== pg1_postion[1]:
                                    cg1=0
                                    ge1=0
                                    pg1.goto(lrog[0].pos())
                                    continue
                                 elif py4_position[1]== pg2_position[1]:
                                    cg2=0
                                    ge2=0
                                    pg2.goto(lrog[0].pos())
                                    continue
                                 elif py4_position[1]== pg3_position[1]:
                                    cg3=0
                                    ge3=0
                                    pg3.goto(lrog[0].pos())
                                    continue
                                 elif py4_position[1]== pg4_position[1]:
                                    cg4=0
                                    ge4=0
                                    pg4.goto(lrog[0].pos())
                                    continue
                                 elif py4_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif py4_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif py4_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif py4_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    sys.exit()
                                    print(NameOfYellowPlayer + " Won the game")
                                       
                                 if n==6:
                                    continue
                                 break
                        break
   #%^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%^^^^^^^^^^^%%%%%^^^^^^^
 #^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%^^^^^^^^^^THREE PLAYERSS^^^^^^%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^%%%%%%%^
 #^^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%
                    
def threeplayers():
            NameOfRedPlayer= input("ENTER red player name")
            NameOfBluePlayer= input("ENTER blue player name")
            NameOfYellowPlayer= input("ENTER yellow player name")
            redname=turtle.Turtle()
            redname.penup()
            redname.color("firebrick")
            redname.goto(120,210)
            redname.write(NameOfRedPlayer,font=('Arial',30))
            redname.hideturtle()
            bluename=turtle.Turtle()
            bluename.penup()
            bluename.color("navy")
            bluename.goto(120,-230)
            bluename.write(NameOfBluePlayer,font=('Arial',30))
            bluename.hideturtle()
            yellowname=turtle.Turtle()
            yellowname.penup()
            yellowname.color("darkorange")
            yellowname.goto(-190,-230)
            yellowname.write(NameOfYellowPlayer,font=('Arial',30))
            yellowname.hideturtle()
            
            pr1= turtle.Turtle()
            pr1.shape("circle")
            pr1.color("firebrick")
            pr1.penup()
            pr1.speed(10000)
            pr1.setpos(180,180)


            #pr1.write(1, font=('Arial',16), align=('center'))
            #pr1.stamp()
            #pr1.hideturtle()


            #r2
            pr2=turtle.Turtle()
            pr2.shape("square")
            pr2.color("firebrick")
            pr2.penup()
            pr2.speed(100)
            pr2.setpos(180,115)
            #r3
            pr3=turtle.Turtle()
            pr3.shape("triangle")
            pr3.color("firebrick")
            pr3.penup()
            pr3.speed(100)
            pr3.setpos(115,115)
            #r4
            pr4=turtle.Turtle()
            pr4.shape("turtle")
            pr4.color("firebrick")
            pr4.penup()
            pr4.speed(100)
            pr4.setpos(115,180)


            #PAWN OF BLUE
            #b1
            pb1= turtle.Turtle()
            pb1.shape("circle")
            pb1.color("navy")
            pb1.penup()
            pb1.speed(100)
            pb1.setpos(180,-180)
            #b2
            pb2= turtle.Turtle()
            pb2.shape("square")
            pb2.color("navy")
            pb2.penup()
            pb2.speed(100)
            pb2.setpos(180,-115)
            #b3
            pb3= turtle.Turtle()
            pb3.shape("triangle")
            pb3.color("navy")
            pb3.penup()
            pb3.speed(100)
            pb3.setpos(115,-115)
            #b4
            pb4= turtle.Turtle()
            pb4.shape("turtle")
            pb4.color("navy")
            pb4.penup()
            pb4.speed(100)
            pb4.setpos(115,-180)


            #PAWN OF YELLOW
            #y1
            py1= turtle.Turtle()
            py1.shape("circle")
            py1.color("darkorange")
            py1.penup()
            py1.speed(100)
            py1.setpos(-180,-180)
            #y2
            py2= turtle.Turtle()
            py2.shape("square")
            py2.color("darkorange")
            py2.penup()
            py2.speed(100)
            py2.setpos(-180,-115)
            #y3
            py3= turtle.Turtle()
            py3.shape("triangle")
            py3.color("darkorange")
            py3.penup()
            py3.speed(100)
            py3.setpos(-115,-115)
            #y4
            py4= turtle.Turtle()
            py4.shape("turtle")
            py4.color("darkorange")
            py4.penup()
            py4.speed(100)
            py4.setpos(-115,-180)

            ############## BOXES ##################
            r1=turtle.Turtle()
            r1.speed(100)
            r1.shape("square")
            r1.shapesize(1.4,1.5)
            r1.color("white")
            r1.penup()
            k=r1.setpos(-36,67)



            #RED TEAM COLUMN #1
            r2=turtle.Turtle()
            r2.speed(100)
            r2.shape("square")
            r2.shapesize(1.4,1.5)
            r2.color("white")
            r2.penup()
            k=r2.setpos(-36,99)

            #RED TEAM COLUMN #1
            r3=turtle.Turtle()
            r3.speed(100)
            r3.shape("square")
            r3.shapesize(1.4,1.5)
            r3.color("white")
            r3.penup()
            k=r3.setpos(-36,132)

            #RED TEAM COLUMN #1
            r4=turtle.Turtle()
            r4.speed(100)
            r4.shape("square")
            r4.shapesize(1.4,1.5)
            r4.color("red")
            r4.penup()
            k=r4.setpos(-36,164)

            #RED TEAM COLUMN #1
            r5=turtle.Turtle()
            r5.speed(100)
            r5.shape("square")
            r5.shapesize(1.4,1.5)
            r5.color("white")
            r5.penup()
            k=r5.setpos(-36,197)

            #RED TEAM COLUMN #1
            r6=turtle.Turtle()
            r6.speed(100)
            r6.shape("square")
            r6.shapesize(1.4,1.5)
            r6.color("white")
            r6.penup()
            k=r6.setpos(-36,230)

            #RED TEAM COLUMN #2
            r7=turtle.Turtle()
            r7.speed(100)
            r7.shape("square")
            r7.shapesize(1.4,1.5)
            r7.color("red")
            r7.penup()
            k=r7.setpos(-2,67)

            #RED TEAM COLUMN #2
            r8=turtle.Turtle()
            r8.speed(100)
            r8.shape("square")
            r8.shapesize(1.4,1.5)
            r8.color("red")
            r8.penup()
            k=r8.setpos(-2,99)

            #RED TEAM COLUMN #2
            r9=turtle.Turtle()
            r9.speed(100)
            r9.shape("square")
            r9.shapesize(1.4,1.5)
            r9.color("red")
            r9.penup()
            k=r9.setpos(-2,132)

            #RED TEAM COLUMN #2
            r10=turtle.Turtle()
            r10.speed(100)
            r10.shape("square")
            r10.shapesize(1.4,1.5)
            r10.color("red")
            r10.penup()
            k=r10.setpos(-2,164)

            #RED TEAM COLUMN #2
            r11=turtle.Turtle()
            r11.speed(100)
            r11.shape("square")
            r11.shapesize(1.4,1.5)
            r11.color("red")
            r11.penup()
            k=r11.setpos(-2,197)

            #RED TEAM COLUMN #2
            r12=turtle.Turtle()
            r12.speed(100)
            r12.shape("square")
            r12.shapesize(1.4,1.5)
            r12.color("white")
            r12.penup()
            k=r12.setpos(-2,230)

            #RED TEAM COLUMN #3
            r13=turtle.Turtle()
            r13.speed(100)
            r13.shape("square")
            r13.shapesize(1.4,1.5)
            r13.color("white")
            r13.penup()
            k=r13.setpos(33,67)



            #RED TEAM COLUMN #3
            r14=turtle.Turtle()
            r14.speed(100)
            r14.shape("square")
            r14.shapesize(1.4,1.5)
            r14.color("white")
            r14.penup()
            k=r14.setpos(33,99)

            #RED TEAM COLUMN #3
            r15=turtle.Turtle()
            r15.speed(100)
            r15.shape("square")
            r15.shapesize(1.4,1.5)
            r15.color("white")
            r15.penup()
            k=r15.setpos(33,132)

            #RED TEAM COLUMN #3
            r16=turtle.Turtle()
            r16.speed(100)
            r16.shape("square")
            r16.shapesize(1.4,1.5)
            r16.color("white")
            r16.penup()
            k=r16.setpos(33,164)

            #RED TEAM COLUMN #3
            r17=turtle.Turtle()
            r17.speed(100)
            r17.shape("square")
            r17.shapesize(1.4,1.5)
            r17.color("red")
            r17.penup()
            k=r17.setpos(33,197)

            #RED TEAM COLUMN #3
            r18=turtle.Turtle()
            r18.speed(100)
            r18.shape("square")
            r18.shapesize(1.4,1.5)
            r18.color("white")
            r18.penup()
            k=r18.setpos(33,230)

            ######### STOP BOXES FOR BLUE COLOR ################

            #BLUE TEAM COLUMN 1
            b1=turtle.Turtle()
            b1.speed(100)
            b1.shape("square")
            b1.shapesize(1.5,1.4)
            b1.color("white")
            b1.penup()
            k=b1.setpos(64,36)

            #BLUE TEAM COLUMN 1
            b2=turtle.Turtle()
            b2.speed(100)
            b2.shape("square")
            b2.shapesize(1.5,1.4)
            b2.color("white")
            b2.penup()
            k=b2.setpos(96,36)


            #BLUE TEAM COLUMN 1
            b3=turtle.Turtle()
            b3.speed(100)
            b3.shape("square")
            b3.shapesize(1.5,1.4)
            b3.color("white")
            b3.penup()
            k=b3.setpos(129,36)


            #BLUE TEAM COLUMN 1
            b4=turtle.Turtle()
            b4.speed(100)
            b4.shape("square")
            b4.shapesize(1.5,1.4)
            b4.color("sky blue")
            b4.penup()
            k=b4.setpos(161,36)


            #BLUE TEAM COLUMN 1
            b5=turtle.Turtle()
            b5.speed(100)
            b5.shape("square")
            b5.shapesize(1.5,1.4)
            b5.color("white")
            b5.penup()
            k=b5.setpos(194,36)


            #BLUE TEAM COLUMN 1
            b6=turtle.Turtle()
            b6.speed(100)
            b6.shape("square")
            b6.shapesize(1.5,1.4)
            b6.color("white")
            b6.penup()
            k=b6.setpos(227,36)


            #BLUE TEAM COLUMN #2
            b7=turtle.Turtle()
            b7.speed(100)
            b7.shape("square")
            b7.shapesize(1.5,1.4)
            b7.color("sky blue")
            b7.penup()
            k=b7.setpos(64,1)


            #BLUE TEAM COLUMN #2
            b8=turtle.Turtle()
            b8.speed(100)
            b8.shape("square")
            b8.shapesize(1.5,1.4)
            b8.color("sky blue")
            b8.penup()
            k=b8.setpos(96,1)


            #BLUE TEAM COLUMN #2
            b9=turtle.Turtle()
            b9.speed(100)
            b9.shape("square")
            b9.shapesize(1.5,1.4)
            b9.color("sky blue")
            b9.penup()
            k=b9.setpos(129,1)


            #BLUE TEAM COLUMN #2
            b10=turtle.Turtle()
            b10.speed(100)
            b10.shape("square")
            b10.shapesize(1.5,1.4)
            b10.color("sky blue")
            b10.penup()
            k=b10.setpos(162,1)


            #BLUE TEAM COLUMN #2
            b11=turtle.Turtle()
            b11.speed(100)
            b11.shape("square")
            b11.shapesize(1.5,1.4)
            b11.color("sky blue")
            b11.penup()
            k=b11.setpos(195,1)


            #BLUE TEAM COLUMN #2
            b12=turtle.Turtle()
            b12.speed(100)
            b12.shape("square")
            b12.shapesize(1.5,1.4)
            b12.color("white")
            b12.penup()
            k=b12.setpos(227,1)



            #BLUE TEAM COLUMN 3
            b13=turtle.Turtle()
            b13.speed(100)
            b13.shape("square")
            b13.shapesize(1.5,1.4)
            b13.color("white")
            b13.penup()
            k=b13.setpos(64,-33)


            #BLUE TEAM COLUMN 3
            b14=turtle.Turtle()
            b14.speed(100)
            b14.shape("square")
            b14.shapesize(1.5,1.4)
            b14.color("white")
            b14.penup()
            k=b14.setpos(97,-33)



            #BLUE TEAM COLUMN 3
            b15=turtle.Turtle()
            b15.speed(100)
            b15.shape("square")
            b15.shapesize(1.5,1.4)
            b15.color("white")
            b15.penup()
            k=b15.setpos(129,-33)



            #BLUE TEAM COLUMN 3
            b16=turtle.Turtle()
            b16.speed(100)
            b16.shape("square")
            b16.shapesize(1.5,1.4)
            b16.color("white")
            b16.penup()
            k=b16.setpos(161,-33)



            #BLUE TEAM COLUMN 3
            b17=turtle.Turtle()
            b17.speed(100)
            b17.shape("square")
            b17.shapesize(1.5,1.4)
            b17.color("sky blue")
            b17.penup()
            k=b17.setpos(194,-33)



            #BLUE TEAM COLUMN 3
            b18=turtle.Turtle()
            b18.speed(100)
            b18.shape("square")
            b18.shapesize(1.5,1.4)
            b18.color("white")
            b18.penup()
            k=b18.setpos(227,-33)


            #STOP BOXES OF YELLOW#######

            #yellow team column #1
            y1=turtle.Turtle()
            y1.speed(100)
            y1.shape("square")
            y1.shapesize(1.4,1.5)
            y1.color("white")
            y1.penup()
            k=y1.setpos(33,-67)



            #yellow team column #1
            y2=turtle.Turtle()
            y2.speed(100)
            y2.shape("square")
            y2.shapesize(1.4,1.5)
            y2.color("white")
            y2.penup()
            k=y2.setpos(33,-99)

            #yellow team column #1
            y3=turtle.Turtle()
            y3.speed(100)
            y3.shape("square")
            y3.shapesize(1.4,1.5)
            y3.color("white")
            y3.penup()
            k=y3.setpos(33,-132)

            #yellow team column #1
            y4=turtle.Turtle()
            y4.speed(100)
            y4.shape("square")
            y4.shapesize(1.4,1.5)
            y4.color("yellow")
            y4.penup()
            k=y4.setpos(33,-164)

            #yellow team column #1
            y5=turtle.Turtle()
            y5.speed(100)
            y5.shape("square")
            y5.shapesize(1.4,1.5)
            y5.color("white")
            y5.penup()
            k=y5.setpos(33,-197)

            #yellow team column #1
            y6=turtle.Turtle()
            y6.speed(100)
            y6.shape("square")
            y6.shapesize(1.4,1.5)
            y6.color("white")
            y6.penup()
            k=y6.setpos(33,-230)

            #yellow team column #2
            y7=turtle.Turtle()
            y7.speed(100)
            y7.shape("square")
            y7.shapesize(1.4,1.5)
            y7.color("yellow")
            y7.penup()
            k=y7.setpos(-2,-67)

            #yellow team column #2
            y8=turtle.Turtle()
            y8.speed(100)
            y8.shape("square")
            y8.shapesize(1.4,1.5)
            y8.color("yellow")
            y8.penup()
            k=y8.setpos(-2,-99)

            #yellow team column #2
            y9=turtle.Turtle()
            y9.speed(100)
            y9.shape("square")
            y9.shapesize(1.4,1.5)
            y9.color("yellow")
            y9.penup()
            k=y9.setpos(-2,-132)

            #yellow team column #2
            y10=turtle.Turtle()
            y10.speed(100)
            y10.shape("square")
            y10.shapesize(1.4,1.5)
            y10.color("yellow")
            y10.penup()
            k=y10.setpos(-2,-164)

            #yellow team column #2
            y11=turtle.Turtle()
            y11.speed(100)
            y11.shape("square")
            y11.shapesize(1.4,1.5)
            y11.color("yellow")
            y11.penup()
            k= y11.setpos(-2,-197)

            #yellow team column #2
            y12=turtle.Turtle()
            y12.speed(100)
            y12.shape("square")
            y12.shapesize(1.4,1.5)
            y12.color("white")
            y12.penup()
            k=y12.setpos(-2,-230)



            #yellow team column #3
            y13=turtle.Turtle()
            y13.speed(100)
            y13.shape("square")
            y13.shapesize(1.4,1.5)
            y13.color("white")
            y13.penup()
            k=y13.setpos(-36,-67)



            #yellow team column #3
            y14=turtle.Turtle()
            y14.speed(100)
            y14.shape("square")
            y14.shapesize(1.4,1.5)
            y14.color("white")
            y14.penup()
            k=y14.setpos(-36,-99)

            #yellow team column #3
            y15=turtle.Turtle()
            y15.speed(100)
            y15.shape("square")
            y15.shapesize(1.4,1.5)
            y15.color("white")
            y15.penup()
            k=y15.setpos(-36,-132)

            #yellow team column #3
            y16=turtle.Turtle()
            y16.speed(100)
            y16.shape("square")
            y16.shapesize(1.4,1.5)
            y16.color("white")
            y16.penup()
            k=y16.setpos(-36,-164)

            #yellow team column #3
            y17=turtle.Turtle()
            y17.speed(100)
            y17.shape("square")
            y17.shapesize(1.4,1.5)
            y17.color("yellow")
            y17.penup()
            k=y17.setpos(-36,-197)

            #yellow team column #3
            y18=turtle.Turtle()
            y18.speed(100)
            y18.shape("square")
            y18.shapesize(1.4,1.5)
            y18.color("white")
            y18.penup()
            k=y18.setpos(-36,-230)



            ########### STOP BOXES FOR GREEN ############

            #GREEN TEAM COLUMN #1
            g1=turtle.Turtle()
            g1.speed(100)
            g1.shape("square")
            g1.shapesize(1.5,1.4)
            g1.color("white")
            g1.penup()
            k=g1.setpos(-67,-33)

            #GREEN TEAM COLUMN #1
            g2=turtle.Turtle()
            g2.speed(100)
            g2.shape("square")
            g2.shapesize(1.5,1.4)
            g2.color("white")
            g2.penup()
            k=g2.setpos(-99,-33)


            #GREEN TEAM COLUMN #1
            g3=turtle.Turtle()
            g3.speed(100)
            g3.shape("square")
            g3.shapesize(1.5,1.4)
            g3.color("white")
            g3.penup()
            k=g3.setpos(-132,-33)


            #GREEN TEAM COLUMN #1
            g4=turtle.Turtle()
            g4.speed(100)
            g4.shape("square")
            g4.shapesize(1.5,1.4)
            g4.color("dark green")
            g4.penup()
            k=g4.setpos(-164,-33)


            #GREEN TEAM COLUMN #1
            g5=turtle.Turtle()
            g5.speed(100)
            g5.shape("square")
            g5.shapesize(1.5,1.4)
            g5.color("white")
            g5.penup()
            k=g5.setpos(-197,-33)


            #GREEN TEAM COLUMN #1
            g6=turtle.Turtle()
            g6.speed(100)
            g6.shape("square")
            g6.shapesize(1.5,1.4)
            g6.color("white")
            g6.penup()
            k=g6.setpos(-230,-33)


            #GREEN TEAM COLUMN #2
            g7=turtle.Turtle()
            g7.speed(100)
            g7.shape("square")
            g7.shapesize(1.5,1.4)
            g7.color("dark green")
            g7.penup()
            k=g7.setpos(-67,1)


            #GREEN TEAM COLUMN #2
            g8=turtle.Turtle()
            g8.speed(100)
            g8.shape("square")
            g8.shapesize(1.5,1.4)
            g8.color("dark green")
            g8.penup()
            k=g8.setpos(-99,1)


            #GREEN TEAM COLUMN #2
            g9=turtle.Turtle()
            g9.speed(100)
            g9.shape("square")
            g9.shapesize(1.5,1.4)
            g9.color("dark green")
            g9.penup()
            k=g9.setpos(-132,1)


            #GREEN TEAM COLUMN #2
            g10=turtle.Turtle()
            g10.speed(100)
            g10.shape("square")
            g10.shapesize(1.5,1.4)
            g10.color("dark green")
            g10.penup()
            k=g10.setpos(-164,1)


            #GREEN TEAM COLUMN #2
            g11=turtle.Turtle()
            g11.speed(100)
            g11.shape("square")
            g11.shapesize(1.5,1.4)
            g11.color("dark green")
            g11.penup()
            k=g11.setpos(-197,1)


            #GREEN TEAM COLUMN #2
            g12=turtle.Turtle()
            g12.speed(100)
            g12.shape("square")
            g12.shapesize(1.5,1.4)
            g12.color("white")
            g12.penup()
            k=g12.setpos(-230,1)




            #GREEN TEAM COLUMN #3
            g13=turtle.Turtle()
            g13.speed(100)
            g13.shape("square")
            g13.shapesize(1.5,1.4)
            g13.color("white")
            g13.penup()
            k=g13.setpos(-67,36)

            #GREEN TEAM COLUMN #3
            g14=turtle.Turtle()
            g14.speed(100)
            g14.shape("square")
            g14.shapesize(1.5,1.4)
            g14.color("white")
            g14.penup()
            k=g14.setpos(-99,36)


            #GREEN TEAM COLUMN #3
            g15=turtle.Turtle()
            g15.speed(100)
            g15.shape("square")
            g15.shapesize(1.5,1.4)
            g15.color("white")
            g15.penup()
            k=g15.setpos(-132,36)


            #GREEN TEAM COLUMN #3
            g16=turtle.Turtle()
            g16.speed(100)
            g16.shape("square")
            g16.shapesize(1.5,1.4)
            g16.color("white")
            g16.penup()
            k=g16.setpos(-164,36)


            #GREEN TEAM COLUMN #3
            g17=turtle.Turtle()
            g17.speed(100)
            g17.shape("square")
            g17.shapesize(1.5,1.4)
            g17.color("dark green")
            g17.penup()
            k=g17.setpos(-197,36)


            #GREEN TEAM COLUMN #3
            g18=turtle.Turtle()
            g18.speed(100)
            g18.shape("square")
            g18.shapesize(1.5,1.4)
            g18.color("white")
            g18.penup()
            k=g18.setpos(-230,36)

            #################################### DICE  ##############################
            ####################################       ##############################
            #lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7]
            end=turtle.Turtle()
            end.shape("square")
            end.shapesize(4,4)
            end.goto(0,0)
            '''dice=turtle.Turtle()
            dice.shape("square")
            dice.color("grey")
            dice.speed(0)
            dice.shapesize(2,4)
            dice.penup()
            dice.goto(250,-250)
            #dice.write("CLICKHERE")'''
            '''clickHere = turtle.Turtle()
            clickHere.penup()
            clickHere.goto(250,-250)
            clickHere.write("CLICK HERE")'''
                            #LOGIC OF DICE
            '''a=turtle.Turtle()
            d=turtle.Turtle()'''
            dicenumber=turtle.Turtle()
            dicenumber.hideturtle()
            #positionpr1=int(1)
            #positionpr2=int(1)
            #positionpr3=int(1)
            i=0
            re1=0
            re2=0
            re3=0
            re4=0
            ye1=0
            ye2=0
            ye3=0
            ye4=0
            gr1=0
            gr2=0
            gr3=0
            gr4=0
            bl1=0
            bl2=0
            bl3=0
            bl4=0
            cr1=0
            cr2=0
            cr3=0
            cr4=0
            cy1=0
            cy2=0
            cy3=0
            cy4=0
            cg1=0
            cg2=0
            cg3=0
            cg4=0
            cb1=0
            cb2=0
            cb3=0
            cb4=0
            turns=0
            b=0
            y=0
            r=0
            z=0
            n=0
            ################################ LISTS OF PATHS #############################################################

            lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7,end]
            lrob=[pb1,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b11,b10,b9,b8,b7,end]
            lroy=[py1,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y11,y10,y9,y8,y7,end]
            
            ####################### LISTS OF positions  ###############################################

            pr4_position=[lrop[re4],lrop[re4+n]]
            pr3_position=[lrop[re3],lrop[re3+n]]
            pr2_position=[lrop[re2],lrop[re2+n]]
            pr1_position=[lrop[re1],lrop[re1+n]]
            py4_position=[lroy[ye4],lroy[ye4+n]]
            py3_position=[lroy[ye3],lroy[ye3+n]]
            py2_position=[lroy[ye2],lroy[ye2+n]]
            py1_position=[lroy[ye1],lroy[ye1+n]]
            pb4_position=[lrob[bl4],lrob[bl4+n]]
            pb3_position=[lrob[bl3],lrob[bl3+n]]
            pb2_position=[lrob[bl2],lrob[bl2+n]]
            pb1_position=[lrob[bl1],lrob[bl1+n]]
            while z<1000:

              while z<1000:        

                        dicenumber.clear()
                        n=int(random.randint(1,6))
                        
                        #lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7,end]
                            
                            
                        print("rrrr")
                        dicenumber.color('red')
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        sn.delay(250)
                        dicenumber.hideturtle()
                        #sn.delay(250)
                        r=eval(input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
            ################################## PR1 ####################################
                        if n==6 or cr1>0:
                            cr1+=1
                            if cr1==1:
                               pr1.goto(lrop[1].pos())
                               re1+=1
                               cr1+=1
                               continue
                            if (r==1)and (cr1>0):
                               pr1_position=[lrop[re1],lrop[re1+n]]
                               pr1.onclick(pr1.goto(pr1_position[1].pos()))
                               re1=re1+n
                               if pr1_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pr1_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pr1_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pr1_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                    sys.exit()
                                    print(NameOfRedPlayer + " Won the game")
                                       
                               if n==6:
                                    continue
                               break
                           ##############################################  PR2 #######################################
                        if n==6 or cr2>0:
                            cr2+=1
                            if cr2==1:
                               pr2.goto(lrop[1].pos())
                               re2+=1
                               cr2+=1
                               continue
                            if (r==2)and (cr2>0):
                                 pr2_position=[lrop[re2],lrop[re2+n]]
                                 pr2.onclick(pr2.goto(pr2_position[1].pos()))
                                 re2=re2+n
                                 
                                 if pr2_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pr2_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pr2_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pr2_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                    sys.exit()
                                    print(NameOfRedPlayer + " Won the game")
                                 if n==6:
                                    continue
                                 break
                 ######################################  PR3 #######################################               
                        if n==6 or cr3>0:
                            cr3+=1
                            if cr3==1:
                               pr3.goto(lrop[1].pos())
                               re3+=1
                               cr3+=1
                               continue
                            if (r==3)and (cr3>0):
                                 pr3_position=[lrop[re3],lrop[re3+n]]
                                 pr3.onclick(pr1.goto(pr3_position[1].pos()))
                                 re3=re3+n
                                 
                                 if pr3_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pr3_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pr3_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pr3_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                    sys.exit()
                                    print(NameOfRedPlayer + " Won the game")
                                 if n==6:
                                    continue
                                 break
             ######################################## PR4 ####################################
                        if n==6 or cr4>0:
                            cr4+=1
                            
                                
                            if cr4==1:
                               pr4.goto(lrop[1].pos())
                               re4+=1
                               cr4+=1
                               continue
                           
                             
                            if (r==4)and (cr4>0):
                                 pr4_position=[lrop[re4],lrop[re4+n]]
                                 pr4.onclick(pr1.goto(pr4_position[1].pos()))
                                 re4=re4+n
                                 
                                 if pr4_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pr4_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pr4_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pr4_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                    sys.exit()
                                    print(NameOfRedPlayer + " Won the game")
                                 if n==6:
                                    continue
                                 break
                            
                        break   
            #-----------------------------------------  BLUE   -----------------------------------------#          
                  
              while(z<100):
                        dicenumber.clear()
                        n=int (random.randint(1,6))
                        #lrob=[pb1,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b11,b10,b9,b8,b7,end]
                        print("bbbb")
                        dicenumber.color('blue')
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        dicenumber.hideturtle()
                        b=eval (input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
            ########################################################  PB1  ################################################
                        if n==6 or cb1>0:
                            cb1+=1
                            if cb1==1:
                               pb1.goto(lrob[1].pos())
                               bl1+=1
                               cb1+=1
                               continue
                            if (b==1)and (cb1>0):
                               pb1_position=[lrob[bl1],lrob[bl1+n]]
                               pb1.onclick(pb1.goto(pb1_position[1].pos()))
                               #sn.delay(150)
                               bl1=bl1+n
                               
                               if pb1_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                               elif pb1_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                    print(NameOfBluePlayer + " Won the game")
                                    sys.exit()
                                    
                               if n==6:
                                   continue
                               break
              ########################################### PB2 ####################################             
                        if n==6 or cb2>0:
                            cb2+=1
                            if cb2==1:
                               pb2.goto(lrob[1].pos())
                               bl2+=1
                               cb2+=1
                               continue
                            if (b==2)and (cb2>0):
                                 pb2_position=[lrob[bl2],lrob[bl2+n]]
                                 pb2.onclick(pb2.goto(pb2_position[1].pos()))
                                 #sn.delay(150)
                                 bl2=bl2+n
                                 
                                 if pb2_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 elif pb2_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                    print(NameOfBluePlayer + " Won the game")
                                    sys.exit()
                                 if n==6:
                                   continue
                                 break
                        if n==6 or cb3>0:
                            cb3+=1
                            if cb3==1:
                               pb3.goto(lrob[1].pos())
                               bl3+=1
                               cb3+=1
                               continue
                            if (b==3)and (cb3>0):
                                 pb3_position=[lrob[bl3],lrob[bl3+n]]
                                 pb3.onclick(pb3.goto(pb3_position[1].pos()))
                                 #sn.delay(150)
                                 bl3=bl3+n
                                 
                                 if pb3_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 elif pb3_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                    print(NameOfBluePlayer + " Won the game")
                                    sys.exit()
                                 if n==6:
                                     
                                    continue
                               
                                 break
                      ######################################### PB 4 ##################################          
                        if n==6 or cb4>0:
                            cb4+=1
                            if cb4==1:
                               pb4.goto(lrob[1].pos())
                               bl4+=1
                               cb4+=1
                               continue
                            if (b==4)and (cb4>0):
                                 pb4_position=[lrob[bl4],lrob[bl4+n]]
                                 pb4.onclick(pb4.goto(pb4_position[1].pos()))
                                 #sn.delay(150)
                                 bl4=bl4+n
                                 
                                 if pb4_position[1]== py1_position[1]:
                                    cy1=0
                                    ye1=0
                                    py1.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== py2_position[1]:
                                    cy2=0
                                    ye2=0
                                    py2.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== py3_position[1]:
                                    cy3=0
                                    ye3=0
                                    py3.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== py4_position[1]:
                                    cy4=0
                                    ye4=0
                                    py4.goto(lroy[0].pos())
                                    continue
                                 elif pb4_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  bl1 >= 58 or bl2>=58 or bl3>=58 or bl4>=58  :
                                    print(NameOfBluePlayer + " Won the game")
                                    sys.exit()
                                 if n==6:
                                   continue
                                 break
                        break
                        '''if (pb1_position[1]==end):
                            print("BLUE TEAM WON")
                        break'''
                        #redroll()
            #--------------------------------------------------   YELLOW   ------------------------------------------------#        
                #def yellowroll():
              while z<100:
                        dicenumber.clear()
                        n=int (random.randint(1,6))
                        print("yyyy")
                        dicenumber.color('yellow')
                        #lroy=[py1,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y11,y10,y9,y8,y7,end]
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        dicenumber.hideturtle()
                        
                        sn.delay(150)
                        y=eval(input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
                        if n==6 or cy1>0:
                            cy1+=1
                            if cy1==1:
                               py1.goto(lroy[1].pos())
                               ye1+=1
                               cy1+=1
                               continue
                            if (y==1)and (cy1>0):
                               py1_position=[lroy[ye1],lroy[ye1+n]]
                               py1.onclick(py1.goto(py1_position[1].pos()))
                               ye1=ye1+n
                               
                               if py1_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               elif py1_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif py1_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif py1_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif py1_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    print(NameOfYellowPlayer + " Won the game")
                                    sys.exit() 
                               if n==6:
                                    continue
                               break
                        if n==6 or cy2>0:
                            cy2+=1
                            if cy2==1:
                               py2.goto(lroy[1].pos())
                               ye2+=1
                               cy2+=1
                               continue
                            if (y==2)and (cy2>0):
                                 py2_position=[lroy[ye2],lroy[ye2+n]]
                                 py2.onclick(py2.goto(py2_position[1].pos()))
                                 ye2=ye2+n
                                 if py2_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif py2_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif py2_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif py2_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif py2_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    print(NameOfYellowPlayer + " Won the game")
                                    sys.exit() 
                                 if n==6:
                                    continue
                                 break
                        if n==6 or cy3>0:
                            cy3+=1
                            if cy3==1:
                               py3.goto(lroy[1].pos())
                               ye3+=1
                               cy3+=1
                               continue
                            if (y==3)and (cy3>0):
                                 py3_position=[lroy[ye3],lroy[ye3+n]]
                                 py3.onclick(py3.goto(py3_position[1].pos()))
                                 ye3=ye3+n
                                 if py3_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif py3_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif py3_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif py3_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif py3_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    print(NameOfYellowPlayer + " Won the game")
                                    sys.exit() 
                                 if n==6:
                                    continue
                                 break
                        if n==6 or cy4>0:
                            cy4+=1
                            if cy4==1:
                               py4.goto(lroy[1].pos())
                               ye4+=1
                               cy4+=1
                               continue
                            if (y==4)and (cy4>0):
                                 py4_position=[lroy[ye4],lroy[ye4+n]]
                                 py4.onclick(py4.goto(py4_position[1].pos()))
                                 ye4=ye4+n
                                 
                                 if py4_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 elif py4_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif py4_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif py4_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif py4_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if  ye1 >= 58 or ye2>=58 or ye3>=58 or ye4>=58  :
                                    print(NameOfYellowPlayer + " Won the game")
                                    sys.exit() 
                                 if n==6:
                                    continue
                                 break
                        break
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^$$$$$$$$$$$$$$$$$$$$%%%%$$$$$$%$%$%$%%$%
#^^^^^^^^^^^^^^^^^^^^^^^^^^^TWO PLAYERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                   
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def twoplayers():
            NameOfRedPlayer= input("ENTER red player name")
            NameOfBluePlayer= input("ENTER blue player name")
            redname=turtle.Turtle()
            redname.penup()
            redname.color("firebrick")
            redname.goto(120,210)
            redname.write(NameOfRedPlayer,font=('Arial',30))
            redname.hideturtle()
            bluename=turtle.Turtle()
            bluename.penup()
            bluename.color("navy")
            bluename.goto(120,-230)
            bluename.write(NameOfBluePlayer,font=('Arial',30))
            bluename.hideturtle()
            
            pr1= turtle.Turtle()
            pr1.shape("circle")
            pr1.color("firebrick")
            pr1.penup()
            pr1.speed(10000)
            pr1.setpos(180,180)


            #pr1.write(1, font=('Arial',16), align=('center'))
            #pr1.stamp()
            #pr1.hideturtle()


            #r2
            pr2=turtle.Turtle()
            pr2.shape("square")
            pr2.color("firebrick")
            pr2.penup()
            pr2.speed(100)
            pr2.setpos(180,115)
            #r3
            pr3=turtle.Turtle()
            pr3.shape("triangle")
            pr3.color("firebrick")
            pr3.penup()
            pr3.speed(100)
            pr3.setpos(115,115)
            #r4
            pr4=turtle.Turtle()
            pr4.shape("turtle")
            pr4.color("firebrick")
            pr4.penup()
            pr4.speed(100)
            pr4.setpos(115,180)


            #PAWN OF BLUE
            #b1
            pb1= turtle.Turtle()
            pb1.shape("circle")
            pb1.color("navy")
            pb1.penup()
            pb1.speed(100)
            pb1.setpos(180,-180)
            #b2
            pb2= turtle.Turtle()
            pb2.shape("square")
            pb2.color("navy")
            pb2.penup()
            pb2.speed(100)
            pb2.setpos(180,-115)
            #b3
            pb3= turtle.Turtle()
            pb3.shape("triangle")
            pb3.color("navy")
            pb3.penup()
            pb3.speed(100)
            pb3.setpos(115,-115)
            #b4
            pb4= turtle.Turtle()
            pb4.shape("turtle")
            pb4.color("navy")
            pb4.penup()
            pb4.speed(100)
            pb4.setpos(115,-180)


            
            ############## BOXES ##################
            r1=turtle.Turtle()
            r1.speed(100)
            r1.shape("square")
            r1.shapesize(1.4,1.5)
            r1.color("white")
            r1.penup()
            k=r1.setpos(-36,67)



            #RED TEAM COLUMN #1
            r2=turtle.Turtle()
            r2.speed(100)
            r2.shape("square")
            r2.shapesize(1.4,1.5)
            r2.color("white")
            r2.penup()
            k=r2.setpos(-36,99)

            #RED TEAM COLUMN #1
            r3=turtle.Turtle()
            r3.speed(100)
            r3.shape("square")
            r3.shapesize(1.4,1.5)
            r3.color("white")
            r3.penup()
            k=r3.setpos(-36,132)

            #RED TEAM COLUMN #1
            r4=turtle.Turtle()
            r4.speed(100)
            r4.shape("square")
            r4.shapesize(1.4,1.5)
            r4.color("red")
            r4.penup()
            k=r4.setpos(-36,164)

            #RED TEAM COLUMN #1
            r5=turtle.Turtle()
            r5.speed(100)
            r5.shape("square")
            r5.shapesize(1.4,1.5)
            r5.color("white")
            r5.penup()
            k=r5.setpos(-36,197)

            #RED TEAM COLUMN #1
            r6=turtle.Turtle()
            r6.speed(100)
            r6.shape("square")
            r6.shapesize(1.4,1.5)
            r6.color("white")
            r6.penup()
            k=r6.setpos(-36,230)

            #RED TEAM COLUMN #2
            r7=turtle.Turtle()
            r7.speed(100)
            r7.shape("square")
            r7.shapesize(1.4,1.5)
            r7.color("red")
            r7.penup()
            k=r7.setpos(-2,67)

            #RED TEAM COLUMN #2
            r8=turtle.Turtle()
            r8.speed(100)
            r8.shape("square")
            r8.shapesize(1.4,1.5)
            r8.color("red")
            r8.penup()
            k=r8.setpos(-2,99)

            #RED TEAM COLUMN #2
            r9=turtle.Turtle()
            r9.speed(100)
            r9.shape("square")
            r9.shapesize(1.4,1.5)
            r9.color("red")
            r9.penup()
            k=r9.setpos(-2,132)

            #RED TEAM COLUMN #2
            r10=turtle.Turtle()
            r10.speed(100)
            r10.shape("square")
            r10.shapesize(1.4,1.5)
            r10.color("red")
            r10.penup()
            k=r10.setpos(-2,164)

            #RED TEAM COLUMN #2
            r11=turtle.Turtle()
            r11.speed(100)
            r11.shape("square")
            r11.shapesize(1.4,1.5)
            r11.color("red")
            r11.penup()
            k=r11.setpos(-2,197)

            #RED TEAM COLUMN #2
            r12=turtle.Turtle()
            r12.speed(100)
            r12.shape("square")
            r12.shapesize(1.4,1.5)
            r12.color("white")
            r12.penup()
            k=r12.setpos(-2,230)

            #RED TEAM COLUMN #3
            r13=turtle.Turtle()
            r13.speed(100)
            r13.shape("square")
            r13.shapesize(1.4,1.5)
            r13.color("white")
            r13.penup()
            k=r13.setpos(33,67)



            #RED TEAM COLUMN #3
            r14=turtle.Turtle()
            r14.speed(100)
            r14.shape("square")
            r14.shapesize(1.4,1.5)
            r14.color("white")
            r14.penup()
            k=r14.setpos(33,99)

            #RED TEAM COLUMN #3
            r15=turtle.Turtle()
            r15.speed(100)
            r15.shape("square")
            r15.shapesize(1.4,1.5)
            r15.color("white")
            r15.penup()
            k=r15.setpos(33,132)

            #RED TEAM COLUMN #3
            r16=turtle.Turtle()
            r16.speed(100)
            r16.shape("square")
            r16.shapesize(1.4,1.5)
            r16.color("white")
            r16.penup()
            k=r16.setpos(33,164)

            #RED TEAM COLUMN #3
            r17=turtle.Turtle()
            r17.speed(100)
            r17.shape("square")
            r17.shapesize(1.4,1.5)
            r17.color("red")
            r17.penup()
            k=r17.setpos(33,197)

            #RED TEAM COLUMN #3
            r18=turtle.Turtle()
            r18.speed(100)
            r18.shape("square")
            r18.shapesize(1.4,1.5)
            r18.color("white")
            r18.penup()
            k=r18.setpos(33,230)

            ######### STOP BOXES FOR BLUE COLOR ################

            #BLUE TEAM COLUMN 1
            b1=turtle.Turtle()
            b1.speed(100)
            b1.shape("square")
            b1.shapesize(1.5,1.4)
            b1.color("white")
            b1.penup()
            k=b1.setpos(64,36)

            #BLUE TEAM COLUMN 1
            b2=turtle.Turtle()
            b2.speed(100)
            b2.shape("square")
            b2.shapesize(1.5,1.4)
            b2.color("white")
            b2.penup()
            k=b2.setpos(96,36)


            #BLUE TEAM COLUMN 1
            b3=turtle.Turtle()
            b3.speed(100)
            b3.shape("square")
            b3.shapesize(1.5,1.4)
            b3.color("white")
            b3.penup()
            k=b3.setpos(129,36)


            #BLUE TEAM COLUMN 1
            b4=turtle.Turtle()
            b4.speed(100)
            b4.shape("square")
            b4.shapesize(1.5,1.4)
            b4.color("sky blue")
            b4.penup()
            k=b4.setpos(161,36)


            #BLUE TEAM COLUMN 1
            b5=turtle.Turtle()
            b5.speed(100)
            b5.shape("square")
            b5.shapesize(1.5,1.4)
            b5.color("white")
            b5.penup()
            k=b5.setpos(194,36)


            #BLUE TEAM COLUMN 1
            b6=turtle.Turtle()
            b6.speed(100)
            b6.shape("square")
            b6.shapesize(1.5,1.4)
            b6.color("white")
            b6.penup()
            k=b6.setpos(227,36)


            #BLUE TEAM COLUMN #2
            b7=turtle.Turtle()
            b7.speed(100)
            b7.shape("square")
            b7.shapesize(1.5,1.4)
            b7.color("sky blue")
            b7.penup()
            k=b7.setpos(64,1)


            #BLUE TEAM COLUMN #2
            b8=turtle.Turtle()
            b8.speed(100)
            b8.shape("square")
            b8.shapesize(1.5,1.4)
            b8.color("sky blue")
            b8.penup()
            k=b8.setpos(96,1)


            #BLUE TEAM COLUMN #2
            b9=turtle.Turtle()
            b9.speed(100)
            b9.shape("square")
            b9.shapesize(1.5,1.4)
            b9.color("sky blue")
            b9.penup()
            k=b9.setpos(129,1)


            #BLUE TEAM COLUMN #2
            b10=turtle.Turtle()
            b10.speed(100)
            b10.shape("square")
            b10.shapesize(1.5,1.4)
            b10.color("sky blue")
            b10.penup()
            k=b10.setpos(162,1)


            #BLUE TEAM COLUMN #2
            b11=turtle.Turtle()
            b11.speed(100)
            b11.shape("square")
            b11.shapesize(1.5,1.4)
            b11.color("sky blue")
            b11.penup()
            k=b11.setpos(195,1)


            #BLUE TEAM COLUMN #2
            b12=turtle.Turtle()
            b12.speed(100)
            b12.shape("square")
            b12.shapesize(1.5,1.4)
            b12.color("white")
            b12.penup()
            k=b12.setpos(227,1)



            #BLUE TEAM COLUMN 3
            b13=turtle.Turtle()
            b13.speed(100)
            b13.shape("square")
            b13.shapesize(1.5,1.4)
            b13.color("white")
            b13.penup()
            k=b13.setpos(64,-33)


            #BLUE TEAM COLUMN 3
            b14=turtle.Turtle()
            b14.speed(100)
            b14.shape("square")
            b14.shapesize(1.5,1.4)
            b14.color("white")
            b14.penup()
            k=b14.setpos(97,-33)



            #BLUE TEAM COLUMN 3
            b15=turtle.Turtle()
            b15.speed(100)
            b15.shape("square")
            b15.shapesize(1.5,1.4)
            b15.color("white")
            b15.penup()
            k=b15.setpos(129,-33)



            #BLUE TEAM COLUMN 3
            b16=turtle.Turtle()
            b16.speed(100)
            b16.shape("square")
            b16.shapesize(1.5,1.4)
            b16.color("white")
            b16.penup()
            k=b16.setpos(161,-33)



            #BLUE TEAM COLUMN 3
            b17=turtle.Turtle()
            b17.speed(100)
            b17.shape("square")
            b17.shapesize(1.5,1.4)
            b17.color("sky blue")
            b17.penup()
            k=b17.setpos(194,-33)



            #BLUE TEAM COLUMN 3
            b18=turtle.Turtle()
            b18.speed(100)
            b18.shape("square")
            b18.shapesize(1.5,1.4)
            b18.color("white")
            b18.penup()
            k=b18.setpos(227,-33)


            #STOP BOXES OF YELLOW#######

            #yellow team column #1
            y1=turtle.Turtle()
            y1.speed(100)
            y1.shape("square")
            y1.shapesize(1.4,1.5)
            y1.color("white")
            y1.penup()
            k=y1.setpos(33,-67)



            #yellow team column #1
            y2=turtle.Turtle()
            y2.speed(100)
            y2.shape("square")
            y2.shapesize(1.4,1.5)
            y2.color("white")
            y2.penup()
            k=y2.setpos(33,-99)

            #yellow team column #1
            y3=turtle.Turtle()
            y3.speed(100)
            y3.shape("square")
            y3.shapesize(1.4,1.5)
            y3.color("white")
            y3.penup()
            k=y3.setpos(33,-132)

            #yellow team column #1
            y4=turtle.Turtle()
            y4.speed(100)
            y4.shape("square")
            y4.shapesize(1.4,1.5)
            y4.color("yellow")
            y4.penup()
            k=y4.setpos(33,-164)

            #yellow team column #1
            y5=turtle.Turtle()
            y5.speed(100)
            y5.shape("square")
            y5.shapesize(1.4,1.5)
            y5.color("white")
            y5.penup()
            k=y5.setpos(33,-197)

            #yellow team column #1
            y6=turtle.Turtle()
            y6.speed(100)
            y6.shape("square")
            y6.shapesize(1.4,1.5)
            y6.color("white")
            y6.penup()
            k=y6.setpos(33,-230)

            #yellow team column #2
            y7=turtle.Turtle()
            y7.speed(100)
            y7.shape("square")
            y7.shapesize(1.4,1.5)
            y7.color("yellow")
            y7.penup()
            k=y7.setpos(-2,-67)

            #yellow team column #2
            y8=turtle.Turtle()
            y8.speed(100)
            y8.shape("square")
            y8.shapesize(1.4,1.5)
            y8.color("yellow")
            y8.penup()
            k=y8.setpos(-2,-99)

            #yellow team column #2
            y9=turtle.Turtle()
            y9.speed(100)
            y9.shape("square")
            y9.shapesize(1.4,1.5)
            y9.color("yellow")
            y9.penup()
            k=y9.setpos(-2,-132)

            #yellow team column #2
            y10=turtle.Turtle()
            y10.speed(100)
            y10.shape("square")
            y10.shapesize(1.4,1.5)
            y10.color("yellow")
            y10.penup()
            k=y10.setpos(-2,-164)

            #yellow team column #2
            y11=turtle.Turtle()
            y11.speed(100)
            y11.shape("square")
            y11.shapesize(1.4,1.5)
            y11.color("yellow")
            y11.penup()
            k= y11.setpos(-2,-197)

            #yellow team column #2
            y12=turtle.Turtle()
            y12.speed(100)
            y12.shape("square")
            y12.shapesize(1.4,1.5)
            y12.color("white")
            y12.penup()
            k=y12.setpos(-2,-230)



            #yellow team column #3
            y13=turtle.Turtle()
            y13.speed(100)
            y13.shape("square")
            y13.shapesize(1.4,1.5)
            y13.color("white")
            y13.penup()
            k=y13.setpos(-36,-67)



            #yellow team column #3
            y14=turtle.Turtle()
            y14.speed(100)
            y14.shape("square")
            y14.shapesize(1.4,1.5)
            y14.color("white")
            y14.penup()
            k=y14.setpos(-36,-99)

            #yellow team column #3
            y15=turtle.Turtle()
            y15.speed(100)
            y15.shape("square")
            y15.shapesize(1.4,1.5)
            y15.color("white")
            y15.penup()
            k=y15.setpos(-36,-132)

            #yellow team column #3
            y16=turtle.Turtle()
            y16.speed(100)
            y16.shape("square")
            y16.shapesize(1.4,1.5)
            y16.color("white")
            y16.penup()
            k=y16.setpos(-36,-164)

            #yellow team column #3
            y17=turtle.Turtle()
            y17.speed(100)
            y17.shape("square")
            y17.shapesize(1.4,1.5)
            y17.color("yellow")
            y17.penup()
            k=y17.setpos(-36,-197)

            #yellow team column #3
            y18=turtle.Turtle()
            y18.speed(100)
            y18.shape("square")
            y18.shapesize(1.4,1.5)
            y18.color("white")
            y18.penup()
            k=y18.setpos(-36,-230)



            ########### STOP BOXES FOR GREEN ############

            #GREEN TEAM COLUMN #1
            g1=turtle.Turtle()
            g1.speed(100)
            g1.shape("square")
            g1.shapesize(1.5,1.4)
            g1.color("white")
            g1.penup()
            k=g1.setpos(-67,-33)

            #GREEN TEAM COLUMN #1
            g2=turtle.Turtle()
            g2.speed(100)
            g2.shape("square")
            g2.shapesize(1.5,1.4)
            g2.color("white")
            g2.penup()
            k=g2.setpos(-99,-33)


            #GREEN TEAM COLUMN #1
            g3=turtle.Turtle()
            g3.speed(100)
            g3.shape("square")
            g3.shapesize(1.5,1.4)
            g3.color("white")
            g3.penup()
            k=g3.setpos(-132,-33)


            #GREEN TEAM COLUMN #1
            g4=turtle.Turtle()
            g4.speed(100)
            g4.shape("square")
            g4.shapesize(1.5,1.4)
            g4.color("dark green")
            g4.penup()
            k=g4.setpos(-164,-33)


            #GREEN TEAM COLUMN #1
            g5=turtle.Turtle()
            g5.speed(100)
            g5.shape("square")
            g5.shapesize(1.5,1.4)
            g5.color("white")
            g5.penup()
            k=g5.setpos(-197,-33)


            #GREEN TEAM COLUMN #1
            g6=turtle.Turtle()
            g6.speed(100)
            g6.shape("square")
            g6.shapesize(1.5,1.4)
            g6.color("white")
            g6.penup()
            k=g6.setpos(-230,-33)


            #GREEN TEAM COLUMN #2
            g7=turtle.Turtle()
            g7.speed(100)
            g7.shape("square")
            g7.shapesize(1.5,1.4)
            g7.color("dark green")
            g7.penup()
            k=g7.setpos(-67,1)


            #GREEN TEAM COLUMN #2
            g8=turtle.Turtle()
            g8.speed(100)
            g8.shape("square")
            g8.shapesize(1.5,1.4)
            g8.color("dark green")
            g8.penup()
            k=g8.setpos(-99,1)


            #GREEN TEAM COLUMN #2
            g9=turtle.Turtle()
            g9.speed(100)
            g9.shape("square")
            g9.shapesize(1.5,1.4)
            g9.color("dark green")
            g9.penup()
            k=g9.setpos(-132,1)


            #GREEN TEAM COLUMN #2
            g10=turtle.Turtle()
            g10.speed(100)
            g10.shape("square")
            g10.shapesize(1.5,1.4)
            g10.color("dark green")
            g10.penup()
            k=g10.setpos(-164,1)


            #GREEN TEAM COLUMN #2
            g11=turtle.Turtle()
            g11.speed(100)
            g11.shape("square")
            g11.shapesize(1.5,1.4)
            g11.color("dark green")
            g11.penup()
            k=g11.setpos(-197,1)


            #GREEN TEAM COLUMN #2
            g12=turtle.Turtle()
            g12.speed(100)
            g12.shape("square")
            g12.shapesize(1.5,1.4)
            g12.color("white")
            g12.penup()
            k=g12.setpos(-230,1)




            #GREEN TEAM COLUMN #3
            g13=turtle.Turtle()
            g13.speed(100)
            g13.shape("square")
            g13.shapesize(1.5,1.4)
            g13.color("white")
            g13.penup()
            k=g13.setpos(-67,36)

            #GREEN TEAM COLUMN #3
            g14=turtle.Turtle()
            g14.speed(100)
            g14.shape("square")
            g14.shapesize(1.5,1.4)
            g14.color("white")
            g14.penup()
            k=g14.setpos(-99,36)


            #GREEN TEAM COLUMN #3
            g15=turtle.Turtle()
            g15.speed(100)
            g15.shape("square")
            g15.shapesize(1.5,1.4)
            g15.color("white")
            g15.penup()
            k=g15.setpos(-132,36)


            #GREEN TEAM COLUMN #3
            g16=turtle.Turtle()
            g16.speed(100)
            g16.shape("square")
            g16.shapesize(1.5,1.4)
            g16.color("white")
            g16.penup()
            k=g16.setpos(-164,36)


            #GREEN TEAM COLUMN #3
            g17=turtle.Turtle()
            g17.speed(100)
            g17.shape("square")
            g17.shapesize(1.5,1.4)
            g17.color("dark green")
            g17.penup()
            k=g17.setpos(-197,36)


            #GREEN TEAM COLUMN #3
            g18=turtle.Turtle()
            g18.speed(100)
            g18.shape("square")
            g18.shapesize(1.5,1.4)
            g18.color("white")
            g18.penup()
            k=g18.setpos(-230,36)

            #################################### DICE  ##############################
            ####################################       ##############################
            #lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7]
            end=turtle.Turtle()
            end.shape("square")
            end.shapesize(4,4)
            end.goto(0,0)
            '''dice=turtle.Turtle()
            dice.shape("square")
            dice.color("grey")
            dice.speed(0)
            dice.shapesize(2,4)
            dice.penup()
            dice.goto(250,-250)
            #dice.write("CLICKHERE")'''
            '''clickHere = turtle.Turtle()
            clickHere.penup()
            clickHere.goto(250,-250)
            clickHere.write("CLICK HERE")'''
                            #LOGIC OF DICE
            '''a=turtle.Turtle()
            d=turtle.Turtle()'''
            dicenumber=turtle.Turtle()
            dicenumber.hideturtle()
            #positionpr1=int(1)
            #positionpr2=int(1)
            #positionpr3=int(1)
            i=0
            re1=0
            re2=0
            re3=0
            re4=0
            ye1=0
            ye2=0
            ye3=0
            ye4=0
            gr1=0
            gr2=0
            gr3=0
            gr4=0
            bl1=0
            bl2=0
            bl3=0
            bl4=0
            cr1=0
            cr2=0
            cr3=0
            cr4=0
            cy1=0
            cy2=0
            cy3=0
            cy4=0
            cg1=0
            cg2=0
            cg3=0
            cg4=0
            cb1=0
            cb2=0
            cb3=0
            cb4=0
            turns=0
            b=0
            y=0
            r=0
            z=0
            n=0
            ################################ LISTS OF PATHS #############################################################

            lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7,end]
            lrob=[pb1,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b11,b10,b9,b8,b7,end]
           
            
            ####################### LISTS OF positions  ###############################################

            pr4_position=[lrop[re4],lrop[re4+n]]
            pr3_position=[lrop[re3],lrop[re3+n]]
            pr2_position=[lrop[re2],lrop[re2+n]]
            pr1_position=[lrop[re1],lrop[re1+n]]
            pb4_position=[lrob[bl4],lrob[bl4+n]]
            pb3_position=[lrob[bl3],lrob[bl3+n]]
            pb2_position=[lrob[bl2],lrob[bl2+n]]
            pb1_position=[lrob[bl1],lrob[bl1+n]]
            while z<1000:

              while z<1000:        

                        dicenumber.clear()
                        n=int(random.randint(1,6))
                        
                        #lrop=[pr1,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7,end]
                            
                            
                        print("rrrr")
                        dicenumber.color('red')
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        sn.delay(250)
                        dicenumber.hideturtle()
                        #sn.delay(250)
                        r=eval(input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
            ################################## PR1 ####################################
                        if n==6 or cr1>0:
                            cr1+=1
                            if cr1==1:
                               pr1.goto(lrop[1].pos())
                               re1+=1
                               cr1+=1
                               continue
                            if (r==1)and (cr1>0):
                               pr1_position=[lrop[re1],lrop[re1+n]]
                               pr1.onclick(pr1.goto(pr1_position[1].pos()))
                               re1=re1+n
                               if pr1_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                               elif pr1_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                               if  re1 >= 58 or re2>=58 or re3>=58 or re4>=58  :
                                    print(NameOfRedPlayer + " Won the game")
                                    sys.exit()  
                              
                               if n==6:
                                    continue
                               break
                           ##############################################  PR2 #######################################
                        if n==6 or cr2>0:
                            cr2+=1
                            if cr2==1:
                               pr2.goto(lrop[1].pos())
                               re2+=1
                               cr2+=1
                               continue
                            if (r==2)and (cr2>0):
                                 pr2_position=[lrop[re2],lrop[re2+n]]
                                 pr2.onclick(pr2.goto(pr2_position[1].pos()))
                                 re2=re2+n
                                 
                                 if pr2_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr2_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 if n==6:
                                    continue
                                 break
                 ######################################  PR3 #######################################               
                        if n==6 or cr3>0:
                            cr3+=1
                            if cr3==1:
                               pr3.goto(lrop[1].pos())
                               re3+=1
                               cr3+=1
                               continue
                            if (r==3)and (cr3>0):
                                 pr3_position=[lrop[re3],lrop[re3+n]]
                                 pr3.onclick(pr1.goto(pr3_position[1].pos()))
                                 re3=re3+n
                                 
                                 if pr3_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr3_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 
                                 if n==6:
                                    continue
                                 break
             ######################################## PR4 ####################################
                        if n==6 or cr4>0:
                            cr4+=1
                            
                                
                            if cr4==1:
                               pr4.goto(lrop[1].pos())
                               re4+=1
                               cr4+=1
                               continue
                           
                             
                            if (r==4)and (cr4>0):
                                 pr4_position=[lrop[re4],lrop[re4+n]]
                                 pr4.onclick(pr1.goto(pr4_position[1].pos()))
                                 re4=re4+n
                                 
                                 if pr4_position[1]== pb1_position[1]:
                                    cb1=0
                                    bl1=0
                                    pb1.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb2_position[1]:
                                    cb2=0
                                    bl2=0
                                    pb2.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb3_position[1]:
                                    cb3=0
                                    bl3=0
                                    pb3.goto(lrob[0].pos())
                                    continue
                                 elif pr4_position[1]== pb4_position[1]:
                                    cb4=0
                                    bl4=0
                                    pb4.goto(lrob[0].pos())
                                    continue
                                 
                                 if n==6:
                                    continue
                                 break
                            
                        break   
            #-----------------------------------------  BLUE   -----------------------------------------#          
                  
              while(z<100):
                        dicenumber.clear()
                        n=int (random.randint(1,6))
                        #lrob=[pb1,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r18,r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b11,b10,b9,b8,b7,end]
                        print("bbbb")
                        dicenumber.color('blue')
                        style = ('Courier', 30, 'italic')
                        dicenumber.penup()
                        dicenumber.goto(0,-22)
                        
                        dicenumber.write(n, font=('Arial',30), align=('center'))
                        dicenumber.hideturtle()
                        b=eval (input("enter 1/2/3/4 if uh want to move circle/square/triangle/turtle respectively"))
            ########################################################  PB1  ################################################
                        if n==6 or cb1>0:
                            cb1+=1
                            if cb1==1:
                               pb1.goto(lrob[1].pos())
                               bl1+=1
                               cb1+=1
                               continue
                            if (b==1)and (cb1>0):
                               pb1_position=[lrob[bl1],lrob[bl1+n]]
                               pb1.onclick(pb1.goto(pb1_position[1].pos()))
                               #sn.delay(150)
                               bl1=bl1+n
                               
                               if pb1_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                               elif pb1_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                               if n==6:
                                   continue
                               break
              ########################################### PB2 ####################################             
                        if n==6 or cb2>0:
                            cb2+=1
                            if cb2==1:
                               pb2.goto(lrob[1].pos())
                               bl2+=1
                               cb2+=1
                               continue
                            if (b==2)and (cb2>0):
                                 pb2_position=[lrob[bl2],lrob[bl2+n]]
                                 pb2.onclick(pb2.goto(pb2_position[1].pos()))
                                 #sn.delay(150)
                                 bl2=bl2+n
                                 
                                 if pb2_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb2_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if n==6:
                                   continue
                                 break
                        if n==6 or cb3>0:
                            cb3+=1
                            if cb3==1:
                               pb3.goto(lrob[1].pos())
                               bl3+=1
                               cb3+=1
                               continue
                            if (b==3)and (cb3>0):
                                 pb3_position=[lrob[bl3],lrob[bl3+n]]
                                 pb3.onclick(pb3.goto(pb3_position[1].pos()))
                                 #sn.delay(150)
                                 bl3=bl3+n
                                 
                                 if pb3_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb3_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if n==6:
                                     
                                    continue
                               
                                 break
                      ######################################### PB 4 ##################################          
                        if n==6 or cb4>0:
                            cb4+=1
                            if cb4==1:
                               pb4.goto(lrob[1].pos())
                               bl4+=1
                               cb4+=1
                               continue
                            if (b==4)and (cb4>0):
                                 pb4_position=[lrob[bl4],lrob[bl4+n]]
                                 pb4.onclick(pb4.goto(pb4_position[1].pos()))
                                 #sn.delay(150)
                                 bl4=bl4+n
                                 
                                
                                 if pb4_position[1]== pr1_position[1]:
                                    cr1=0
                                    re1=0
                                    pr1.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr2_position[1]:
                                    cr2=0
                                    re2=0
                                    pr2.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr3_position[1]:
                                    cr3=0
                                    re3=0
                                    pr3.goto(lrop[0].pos())
                                    continue
                                 elif pb4_position[1]== pr4_position[1]:
                                    cr4=0
                                    re4=0
                                    pr4.goto(lrop[0].pos())
                                    continue
                                 if n==6:
                                   continue
                                 break
                        break
                        '''if (pb1_position[1]==end):
                            print("BLUE TEAM WON")
                        break'''
                        #redroll()
            
                        break                         


if chooseNumberOfPlayers==2:
    twoplayers()
             
if chooseNumberOfPlayers==4:
    fourplayers()
if chooseNumberOfPlayers==3:
    threeplayers()    

            #blueroll()
        
#-------------------------------------   RED   ----------------------------------------#
    #def redroll():     

   
            #greenroll()
       
    #pr3.onclick(pr3movement)
    
    #pr4.onclick(pr4movement)
      #redroll()

turtle.mainloop()
#--------------------------------------------->      list for red pawns paths      <<--------------------------------#
#lrop=[r17,r16,r15,r14,r13,b1,b2,b3,b4,b5,b6,b12,b18,b17,b16,b15,b14,b13,y1,y2,y3,y4,y5,y6,y12,y18,y17,y16,y15,y14,y13,g1,g2,g3,g4,g5,g6,g12,g18,g17,g16,g15,g14,g13,r1,r2,r3,r4,r5,r6,r12,r11,r10,r9,r8,r7]
