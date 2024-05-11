import tkinter as tk
button=['']*10
frame=[""]*10
root=tk.Tk()
root.title("Tik-Toe-Game")
root.geometry("600x700")
root.configure(bg="#383E45")
font=("lucidaconsole",30)
fonttext=("arialblack",14)
colbg="#6B6D70"
colfg="#ECECEC"
wd=20
hg=10
mdbylabel=tk.Label(root,font=fonttext,height=3,borderwidth=3,text="made by\n Arhip",bg="#52BCBE",relief="ridge")
infolabel=tk.Label(root,font=fonttext,height=3,borderwidth=3,text="ЛКМ за X\nПКМ за O",bg="#52BCBE",relief="ridge")
desk=[i for i in range(10)]

def win(winner):
    winner=str(winner)
    if winner!="D":  wnmsg=winner+" win!"
    else:   wnmsg="Ничья!"
    wnmsg+="\nGoodbye!"
    fr=tk.Frame(root)
    fr.grid(row=3,column=1,pady=10)
    winLab=tk.Label(fr,width=40,height=3,text=wnmsg,font=fonttext,relief="groove",bg="#87A6A6",fg="white")
    winLab.pack()
    root.after(2000,lambda:root.destroy())
def isWin(d):
    for i in range(3):
        if d[i*3+1]==d[i*3+2]==d[i*3+3]:    win(d[i*3+1])
        elif d[i+1]==d[i+4]==d[i+7]:    win(d[i+1])
    if d[1]==d[5]==d[9]:    win(d[5])
    elif d[3]==d[5]==d[7]:  win(d[5])
    elif d.count("O")+d.count("X")==9:  root.after(200, lambda:win("D"))
def click(ev,player):
    color="#9B3D3D" if player=="X" else "#43994C"
    num=ev.widget['text']
    button[num].destroy()
    button[num]=tk.Label(frame[num],text=player,fg=colfg,bg=color,width=wd,height=hg,font=font,relief="sunken",borderwidth=5)
    button[num].pack()
    desk[num]=player
    isWin(desk)
def click1(ev): click(ev,"X")
def click2(ev): click(ev,"O")

for i in range(3):
    root.rowconfigure(i,weight=1,minsize=100)
    root.columnconfigure(i,weight=1,minsize=100)
    for j in range(3):
        n=1+j+i*3
        frame[n]=tk.Frame(root)
        frame[n].grid(row=i,column=j,padx=10,pady=10)
        button[n]=tk.Button(frame[n],bg=colbg,fg=colbg,text=n,width=wd,height=hg,font=font)
        button[n].pack()
        button[n].bind('<1>',click1)
        button[n].bind('<3>',click2)
infolabel.grid(column=2,pady=10)
mdbylabel.grid(row=3,column=0,pady=10)
#red#B24646#lime#4DB658#
