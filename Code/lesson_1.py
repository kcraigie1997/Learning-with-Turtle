def test(res):
    import turtle

    screen = turtle.TurtleScreen(res)
    screen.setworldcoordinates(-10, 200, 400, -10)	
    t = turtle.RawTurtle(res)

    number = 0

    while number < 21:
        if number % 2 == 0:
            t.pencolor('red')
        else:
            t.pencolor('green')

        t.back(number * 10)
        t.left(144)
        number = number + 1

    turtle.bye()














