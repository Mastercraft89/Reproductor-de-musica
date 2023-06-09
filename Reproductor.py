from tkinter import*
import pygame, sys
from pygame.locals import*
from tkinter import filedialog
#from PIL import ImageTk, image
import os  
pygame.init()

def openSONG():
    song = filedialog.askopenfilename()
    pygame.mixer.music.load(song)
    
def playSONG():
    pygame.mixer.music.play()
    
def stopSONG():
    pygame.mixer.music.stop()

def resumeSONG():
    pygame.mixer.music.unpause()

def pauseSONG():
    pygame.mixer.music.pause()

def volumen_up():
    nivelvolumen = pygame.mixer.music.get_volume() + 0.5
    pygame.mixer.music.set_volume(nivelvolumen)
def volumen_lower():
    nivelvolumen = pygame.mixer.music.get_volume() - 0.5
    pygame.mixer.music.set_volume(nivelvolumen)

raiz = Tk()
raiz.title("MP3")
raiz.geometry("600x400")
raiz.resizable(1,1)

#frame -  marco
frame_principal = Frame(raiz,bg="#00aae4",width=600,height=400)
frame_principal.pack(fill="both", expand=1)

#Titulo Reproductor
tituloreproductor = Label(frame_principal, text = "REPRODUCTOR DE MUSICA",bg="#4d4d4d",fg="#f4f4f4",font =("COCOGOOSE", 15))
tituloreproductor.place(relx=0.30,rely=0.20)

#Botones
botonfile = Button(frame_principal, text="OPEN FILE",bg = "#458874", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,
                    command= openSONG)
botonfile.place(relx=0.1, rely=0.5)

#Boton para iniciar
botonplay = Button(frame_principal, text="INICIAR",bg="#76EE00", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,
                   command= playSONG)
botonplay.place(relx=0.25, rely=0.5)

#boton para detenerse
botonstop = Button(frame_principal, text="DETENERSE", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,bg="#e2504c",
                   command= stopSONG)
botonstop.place(relx=0.4, rely=0.5)

#boton para pausar
botonpause = Button(frame_principal, text="PAUSAR",bg="#00CDCD", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,
                    command=pauseSONG)
botonpause.place(relx=0.55, rely=0.5)

#boton para continuar
botoncontinue = Button(frame_principal, text="CONTINUAR",bg="#BF3EFF", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,
                       command= resumeSONG)
botoncontinue.place(relx=0.7, rely=0.5)

#boton para subir de volumen
botonVolUP = Button(frame_principal, text="VOL +", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,
                       command= volumen_up)
botonVolUP.place(relx=0.1, rely=0.7)

#boton para bajar de volumen
botonVolLower = Button(frame_principal, text="VOL -", font=("COCOGOOSE", 10),width=10,height=2,bd=0,highlightthickness=0,
                      command= volumen_lower)
botonVolLower.place(relx=0.7, rely=0.7)
raiz.mainloop()