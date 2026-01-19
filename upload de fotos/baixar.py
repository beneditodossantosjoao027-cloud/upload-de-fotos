import turtle
import time
import requests
#janela
wn=turtle.Screen()
wn.title("passaro voa")
wn.setup(width=1000,height=500)
wn.bgcolor("black")
#register
wn.register_shape("rua.gif")
wn.register_shape("mendigo.gif")
wn.register_shape("pc.gif")

pc=turtle.Turtle()
pc.shape("pc.gif")
pc.goto(-350,0)

rua=turtle.Turtle()
rua.shape("rua.gif")
rua.goto(0,0)


mendigo=turtle.Turtle()
mendigo.shape("mendigo.gif")
mendigo.goto(350,0)

url1="https://www.bocamaldita.com/wp-content/uploads/2011/08/morador-rua.jpg"
mendigogif=requests.get(url1)
url2="https://viajantesemfim.com.br/wp-content/uploads/2022/03/274984386_4837054576414274_5406000242970143223_n.jpg"
ruagif=requests.get(url2)
url3="https://m.media-amazon.com/images/I/51BtRE4IMcL._AC_UL960_QL65_.jpg"
pcgif=requests.get(url3)
def clicar(x,y):
    if x>200 and x<500:
        with open ("mendigoupload.jpg","wb") as ft:
            ft.write(mendigogif.content)
            print("pronto!")

    if x>-150 and x<150:
        with open ("ruaupload.jpg","wb") as ft:
            ft.write(ruagif.content)
            print("pronto!")
    
    if x<-200 and x>-500:
        with open ("pcupload.jpg","wb") as ft:
            ft.write(pcgif.content)
            print("pronto!")



wn.onscreenclick(clicar)
wn.tracer(1)
wn.mainloop()
