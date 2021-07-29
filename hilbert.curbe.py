from turtle import Turtle, Screen

def curva_der(nivel, longitud):
    if nivel > 0:
        trt.left(90)
        curva_izq(nivel-1, longitud)
        trt.fd(longitud)
        trt.right(90)
        curva_der(nivel-1, longitud)
        trt.fd(longitud)
        curva_der(nivel-1, longitud)
        trt.right(90)
        trt.fd(longitud)
        curva_izq(nivel-1, longitud)
        trt.left(90)

def curva_izq(nivel, longitud):
    if nivel > 0:
        trt.right(90)
        curva_der(nivel-1, longitud)
        trt.fd(longitud)
        trt.left(90)
        curva_izq(nivel-1, longitud)
        trt.fd(longitud)
        curva_izq(nivel-1, longitud)
        trt.left(90)
        trt.fd(longitud)
        curva_der(nivel-1, longitud)
        trt.right(90)

trt = Turtle()
trt.hideturtle()
trt.speed(0)
pantalla = Screen()
pantalla.setup(500, 500)
pantalla.screensize(500, 500)
pantalla.setworldcoordinates(-60, -60, 540, 540)
pantalla.delay(0)
curva_der(6, 5)

# Guía longitudes según el nivel de la curva
# 500  150  70   30   15

pantalla.exitonclick()
