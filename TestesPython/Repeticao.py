import turtle

#for passo in range(4) :
#    print(passo)
#    turtle.forward(200)
#    turtle.right(90)

#****************** TIPOS DE LOOPs  FOR********************************************************
#for variavel in range(9)     laço normal                                                     *
#for variavel in range(1,9)   primeiro valor especifica valor inicial do laço                 *
#for variavel in range(1,9,3) terceiro valor define passo do laço                             *
#for variavel in [1,5,6,9]    pode ser especificado o valor da variavel a cada loop           *
#**********************************************************************************************

for passo in range(6) :
    turtle.forward(100)
    turtle.right(360/6)

    for outroPasso in range(6) :
        turtle.forward(50)
        turtle.right(360/6)

