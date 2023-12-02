import re
class game:
    dlm="|"
    dlm2="--"
    end=" "
    xwin="Победа Крестиков!"
    owin="Победа Ноликов!"
    nowin="Матч окончен! Ничья!"
    x="X"
    o="O"
    winners=[x,o]
    empty="-"
    choiceis="Выбор: "
    exitMsg="exit"
    def __init__(self):
        self.desk=[game.empty for i in range(9)]
        self.move="Крестики"
        self.Over=0
    def output(self):
       print("")
       for y in range(3):
            for x in range(1,4):
                if x==1:
                    print(game.dlm,end=game.end)
                if self.desk[y*3+x-1]==game.empty: print(y*3+x,end=game.end)
                else: print(self.desk[y*3+x-1],end=game.end)
                print(game.dlm, end=game.end)
            print("")
    def newMove(self):
        movePattern=r"^[0-9]$"
        newMove=input("Ходят {}: ".format(self.move))
        if newMove==game.exitMsg:
            print("Выход...")
            self.Over=1
            return
        while not re.match(movePattern,newMove) or not 10>int(newMove)>0 or self.desk[int(newMove)-1]!=game.empty:
            print('Клетки "{}" на поле не существует или она занята.'.format(newMove))
            newMove=input("Ходят {}: ".format(self.move))
        newMove=int(newMove)
        if self.move=="Крестики": 
            self.desk[newMove-1]=game.x
            self.move="Нолики"
        else:
            self.desk[newMove-1]=game.o
            self.move="Крестики"
    def isOver(self):
        d=self.desk
        e=game.empty
        for i in game.winners:
            if i==d[0]==d[4]==d[8]!=e or i==d[2]==d[4]==d[6]!=e: self.Over=i
            for colomn in range(3):
                if i==d[colomn]==d[colomn+3]==d[colomn+6]!=e: self.Over=i
            for row in range(0,6,3):
                if i==d[row]==d[row+1]==d[row+2]!=e: self.Over=i
            if i==game.x and self.Over==i:
                print(game.xwin)
                return
            elif i==game.o and self.Over==i:
                print(game.owin)
                return
        if d.count(game.empty)==0 or self.Over==1:
            print(game.nowin)
            self.Over=1
    def start(name):
        print("{:^14}".format("Новая игра!"))
        name=game()
        while True:
            name.output()
            name.isOver()
            if name.Over!=0: break
            name.newMove()
        print("\n Игра окончена. Начать заново?\n1. {:10} 2. {:10}".format("Да","Нет"))
        choice=input(choiceis)
        if re.search(r"^1$|^(?:Д|L|l|д)(?:А|а|F|f)$",choice): game.start('anoterNewGame')
#actualcode
game.start('newGame')
