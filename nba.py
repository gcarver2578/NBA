# Gabriel Carver
from tkinter import *

t = {1: '76ers', 2: 'Bucks', 3: 'Bulls', 4: 'Cavaliers', 5: 'Celtics',
     6: 'Clippers', 7: 'Grizzlies', 8: 'Hawks', 9: 'Heat', 10: 'Hornets',
     11: 'Jazz', 12: 'Kings', 13: 'Knicks', 14: 'Lakers', 15: 'Magic',
     16: 'Mavericks', 17: 'Nets', 18: 'Nuggets', 19: 'Pacers', 20: 'Pelicans',
     21: 'Pistons', 22: 'Raptors', 23: 'Rockets', 24: 'Spurs', 25: 'Suns',
     26: 'Thunder', 27: 'Timberwolves', 28: 'Trail Blazers', 29: 'Warriors', 30: 'Wizards'}


class Start:
    """class for the beginning of the program, user chooses their favorite team"""
    def __init__(self, root):
        self.team = ''
        self.root = root
        self.root.configure(bg='black')
        self.t_frame = Frame(self.root)
        self.b_frame = Frame(self.root, bg='black')
        self.b1_frame = Frame(self.b_frame)
        self.b2_frame = Frame(self.b_frame)
        self.b3_frame = Frame(self.b_frame)
        self.b4_frame = Frame(self.b_frame, bg='black')
        self.t_frame.pack(side=TOP)
        self.b_frame.pack(side=TOP)
        self.b1_frame.pack(side=TOP)
        self.b2_frame.pack(side=TOP)
        self.b3_frame.pack(side=TOP)
        self.b4_frame.pack(side=TOP)
        self.confirm_b = Button(self.b4_frame, bg='green', fg='white', text='Yes',
                                width=6, height=3, font=('Courier', 25), command=lambda: self.off_season())
        self.info = StringVar()
        self.info.set('You will manage and make trades for the team you choose.\nTry to win the NBA championship!')
        self.info_lbl = Label(self.b4_frame, textvariable=self.info, bg='black', fg='white',
                              font=('Courier', 25))
        self.info_lbl.pack(side=TOP)
        self.intro = StringVar()
        self.intro.set('Choose your favorite team.')
        self.intro_lbl = Label(self.t_frame, textvariable=self.intro,
                               bg='black',
                               fg='white',
                               font=("Courier", 35))
        self.intro_lbl.pack(side=TOP)
        t_names = [(['Hawks', 'Celtics', 'Nets', 'Hornets', 'Bulls',
                     'Cavaliers', 'Mavericks', 'Nuggets', 'Pistons', 'Warriors'],
                    self.b1_frame),
                   (['Rockets', 'Pacers', 'Clippers', 'Lakers', 'Grizzlies',
                     'Heat', 'Bucks', 'Timberwolves', 'Pelicans', 'Knicks'],
                    self.b2_frame),
                   (['Thunder', 'Magic', '76ers', 'Suns', 'Trail Blazers',
                     'Kings', 'Spurs', 'Raptors', 'Jazz', 'Wizards'],
                    self.b3_frame)]
        self.img_list = []
        for names, frame in t_names:
            for name in names:
                try:
                    self.img_list.append(PhotoImage(file='images/'+name.lower()+'_logo.png'))
                except TclError:
                    self.img_list.append(PhotoImage(file='images/red x.png'))
                self.b = Button(frame, image=self.img_list[-1],
                                height=100,
                                width=100,
                                bg='black',
                                fg='black',
                                highlightcolor='black',
                                highlightbackground='black',
                                relief='flat',
                                command=lambda n=name: self.team_clicked(n))
                self.b.pack(side='left')
                if name == 'Hawks':
                    self.b.focus_force()

    def team_clicked(self, name):
        self.intro.set('Favorite Team: The ' + name)
        self.info.set('Are you sure you want to be the manager of the ' + name + '?')
        if self.confirm_b.winfo_manager() == '':
            self.confirm_b.pack(side=TOP)
        self.team = name

    def off_season(self):
        clear_root(self.root)
        Trades(self.root, self.team)


class Trades:
    """used for making trades during the season"""
    def __init__(self, root, team):
        self.root = root
        self.team = team
        self.t_frame = Frame(self.root)
        self.t_frame.pack(side=TOP)
        self.str_v = StringVar()
        self.str_v.set('It is working! Team: ' + self.team)
        self.lbl = Label(self.root, bg='white', fg='black', textvariable=self.str_v)
        self.lbl.pack(side=TOP)

        variable = StringVar()
        variable.set('')
        w = OptionMenu(self.t_frame, variable, *[t[x] for x in range(1, 31) if t[x] != self.team],
                       command=lambda tm=variable: self.disp_team(tm))
        w.pack(side=TOP)

    def disp_team(self, team):
        print(team)
        self.str_v.set('Trading with: ' + team)


def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()


def main():
    root = Tk()
    Start(root)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()


main()
