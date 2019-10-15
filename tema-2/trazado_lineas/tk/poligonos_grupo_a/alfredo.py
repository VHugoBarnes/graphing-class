# -*- coding: utf-8 -*-
from Tkinter import *
import tkColorChooser  # libreria para obtener la gama de colores

class Alfredo:
    def mostrar(self, v0):
        # aparece la gamade colores RGB o en numero hexadecimal
        a = tkColorChooser.askcolor(title="Color de contorno")
        b = tkColorChooser.askcolor(title="Color de cornia y partes iluminadas")
        c = tkColorChooser.askcolor(title="Color de piel iluminada")
        d = tkColorChooser.askcolor(title="Color de sombra clara")
        e = tkColorChooser.askcolor(title="Color de sombra oscurra")
        f = tkColorChooser.askcolor(title="Color de sombra media")
        g = tkColorChooser.askcolor(title="Color de pupila")
        h = tkColorChooser.askcolor(title="Color de iris")
        # ventana secundaria
        v1 = Toplevel()
        v1.title(v0)

        v1.protocol('Wn_DELETE_WINDOW', "onexit")  # para cerrar la ventana por medio de la cruz
        v1.geometry('450x560')  # tamaño de la ventana
        # v1.iconbitmap("vhija.ico")  # para cambiar el icono de la ventana

        canvas1 = Canvas(v1, width=200, height=200,
                         bg='white')  # (b[1])) esto es para seleccionar el color de fondo# OBJETO DE LA TKINTER   CANVAS(FIGURAS)     200 pixeles de ancho 200 ancho
        canvas1.pack(expand=YES, fill=BOTH)  # DESPLEGAR EL CANVAS, EXPAND QUE SEA EXPANDIBLE
        # puntos = [0, 0, 0, 10, 10, 10, 10, 20]
        # canvas1.create_polygon(puntos, width=10, fill=(a[1]))

        # Cabeza
        canvas1.create_polygon(50, 170, 50, 120, 60, 120, 60, 100,
                               70, 100, 70, 90, 90, 90, 90, 80,
                               160, 80, 160, 60, 170, 60, 170, 50,
                               190, 50, 190, 40, 230, 40, 230, 50,
                               240, 50, 240, 80, 230, 80, 230, 90,
                               270, 90, 270, 100, 290, 100, 290, 110,
                               300, 110, 300, 120, 310, 120, 310, 160,
                               300, 160, 300, 170, 290, 170, 290, 180,
                               280, 180, 280, 190, 200, 190, 50, 170, width=10, fill=(a[1]))  # fill='black')#negro

        # beige
        canvas1.create_polygon(70, 150, 140, 120, 180, 120, 270, 130,
                               270, 180, 210, 180, 210, 200, 200, 220,
                               170, 250, 80, 250, 60, 240, 40, 220,
                               40, 200, 50, 180, 60, 170, 70, 150, width=10,
                               fill=(c[1]))  # fill="#%02x%02x%02x" % (240, 230, 140))

        canvas1.create_polygon(30, 200, 30, 220, 40, 220, 40, 230,
                               50, 230, 50, 240, 60, 240, 60, 250,
                               80, 250, 80, 260, 110, 260, 110, 300,
                               120, 300, 120, 330, 130, 330, 130, 350,
                               140, 350, 140, 360, 150, 360, 150, 370,
                               160, 370, 160, 380, 170, 380, 170, 370,
                               160, 370, 160, 360, 150, 360, 150, 350,
                               140, 350, 140, 330, 130, 330, 130, 300,
                               120, 300, 120, 260, 170, 260, 170, 250,
                               180, 250, 180, 240, 190, 240, 190, 230,
                               200, 230, 200, 220, 210, 220, 210, 200,
                               220, 200, 220, 190, 250, 190, 250, 180,
                               280, 150, 280, 140, 270, 140, 270, 130,
                               260, 130, 260, 120, 210, 120, 210, 130,
                               200, 130, 200, 140, 210, 140, 210, 130,
                               260, 130, 260, 140, 270, 140, 270, 150,
                               280, 150, 250, 180, 210, 180, 210, 200,
                               200, 200, 200, 220, 190, 220, 190, 230,
                               180, 230, 180, 240, 170, 240, 170, 250,
                               80, 250, 80, 240, 60, 240, 60, 230,
                               50, 230, 50, 220, 40, 220, 40, 200,
                               30, 200, width=10, fill=(f[1]))  # fill="#%02x%02x%02x" % (210, 106, 30) ) #barro

        canvas1.create_polygon(220, 50, 190, 50, 190, 60, 170, 60,
                               170, 80, 160, 80, 160, 90, 140, 100,
                               110, 100, 110, 90, 90, 90, 90, 110,
                               110, 110, 110, 100, 130, 100, 130, 110,
                               140, 110, 140, 120, 90, 120, 90, 130,
                               80, 130, 80, 140, 70, 140, 70, 150,
                               130, 150, 130, 140, 140, 140, 140, 120,
                               210, 110, 230, 110, 230, 100, 210, 100,
                               210, 110, 140, 120, 140, 100, 160, 90,
                               170, 90, 170, 70, 190, 70, 190, 60,
                               220, 60, 220, 60, width=10, fill=(b[1]))  # fill='white')#blanco

        # cafemarrom
        canvas1.create_polygon(70, 100, 70, 120, 60, 120, 60, 170,
                               50, 170, 50, 180, 60, 180, 60, 170,
                               70, 170, 70, 140, 80, 140, 80, 130,
                               90, 130, 90, 120, 100, 120, 100, 110,
                               90, 110, 90, 100, 70, 100, width=10,
                               fill=(d[1]))  # fill="#%02x%02x%02x" % (250, 133, 63))

        canvas1.create_rectangle(180, 120, 210, 130, width=1, fill=(d[1]), outline=(
            d[1]))  # fill="#%02x%02x%02x" % (250, 133, 63),outline="#%02x%02x%02x" % (250, 133, 63))

        canvas1.create_polygon(290, 120, 300, 120, 300, 160, 290, 160,
                               290, 170, 280, 170, 280, 180, 250, 180,
                               250, 170, 260, 170, 260, 160, 270, 160,
                               270, 150, 280, 150, 280, 140, 290, 140,
                               290, 120, width=10, fill=(d[1]))  # fill="#%02x%02x%02x" % (250, 133, 63))

        # cafe

        canvas1.create_polygon(200, 100, 190, 100, 180, 100, 180, 90,
                               170, 90, 170, 70, 190, 70, 190, 60,
                               220, 60, 220, 50, 230, 50, 230, 80,
                               220, 80, 220, 90, 200, 90, 200, 100,
                               200, 110, 180, 110, 180, 100, 160, 100,
                               160, 90, 110, 90, 110, 110, 100, 110,
                               100, 120, 130, 120, 130, 100, 140, 100,
                               140, 110, 130, 110, 130, 120, 260, 120,
                               260, 130, 270, 130, 270, 140, 290, 140,
                               290, 110, 270, 110, 270, 100, 230, 100,
                               230, 110, 210, 110, 210, 100, 200, 100, width=10,
                               fill=(e[1]))  # fill="#%02x%02x%02x" % (139, 69, 19))

        # NARIZ
        canvas1.create_rectangle(20, 170, 50, 200, width=1, fill=(a[1]),
                                 outline=(a[1]))  # fill="black", outline="black")#negro

        canvas1.create_rectangle(30, 180, 40, 190, width=1, fill=(e[1]), outline=(
            e[1]))  # fill="#%02x%02x%02x" % (139, 69, 19),outline="#%02x%02x%02x" % (139, 69, 19))#cafe

        # OJO
        canvas1.create_polygon(140, 160, 140, 170, 110, 170, 110, 180,
                               100, 180, 100, 190, 90, 190, 90, 220,
                               100, 220, 100, 230, 130, 230, 130, 220,
                               160, 220, 160, 210, 170, 210, 170, 170,
                               180, 170, 180, 160, 140, 160, width=10, fill=(a[1]))  # fill='black')#negro

        canvas1.create_polygon(100, 200, 100, 190, 110, 190, 130, 180,
                               160, 180, 160, 210, 150, 210, 150, 220,
                               140, 220, 100, 200, width=10, fill=(b[1]))  # fill='white')#blanco

        canvas1.create_rectangle(100, 210, 130, 220, width=1, fill=(g[1]),
                                 outline=(g[1]))  # fill="sky blue", outline="sky blue")#celeste

        canvas1.create_polygon(100, 210, 100, 200, 110, 200, 110, 180,
                               130, 180, 130, 190, 140, 190, 140, 220,
                               130, 220, 130, 210, width=10, fill=(h[1]))  # fill='blue')#azul
        # cuerpo
        # MARRON
        canvas1.create_polygon(160, 450, 150, 450, 150, 480, 140, 480,
                               140, 500, 120, 500, 120, 450, 130, 450,
                               130, 450, 140, 450, 140, 360, 150, 360,
                               150, 370, 160, 370, 160, 450, 160, 480,
                               150, 480, 150, 500, 180, 500, 180, 470,
                               190, 470, 190, 430, 200, 430, 200, 380,
                               210, 380, 210, 350, 220, 350, 260, 320,
                               270, 340, 270, 370, 280, 380, 280, 430,
                               270, 470, 270, 500, 310, 500, 330, 420,
                               330, 420, 340, 400, 360, 400, 360, 480,
                               350, 480, 350, 500, 400, 500, 400, 430,
                               420, 430, 420, 370, 390, 370, 390, 360,
                               360, 210, 340, 190, 340, 260, 250, 300,
                               140, 260, 130, 260, 130, 290, 145, 340,
                               170, 370, 170, 450, 160, 450, width=10, fill=(d[1]))
        # NEGRO
        canvas1.create_polygon(130, 350, 130, 450, 120, 450, 120, 480,
                               110, 480, 110, 500, 120, 500, 120, 510,
                               180, 510, 180, 500, 190, 500, 190, 470,
                               200, 470, 200, 430, 210, 430, 210, 380,
                               200, 380, 200, 430, 190, 430, 190, 470,
                               180, 470, 180, 500, 150, 500, 150, 480,
                               160, 480, 160, 450, 170, 450, 170, 380,
                               160, 380, 160, 450, 150, 450, 150, 480,
                               140, 480, 140, 500, 120, 500, 120, 480,
                               130, 480, 130, 450, 140, 450, 140, 350,
                               130, 350, width=10, fill=(a[1]))

        canvas1.create_polygon(260, 340, 260, 370, 270, 370, 270, 380,
                               280, 380, 280, 430, 270, 430, 270, 470,
                               260, 470, 260, 500, 270, 500, 270, 510,
                               310, 510, 310, 500, 320, 500, 320, 460,
                               330, 460, 330, 420, 340, 420, 340, 400,
                               360, 400, 360, 450, 350, 450, 350, 480,
                               340, 480, 340, 500, 350, 500, 350, 510,
                               390, 510, 390, 500, 400, 500, 400, 470,
                               410, 470, 410, 430, 420, 430, 420, 410,
                               430, 410, 430, 380, 420, 380, 420, 370,
                               410, 370, 410, 360, 390, 360, 390, 370,
                               410, 370, 410, 380, 420, 380, 420, 410,
                               410, 410, 410, 430, 400, 430, 400, 470,
                               390, 470, 390, 500, 350, 500, 350, 480,
                               360, 480, 360, 450, 370, 450, 370, 390,
                               340, 390, 340, 380, 320, 380, 320, 370,
                               310, 370, 310, 360, 300, 360, 300, 350,
                               290, 350, 290, 340, 280, 340, 280, 350,
                               290, 350, 290, 360, 300, 360, 300, 370,
                               310, 370, 310, 380, 320, 380, 320, 390,
                               340, 390, 340, 400, 330, 400, 330, 420,
                               320, 420, 320, 460, 310, 460, 310, 500,
                               270, 500, 270, 470, 280, 470, 280, 430,
                               290, 430, 290, 380, 280, 380, 280, 370,
                               270, 370, 270, 340, 260, 340, width=10, fill=(a[1]))

        canvas1.create_polygon(160, 250, 160, 260, 170, 260, 170, 270,
                               180, 270, 180, 280, 200, 280, 200, 270,
                               220, 270, 220, 260, 240, 260, 240, 250,
                               260, 250, 260, 240, 320, 240, 320, 250,
                               340, 250, 340, 200, 350, 200, 350, 210,
                               360, 210, 360, 220, 370, 220, 370, 210,
                               360, 210, 360, 200, 350, 200, 350, 190,
                               340, 190, 340, 180, 330, 180, 330, 240,
                               320, 240, 320, 230, 260, 230, 260, 240,
                               240, 240, 240, 250, 220, 250, 220, 260,
                               200, 260, 200, 270, 180, 270, 180, 260,
                               170, 260, 170, 250, 160, 250, width=10, fill=(a[1]))

        # cafe
        canvas1.create_polygon(140, 260, 140, 270, 150, 270, 150, 280,
                               160, 280, 160, 290, 200, 290, 200, 300,
                               320, 300, 320, 290, 330, 290, 330, 280,
                               340, 280, 340, 250, 320, 250, 320, 240,
                               260, 240, 260, 250, 240, 250, 240, 260,
                               220, 260, 220, 270, 200, 270, 200, 280,
                               180, 280, 180, 270, 170, 270, 170, 260,
                               140, 260, width=10, fill=(e[1]))

        # beige
        canvas1.create_rectangle(220, 270, 240, 290, width=1, fill=(c[1]), outline=(c[1]))

        canvas1.create_rectangle(260, 250, 280, 270, width=1, fill=(c[1]), outline=(c[1]))

        canvas1.create_rectangle(280, 270, 300, 290, width=1, fill=(c[1]), outline=(c[1]))

        canvas1.create_rectangle(290, 240, 310, 250, width=1, fill=(c[1]), outline=(c[1]))

        canvas1.create_polygon(370, 220, 370, 230, 380, 230, 380, 260,
                               370, 260, 370, 270, 380, 270, 380, 290,
                               390, 290, 390, 330, 380, 330, 380, 350,
                               370, 350, 370, 340, 360, 340, 360, 220,
                               370, 220, width=10, fill=(c[1]))

        canvas1.create_polygon(210, 360, 220, 360, 220, 350, 230, 350,
                               230, 340, 250, 340, 250, 330, 290, 330,
                               290, 340, 300, 340, 300, 320, 290, 320,
                               290, 310, 260, 310, 260, 320, 240, 320,
                               240, 330, 230, 330, 230, 340, 220, 340,
                               220, 350, 210, 350, 210, 360, width=10, fill=(c[1]))

        canvas1.create_polygon(120, 260, 120, 300, 130, 300, 130, 330,
                               140, 330, 140, 350, 150, 350, 150, 360,
                               160, 360, 160, 370, 170, 370, 170, 350,
                               160, 350, 160, 340, 150, 340, 150, 320,
                               140, 320, 140, 290, 130, 290, 130, 260,
                               120, 260, width=10, fill=(c[1]))

        # blanco
        canvas1.create_polygon(150, 290, 150, 300, 160, 300, 160, 320,
                               170, 320, 170, 330, 180, 330, 180, 380,
                               170, 380, 170, 420, 180, 420, 180, 380,
                               190, 380, 190, 350, 200, 350, 200, 340,
                               210, 340, 210, 330, 200, 330, 200, 320,
                               190, 320, 190, 310, 170, 310, 170, 300,
                               160, 300, 160, 290, 150, 290, width=10, fill=(b[1]))

        canvas1.create_polygon(320, 340, 330, 340, 330, 360, 340, 360,
                               340, 330, 330, 330, 330, 320, 320, 320,
                               320, 340, width=10, fill=(b[1]))

        canvas1.create_polygon(350, 480, 350, 490, 360, 490, 360, 480,
                               370, 480, 370, 450, 380, 450, 380, 430,
                               370, 430, 370, 450, 360, 450, 360, 480,
                               350, 480, width=10, fill=(b[1]))
        # barro
        canvas1.create_polygon(210, 380, 220, 380, 220, 360, 230, 360,
                               230, 350, 250, 350, 250, 340, 290, 340,
                               290, 330, 250, 330, 250, 340, 230, 340,
                               230, 350, 220, 350, 220, 360, 210, 360,
                               210, 380, width=10, fill=(f[1]))

        canvas1.create_polygon(380, 360, 390, 360, 390, 330, 400, 330,
                               400, 290, 390, 290, 390, 270, 380, 270,
                               380, 260, 390, 260, 390, 230, 380, 230,
                               380, 220, 370, 220, 370, 230, 380, 230,
                               380, 260, 370, 260, 370, 270, 380, 270,
                               380, 290, 390, 290, 390, 330, 380, 330,
                               380, 360, width=10, fill=(f[1]))

