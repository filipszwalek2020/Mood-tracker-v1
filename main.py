'''
Mood tracker - jego zadaniem jest codzienne zbadanie tego jak się czujesz
jak fizycznie? jak psychicznie?
następnie zapisać te dane do pliku txt który później można wykorzystać
jako dane do badań nad samopoczuciem
'''

from tkinter import *
from datetime import *
import sys

#można to przerobić na pola w klasie
# data
today = str(date.today())
# godzina
now = datetime.now()
time = now.strftime("%H:%M")
# lista z nastrojami
mood = ["Enraged","Stressed","Shocked","Surprised","Festive","Ecsastic","Fuming","Angry","Restlest","Energized","Optimstic","Excited","Repulsed","Worried","Uneasy","Pleasant","Hopeful","Blissful","Disgusted","Down","Apathetic","At ease","Content","Fulfilled","Miserable","Lonely","Tired","Relaxed","Restful","Balanced","Despair","Desolate","Drained","Sleepy","Tranquil","Serene"]

#to można na metodę ale to do przemyślenia
def saveFile(n):
    '''#funkcja zapisująca wybrany mood do pliku mood.txt'''
    #data,godzina,wybrany mood
    result = str(today) +"\t"+time+"\t"+ mood[n] +"\n"
    #print(result)
    with open("Mood.txt","a") as file:
        file.write(result)
    #po wybraniu nastroju aplikacja ma się zamknąć
    sys.exit(0)

#GUI
# tworzy obiektk przy użyciu klasy Tk()
root = Tk()
# rozmiary okna i położenie
width = 720
height = 750
root.geometry("%ix%i+300+30"%(width,height))
root.tk.call('tk', 'scaling', 2.0)
#tytuł okna aplikacji
root.title("Mood Tracker v0.2")
#ikona okna aplikacji
root.iconbitmap("icon.ico")
#kolor tła aplikacji
root['bg']='#c0d6e4'
#blokuje możliwość zmiany rozdzielczości
root.resizable(False, False)
#label z pytaniem
label1=Label(root,width=50,height=2, text="How feeling today? \n{0}".format(today), font=('Arial', '13'))
label1.grid(row=0,columnspan=8,pady=5)

#bardzo dużo kodu, tworzenie przycisków i ich umieszczenie na siatce
#zmienna do obsługi indexów z listy mood
i=0
bttn0 = Button(root, width=9, height=4, text=(mood[0]), font=('Lato', '9'),bd=0,command= lambda i=i:saveFile(i),bg="#FA0D13")
bttn1 = Button(root, width=9, height=4, text=(mood[1]),font=('Lato', '9'),bd=0,command= lambda i=i+1:saveFile(i),bg="#DE280B")
bttn2 = Button(root, width=9, height=4, text=(mood[2]),font=('Lato', '9'),bd=0,command=lambda i=i+2:saveFile(i),bg="#F54500")
bttn3 = Button(root, width=9, height=4, text=(mood[3]),font=('Lato', '9'),bd=0,command=lambda i=i+3:saveFile(i),bg="#DE660B")
bttn4 = Button(root, width=9, height=4, text=(mood[4]),font=('Lato', '9'),bd=0,command=lambda i=i+4:saveFile(i),bg="#FA950D")
bttn5 = Button(root, width=9, height=4, text=(mood[5]),font=('Lato', '9'),bd=0,command=lambda i=i+5:saveFile(i),bg="#F2CB05")

bttn6 = Button(root, width=9, height=4, text=(mood[6]),font=('Lato', '9'),bd=0,command=lambda i=i+6:saveFile(i),bg="#FA0D13")
bttn7 = Button(root, width=9, height=4, text=(mood[7]),font=('Lato', '9'),bd=0,command=lambda i=i+7:saveFile(i),bg="#DE280B")
bttn8 = Button(root, width=9, height=4, text=(mood[8]),font=('Lato', '9'),bd=0,command=lambda i=i+8:saveFile(i),bg="#F54500")
bttn9 = Button(root, width=9, height=4, text=(mood[9]),font=('Lato', '9'),bd=0,command=lambda i=i+9:saveFile(i),bg="#DE660B")
bttn10 = Button(root, width=9, height=4, text=(mood[10]),font=('Lato', '9'),bd=0,command=lambda i=i+10:saveFile(i),bg="#FA950D")
bttn11 = Button(root, width=9, height=4, text=(mood[11]),font=('Lato', '9'),bd=0,command=lambda i=i+11:saveFile(i),bg="#F2CB05")

bttn12 = Button(root, width=9, height=4, text=(mood[12]),font=('Lato', '9'),bd=0,command=lambda i=i+12:saveFile(i),bg="#FA0D13")
bttn13 = Button(root, width=9, height=4, text=(mood[13]),font=('Lato', '9'),bd=0,command=lambda i=i+13:saveFile(i),bg="#DE280B")
bttn14 = Button(root, width=9, height=4, text=(mood[14]),font=('Lato', '9'),bd=0,command=lambda i=i+14:saveFile(i),bg="#F54500")
bttn15 = Button(root, width=9, height=4, text=(mood[15]),font=('Lato', '9'),bd=0,command=lambda i=i+15:saveFile(i),bg="#DE660B")
bttn16 = Button(root, width=9, height=4, text=(mood[16]),font=('Lato', '9'),bd=0,command=lambda i=i+16:saveFile(i),bg="#FA950D")
bttn17 = Button(root, width=9, height=4, text=(mood[17]),font=('Lato', '9'),bd=0,command=lambda i=i+17:saveFile(i),bg="#F2CB05")

bttn18 = Button(root, width=9, height=4, text=(mood[18]),font=('Lato', '9'),bd=0,command=lambda i=i+18:saveFile(i),bg="#38465B")
bttn19 = Button(root, width=9, height=4, text=(mood[19]),font=('Lato', '9'),bd=0,command=lambda i=i+19:saveFile(i),bg="#303C4E")
bttn20 = Button(root, width=9, height=4, text=(mood[20]),font=('Lato', '9'),bd=0,command=lambda i=i+20:saveFile(i),bg="#5F769A")
bttn21 = Button(root, width=9, height=4, text=(mood[21]),font=('Lato', '9'),bd=0,command=lambda i=i+21:saveFile(i),bg="#53956C")
bttn22 = Button(root, width=9, height=4, text=(mood[22]),font=('Lato', '9'),bd=0,command=lambda i=i+22:saveFile(i),bg="#74BB88")
bttn23 = Button(root, width=9, height=4, text=(mood[23]),font=('Lato', '9'),bd=0,command=lambda i=i+23:saveFile(i),bg="#BEE5BE")

bttn24 = Button(root, width=9, height=4, text=(mood[24]),font=('Lato', '9'),bd=0,command=lambda i=i+24:saveFile(i),bg="#38465B")
bttn25 = Button(root, width=9, height=4, text=(mood[25]),font=('Lato', '9'),bd=0,command=lambda i=i+25:saveFile(i),bg="#303C4E")
bttn26 = Button(root, width=9, height=4, text=(mood[26]),font=('Lato', '9'),bd=0,command=lambda i=i+26:saveFile(i),bg="#5F769A")
bttn27 = Button(root, width=9, height=4, text=(mood[27]),font=('Lato', '9'),bd=0,command=lambda i=i+27:saveFile(i),bg="#53956C")
bttn28 = Button(root, width=9, height=4, text=(mood[28]),font=('Lato', '9'),bd=0,command=lambda i=i+28:saveFile(i),bg="#74BB88")
bttn29 = Button(root, width=9, height=4, text=(mood[29]),font=('Lato', '9'),bd=0,command=lambda i=i+29:saveFile(i),bg="#BEE5BE")

bttn30 = Button(root, width=9, height=4, text=(mood[30]),font=('Lato', '9'),bd=0,command=lambda i=i+30:saveFile(i),bg="#38465B")
bttn31 = Button(root, width=9, height=4, text=(mood[31]),font=('Lato', '9'),bd=0,command=lambda i=i+31:saveFile(i),bg="#303C4E")
bttn32 = Button(root, width=9, height=4, text=(mood[32]),font=('Lato', '9'),bd=0,command=lambda i=i+32:saveFile(i),bg="#5F769A")
bttn33 = Button(root, width=9, height=4, text=(mood[33]),font=('Lato', '9'),bd=0,command=lambda i=i+33:saveFile(i),bg="#53956C")
bttn34 = Button(root, width=9, height=4, text=(mood[34]),font=('Lato', '9'),bd=0,command=lambda i=i+34:saveFile(i),bg="#74BB88")
bttn35 = Button(root, width=9, height=4, text=(mood[35]),font=('Lato', '9'),bd=0,command=lambda i=i+35:saveFile(i),bg="#BEE5BE")

bttn0.grid(row=1,column=0,pady=3)
bttn1.grid(row=1,column=1,pady=3)
bttn2.grid(row=1,column=2,pady=3)
bttn3.grid(row=1,column=3,pady=3)
bttn4.grid(row=1,column=4,pady=3)
bttn5.grid(row=1,column=5,pady=3)

bttn6.grid(row=2,column=0,pady=3)
bttn7.grid(row=2,column=1,pady=3)
bttn8.grid(row=2,column=2,pady=3)
bttn9.grid(row=2,column=3,pady=3)
bttn10.grid(row=2,column=4,pady=3)
bttn11.grid(row=2,column=5,pady=3)

bttn12.grid(row=3,column=0,pady=3)
bttn13.grid(row=3,column=1,pady=3)
bttn14.grid(row=3,column=2,pady=3)
bttn15.grid(row=3,column=3,pady=3)
bttn16.grid(row=3,column=4,pady=3)
bttn17.grid(row=3,column=5,pady=3)

bttn18.grid(row=4,column=0,pady=3)
bttn19.grid(row=4,column=1,pady=3)
bttn20.grid(row=4,column=2,pady=3)
bttn21.grid(row=4,column=3,pady=3)
bttn22.grid(row=4,column=4,pady=3)
bttn23.grid(row=4,column=5,pady=3)

bttn24.grid(row=5,column=0,pady=3)
bttn25.grid(row=5,column=1,pady=3)
bttn26.grid(row=5,column=2,pady=3)
bttn27.grid(row=5,column=3,pady=3)
bttn28.grid(row=5,column=4,pady=3)
bttn29.grid(row=5,column=5,pady=3)

bttn30.grid(row=6,column=0,pady=3)
bttn31.grid(row=6,column=1,pady=3)
bttn32.grid(row=6,column=2,pady=3)
bttn33.grid(row=6,column=3,pady=3)
bttn34.grid(row=6,column=4,pady=3)
bttn35.grid(row=6,column=5,pady=3)




#zapętla okno aby nie zniknęło
root.mainloop()


