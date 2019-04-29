# Gabriel Carver
from tkinter import *
import random

atlantic = ['76ers', 'Celtics', 'Knicks', 'Nets', 'Raptors']
central = ['Bucks', 'Bulls', 'Cavaliers', 'Pacers', 'Pistons']
southeast = ['Hawks', 'Heat', 'Hornets', 'Magic', 'Wizards']

northwest = ['Jazz', 'Nuggets', 'Thunder', 'Timberwolves', "Trail Blazers"]
pacific = ['Clippers', 'Kings', 'Lakers', 'Suns', 'Warriors']
southwest = ['Grizzlies', 'Mavericks', 'Pelicans', 'Rockets', 'Spurs']

east = atlantic+central+southeast
west = northwest+pacific+southwest
nba = east+west

t = {1: '76ers', 2: 'Bucks', 3: 'Bulls', 4: 'Cavaliers', 5: 'Celtics',
     6: 'Clippers', 7: 'Grizzlies', 8: 'Hawks', 9: 'Heat', 10: 'Hornets',
     11: 'Jazz', 12: 'Kings', 13: 'Knicks', 14: 'Lakers', 15: 'Magic',
     16: 'Mavericks', 17: 'Nets', 18: 'Nuggets', 19: 'Pacers', 20: 'Pelicans',
     21: 'Pistons', 22: 'Raptors', 23: 'Rockets', 24: 'Spurs', 25: 'Suns',
     26: 'Thunder', 27: 'Timberwolves', 28: 'Trail Blazers', 29: 'Warriors', 30: 'Wizards'}

cities = {t[1]: "Philadelphia", t[2]: "Milwaukee", t[3]: "Chicago", t[4]: "Cleveland", t[5]: "Boston",
          t[6]: "Los Angeles", t[7]: "Memphis", t[8]: "Atlanta", t[9]: "Miami", t[10]: "Charlotte",
          t[11]: "Utah", t[12]: "Sacramento", t[13]: "New York", t[14]: "Los Angeles", t[15]: "Orlando",
          t[16]: "Dallas", t[17]: "Brooklyn", t[18]: "Denver", t[19]: "Indiana", t[20]: "New Orleans",
          t[21]: "Detroit", t[22]: "Toronto", t[23]: "Houston", t[24]: "San Antonio", t[25]: "Phoenix",
          t[26]: "Oklahoma City", t[27]: "Minnesota", t[28]: "Portland", t[29]: "Golden State", t[30]: "Washington"}

# conference identification to skip the need for if statements in the playoffs
conf_id = {}
for _tm_ in cities:
    if _tm_ in east:
        conf_id[_tm_] = 'Eastern'
    else:
        conf_id[_tm_] = 'Western'

# Below are the (subjective) top 3 players from each team. (2017-2018 season)
# Beside each player are a list of shot percentages (2pt, 3pt) and then shot tendencies (2PA, 3PA)
# **if they shoot nearly no 3's, tendency is 1,0**
# player pass tendencies have been added so that mediocre players are not dropping all-star stats.
# **third item in shooting percentages**
# 0-.50 = less likely to shoot, .51-1 = more likely to shoot
# the usage rates also help this **separate dictionary below**
# overall rating added (4th item in each player list)
top_3 = {t[1]: [["Joel Embiid", [.527, .308, .75], [13.4, 3.4], 93],
                ["Ben Simmons", [.551, .01, .40], [12.2, 0.1], 88],
                ["JJ Redick", [.504, .420, .67], [6, 6.6], 81]],
         t[2]: [["Giannis Antetokounmpo", [.554, .307, .70], [16.8, 1.9], 96],
                ["Eric Bledsoe", [.550, .349, .55], [8.5, 4.9], 85],
                ["Khris Middleton", [.517, .359, .65], [10.5, 5], 83]],
         t[3]: [["Lauri Markkanen", [.497, .362, .75], [6.8, 5.9], 83],
                ["Zach Lavine", [.405, .341, .75], [9.7, 5.1], 86],
                ["Kris Dunn", [.457, .321, .50], [10.2, 2.6], 77]],
         t[4]: [["LeBron James", [.603, .367, .50], [8.7, 5], 96],
                ["Kevin Love", [.494, .415, .80], [6.8, 5.6], 85],
                ["Jeff Green", [.540, .312, .70], [5.7, 2.2], 77]],
         t[5]: [["Kyrie Irving", [.541, .408, .65], [11.3, 6.8], 92],
                ["Gordon Hayward", [.506, .398, .67], [10.7, 5.1], 86],
                ["Jayson Tatum", [.526, .324, .70], [10, 3.7], 84]],
         t[6]: [["DeAndre Jordan", [.645, 0, .70], [1, 0], 83],
                ["Lou Williams", [.484, .359, .61], [10.3, 6.6], 85],
                ["Tobias Harris", [.501, .414, .70], [10.7, 5.3], 85]],
         t[7]: [["Mike Conley", [.440, .312, .70], [7.6, 6.4], 87],
                ["Marc Gasol", [.456, .341, .70], [9.8, 4.4], 83],
                ["Tyreke Evans", [.482, .399, .60], [10.1, 5.5], 77]],
         t[8]: [["Dennis Schroder", [.48, .29, .58], [13.2, 3.9], 77],
                ["John Collins", [.598, .340, .75], [6.8, .6], 84],
                ["Kent Bazemore", [.438, .394, .60], [6.2, 4.2], 76]],
         t[9]: [["Goran Dragic", [.481, .37, .60], [10.3, 4], 80],
                ["Hassan Whiteside", [.538, 1, .77], [1, 0], 83],
                ["Dwyane Wade", [.447, .22, .58], [9.8, 2], 81]],
         t[10]: [["Kemba Walker", [.469, .384, .60], [9.5, 7.5], 88],
                 ["Dwight Howard", [.559, .143, .75], [11.1, .1], 80],
                 ["Jeremy Lamb", [.495, .370, .70], [7.2, 3.2], 79]],
         t[11]: [["Donovan Mitchell", [.502, .340, .69], [10.2, 7], 87],
                 ["Rudy Gobert", [.622, 0, .70], [1, 0], 89],
                 ["Joe Ingles", [.516, .44, .47], [3.1, 5.7], 78]],
         t[12]: [["Zach Randolph", [.503, .347, .70], [10.4, 2.5], 78],
                 ["Buddy Hield", [.457, .431, .80], [6.6, 5.1], 83],
                 ["De'Aaron Fox", [.436, .307, .53], [8.8, 2.1], 83]],
         t[13]: [["Kristaps Porzingis", [.494, .395, .87], [13.7, 4.8], 88],
                 ["Tim Hardaway Jr.", [.515, .317, .74], [7.8, 7.2], 77],
                 ["Enes Kanter", [.594, 0, .76], [1, 0], 81]],
         t[14]: [["Brandon Ingram", [.483, .39, .65], [11.1, 1.8], 81],
                 ["Lonzo Ball", [.42, .305, .40], [5.1, 5.7], 80],
                 ["Kyle Kuzma", [.511, .366, .75], [7.9, 5.6], 83]],
         t[15]: [["Evan Fournier", [.516, .379, .70], [8.2, 5.9], 77],
                 ["Aaron Gordon", [.497, .336, .73], [9, 5.9], 80],
                 ["Nikola Vucevic", [.527, .314, .65], [11.1, 3.6], 85]],
         t[16]: [["Dennis Smith Jr.", [.435, .313, .57], [9.9, 4.9], 77],
                 ["Harrison Barnes", [.487, .357, .75], [11.4, 4.3], 79],
                 ["Wesley Matthews", [.441, .381, .65], [4.7, 6.4], 76]],
         t[17]: [["D'Angelo Russell", [.477, .324, .55], [8.2, 5.8], 87],
                 ["Rondae Hollis-Jefferson", [.491, .241, .70], [9.8, 0.8], 75],
                 ["DeMarre Carroll", [.457, .371, .70], [5.4, 5.4], 77]],
         t[18]: [["Nikola Jokic", [.538, .396, .50], [9.8, 3.7], 92],
                 ["Gary Harris", [.553, .396, .70], [7.7, 5.9], 79],
                 ["Jamal Murray", [.502, .378, .65], [7.7, 5.4], 82]],
         t[19]: [["Victor Oladipo", [.528, .371, .68], [12.1, 5.8], 87],
                 ["Myles Turner", [.519, .357, .75], [7.4, 2.4], 82],
                 ["Bojan Bogdanovic", [.534, .402, .80], [5.9, 4.8], 83]],
         t[20]: [["Anthony Davis", [.558, .340, .80], [17.3, 2.2], 94],
                 ["DeMarcus Cousins", [.53, .354, .65], [11.9, 6.1], 89],
                 ["Jrue Holiday", [.557, .337, .53], [11, 4.4], 86]],
         t[21]: [["Blake Griffin", [.473, .348, .60], [11.3, 5.4], 87],
                 ["Andre Drummond", [.536, .001, .67], [11.2, 0.1], 87],
                 ["Reggie Jackson", [.475, .308, .53], [9, 3.8], 80]],
         t[22]: [["DeMar DeRozan", [.494, .310, .65], [14.1, 3.6], 88],
                 ["Kyle Lowry", [.474, .399, .50], [4.5, 7.6], 84],
                 ["Jonas Valanciunas", [.587, .405, .70], [7.9, 1], 82]],
         t[23]: [["James Harden", [.531, .367, .57], [10.1, 10], 96],
                 ["Chris Paul", [.532, .380, .46], [7.3, 6.5], 87],
                 ["Eric Gordon", [.544, .359, .85], [5.3, 8.8], 77]],
         t[24]: [["Kawhi Leonard", [.529, .380, .70], [12.5, 5.2], 95],
                 ["LaMarcus Aldridge", [.526, .293, .70], [16.8, 1.2], 87],
                 ["Rudy Gay", [.516, .314, .75], [7.3, 2.1], 81]],
         t[25]: [["Devin Booker", [.46, .383, .70], [12.4, 7.1], 88],
                 ["TJ Warren", [.523, .222, .82], [15, 1.4], 81],
                 ["Josh Jackson", [.464, .263, .75], [9.3, 2.8], 77]],
         t[26]: [["Russel Westbrook", [.485, .298, .50], [17, 4.1], 93],
                 ["Paul George", [.454, .401, .65], [9.3, 7.7], 90],
                 ["Carmelo Anthony", [.437, .357, .80], [8.9, 6.1], 76]],
         t[27]: [["Karl-Anthony Towns", [.585, .421, .70], [10.8, 3.5], 91],
                 ["Jimmy Butler", [.509, .35, .65], [12.2, 3.4], 88],
                 ["Andrew Wiggins", [.475, .331, .70], [11.8, 4.1], 80]],
         t[28]: [["Damian Lillard", [.501, .361, .60], [10.8, 8.6], 92],
                 ["CJ McCollum", [.465, .397, .65], [12.7, 5.9], 85],
                 ["Jusuf Nurkic", [.508, .001, .70], [11.9, 0.1], 85]],
         t[29]: [["Stephen Curry", [.595, .423, .60], [7.1, 9.8], 95],
                 ["Kevin Durant", [.565, .419, .63], [11.9, 6.1], 95],
                 ["Klay Thompson", [.527, .440, .70], [9, 7.1], 88]],
         t[30]: [["John Wall", [.436, .371, .50], [12.2, 4.1], 89],
                 ["Bradley Beal", [.507, .375, .65], [11.6, 6.5], 88],
                 ["Otto Porter Jr.", [.537, .441, .71], [7.4, 4.1], 81]]}

# personal usage rates for each player
usage_r = {'76ers': [.34, .33, .21], 'Bucks': [.35, .28, .30], 'Bulls': [.20, .29, .30],
           'Cavaliers': [.44, .20, .14], 'Celtics': [.31, .29, .25], 'Clippers': [.15, .35, .26],
           'Grizzlies': [.28, .27, .29], 'Hawks': [.35, .12, .20], 'Heat': [.29, .15, .23],
           'Hornets': [.34, .19, .18], 'Jazz': [.28, .15, .20], 'Kings': [.20, .16, .23],
           'Knicks': [.23, .23, .15], 'Lakers': [.25, .29, .20], 'Magic': [.23, .24, .24],
           'Mavericks': [.30, .24, .18], 'Nets': [.29, .18, .18], 'Nuggets': [.32, .22, .23],
           'Pacers': [.32, .15, .15], 'Pelicans': [.30, .36, .32], 'Pistons': [.38, .21, .28],
           'Raptors': [.36, .33, .15], 'Rockets': [.47, .36, .17], 'Spurs': [.32, .28, .14],
           'Suns': [.34, .23, .20], 'Thunder': [.50, .30, .20], 'Timberwolves': [.24, .33, .25],
           'Trail Blazers': [.40, .30, .20], 'Warriors': [.34, .33, .25], 'Wizards': [.40, .32, .18]}

# below are the players in a dictionary for stat keeping.
# The order of stats is [[2pt made, 2pt att],[3pt made, 3pt att],assists,games played]
stats = {}
for t_e_a_m in top_3:
    for p_layer in top_3[t_e_a_m]:
        stats[p_layer[0]] = [[0, 0], [0, 0], 0, 0]

# below are team stats
# ([[W,L],[points scored,points allowed],games played])
t_stats = {}
for t_e_a_m in top_3:
    t_stats[t_e_a_m] = [[0, 0], [0, 0], 0]

# used to identify what team each player is on
team_id = {}
for t_e_a_m in top_3:
    for p_layer in top_3[t_e_a_m]:
        team_id[p_layer[0]] = t_e_a_m

# used for trading, teams cannot decline trades when set to true
force_trades = False


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
        self.force_str = StringVar()
        self.force_str.set('Forced Trades is off')
        self.force_b = Button(self.b_frame, textvariable=self.force_str, bg='red',
                              fg='white', command=lambda: self.toggle_forced_trades())
        self.force_b.pack(side=TOP)

    def team_clicked(self, name):
        self.intro.set('Favorite Team: The ' + name)
        self.info.set('Are you sure you want to be the manager of the ' + name + '?')
        if self.confirm_b.winfo_manager() == '':
            self.confirm_b.pack(side=TOP)
        self.team = name

    def off_season(self):
        clear_root(self.root)
        Season(self.root, self.team)

    def toggle_forced_trades(self):
        global force_trades
        if not force_trades:
            self.force_b.config(bg='green')
            self.force_str.set('Forced Trades is on')
            force_trades = True
        else:
            self.force_b.config(bg='red')
            self.force_str.set('Forced Trades is off')
            force_trades = False


class Trades:
    """used for making trades during the season"""
    def __init__(self, root, team):
        self.root = root
        self.root.configure(bg='grey')
        self.team = team
        self.l_frame = Frame(self.root, bg='white')
        self.m_frame = Frame(self.root, bg='white')
        self.r_frame = Frame(self.root, bg='white')
        self.l_frame.pack(side=LEFT)
        self.m_frame.pack(side=LEFT)
        self.r_frame.pack(side=LEFT)
        self.str_v = StringVar()
        self.img_1 = PhotoImage(file='images/' + self.team + '_logo.png')
        self.t_1_lbl = Label(self.m_frame, bg='white', image=self.img_1)
        self.t_1_lbl.pack(side=TOP, padx=100)
        self.lbl = Label(self.m_frame, bg='white', fg='black', textvariable=self.str_v)
        self.lbl.pack(side=TOP)
        self.variable = StringVar()
        self.variable.set([t[x] for x in range(1, 31) if t[x] != self.team][0])
        self.w = OptionMenu(self.m_frame, self.variable, *[t[x] for x in range(1, 31) if t[x] != self.team],
                            command=lambda tm=self.variable.get(): self.disp_team(tm))
        self.w.pack(side=TOP)
        self.img_2 = PhotoImage(file='images/' + self.variable.get() + '_logo.png')
        self.t_2_lbl = Label(self.m_frame, bg='white', image=self.img_2)
        self.t_2_lbl.pack(side=TOP)
        self.b_list = []
        self.selected_buttons = []
        self.img_list = []
        self.b1 = ''
        self.b2 = ''
        self.b3 = ''
        self.b4 = ''
        self.b5 = ''
        self.b6 = ''
        self.declined_trades = []
        self.disp_team(self.variable.get())
        self.trade_btn = Button(self.m_frame, text='Trade', command=lambda: self.player_swap())
        self.trade_btn.pack(side=TOP)
        self.done_btn = Button(self.m_frame, text='Done', bg='red', fg='white',
                               command=lambda: self.goto_season())
        self.done_btn.pack(side=TOP)

    def disp_team(self, team):
        self.img_2 = PhotoImage(file='images/' + team + '_logo.png')
        self.t_2_lbl.configure(image=self.img_2)
        for btn in self.b_list:
            btn[0].destroy()
        del self.selected_buttons
        del self.b_list
        self.b_list = []
        self.selected_buttons = []
        for item in self.img_list:
            self.img_list.remove(item)
        for _tm, frame, pad in [(self.team, self.l_frame, (260, 0)), (team, self.r_frame, (0, 260))]:
            for widget in frame.winfo_children():
                widget.destroy()
            for player in top_3[_tm]:
                p_name = player[0].split()
                try:
                    self.img_list.append(PhotoImage(file='images/' + p_name[0][0] + '_' + p_name[1] + '.png'))
                except TclError:
                    self.img_list.append(PhotoImage(file='images/red x 2.png'))
                self.b_list.append((Button(frame, image=self.img_list[-1], bg='white', text=player[0], borderwidth=5),
                                    player[0]))
                lbl = Label(frame, text=stats_str(player[0]), bg='white')
                self.b_list[-1][0].pack(side=TOP, padx=pad)
                lbl.pack(side=TOP, padx=pad)
        self.b1 = self.b_list[0][0]
        self.b2 = self.b_list[1][0]
        self.b3 = self.b_list[2][0]
        self.b4 = self.b_list[3][0]
        self.b5 = self.b_list[4][0]
        self.b6 = self.b_list[5][0]
        self.b1.configure(command=lambda _btn=self.b1: self.toggle_selection(_btn))
        self.b2.configure(command=lambda _btn=self.b2: self.toggle_selection(_btn))
        self.b3.configure(command=lambda _btn=self.b3: self.toggle_selection(_btn))
        self.b4.configure(command=lambda _btn=self.b4: self.toggle_selection(_btn))
        self.b5.configure(command=lambda _btn=self.b5: self.toggle_selection(_btn))
        self.b6.configure(command=lambda _btn=self.b6: self.toggle_selection(_btn))
        self.str_v.set('Trading with: ' + team)

    def toggle_selection(self, _btn):
        name = _btn.cget('text')
        if name not in self.selected_buttons:
            self.selected_buttons.append(name)
            _btn.configure(bg='green')
        else:
            self.selected_buttons.remove(name)
            _btn.configure(bg='white')

    def player_swap(self):
        if self.trade_accepted():
            l_1 = [player for player in self.selected_buttons if team_id[player] == self.team]
            l_2 = [player for player in self.selected_buttons if team_id[player] != self.team]
            t_list = [[l_1[i], l_2[i]] for i in range(len(l_1))]
            t_1 = ''
            t_2 = ''
            for _trade_ in t_list:
                p_1 = _trade_[0]
                p_2 = _trade_[1]
                t_1 = team_id[p_1]
                t_2 = team_id[p_2]
                i_1 = team_index(p_1)
                i_2 = team_index(p_2)
                temp_usage = usage_r[t_1][i_1]
                usage_r[t_1][i_1] = usage_r[t_2][i_2]
                usage_r[t_2][i_2] = temp_usage
                temp_top = top_3[t_1][i_1][:]
                top_3[t_1][i_1] = top_3[t_2][i_2][:]
                top_3[t_2][i_2] = temp_top
                temp_id = t_1
                team_id[p_1] = t_2
                team_id[p_2] = temp_id
            adjust_usage(t_1)
            adjust_usage(t_2)
            self.disp_team(t_2)
        else:
            self.str_v.set('Trade declined.')
            self.declined_trades.append(sorted(self.selected_buttons))

    def trade_accepted(self):
        if sorted(self.selected_buttons) in self.declined_trades:
            return False
        t_1_ps = 0
        t_2_ps = 0
        t_1_ovr = 0
        t_2_ovr = 0
        for player in self.selected_buttons:
            if team_id[player] == self.team:
                t_1_ps += 1
                t_1_ovr += top_3[self.team][team_index(player)][3]
            else:
                t_2_ps += 1
                t_2_ovr += top_3[team_id[player]][team_index(player)][3]
        if t_1_ps != t_2_ps:
            return False
        if force_trades:
            return True
        if t_1_ovr + 5 >= t_2_ovr:
            return True
        return False

    def goto_season(self):
        clear_root(self.root)
        Season(self.root, self.team)


class Season:
    def __init__(self, root, team):
        self.team = team
        self.root = root
        self.lbl = Label(self.root, text='Hello there.')
        self.lbl.pack(side=TOP)
        self.trade_btn = Button(self.root, text='Trade', bg='blue', fg='white',
                                command=lambda: self.trader())
        self.trade_btn.pack(side=TOP)

    def trader(self):
        clear_root(self.root)
        Trades(self.root, self.team)
        self.repack()

    def repack(self):
        return


def adjust_usage(team):
    """adjusts the usage rate of each player on a team after a trade"""
    while sum(usage_r[team]) >= 1:
        for i in range(3):
            usage_r[team][i] = usage_r[team][i] - .01


def stats_str(player):
    """returns the stats of the player in a str"""
    _st_ = stats[player]
    if _st_[3] != 0:
        ppg = round((_st_[0][0] * 2 + _st_[1][0] * 3) / _st_[3], 1)
        apg = round((_st_[2]) / _st_[3], 1)
        if (_st_[0][1] + _st_[1][1]) == 0:
            fgp = 0
        else:
            fgp = round(((_st_[0][0] + _st_[1][0]) / (_st_[0][1] + _st_[1][1])) * 100, 1)
        if _st_[1][1] == 0:
            tpp = 0
        else:
            tpp = round((_st_[1][0] / _st_[1][1]) * 100, 1)
        gp = _st_[3]
    else:
        ppg = 0
        apg = 0
        fgp = 0
        tpp = 0
        gp = 0
    c = str(ppg) + ' PPG ' + str(apg) + ' APG ' + str(fgp) + ' FG% ' + str(tpp) + ' 3P% ' + str(gp) + ' Games Played '
    try:
        c = c + str(top_3[team_id[player]][team_index(player)][3]) + ' OVR'
    except IndexError:
        c = c + '?? OVR'
    return c


def team_index(player):
    """returns the index of a player in their top_3 list"""
    _tm = top_3[team_id[player]]
    for i in range(len(_tm)):
        if _tm[i][0] == player:
            return i


def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()


def toggle_fullscreen(r):
    r.attributes('-fullscreen', not r.attributes('-fullscreen'))


def main():
    root = Tk()
    Start(root)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.attributes("-fullscreen", True)
    root.bind('<Escape>', lambda event, r=root: toggle_fullscreen(r))
    root.mainloop()


"""## NBA game
def game(team_1, team_2):
    score_1 = 0
    score_2 = 0
    scores = [score_1, score_2]
    teams = [team_1, team_2]
    role_player = [[.41, .33], [4.1, 1.3]]
    for team in teams:
        t_stats[team][2] += 1
        for player in top_3[team]:
            stats[player[0]][3] += 1
    for quarter in range(1, 5):
        time = 12 * 60
        possession = quarter % 2
        while time > 0:
            pl = play(teams[possession], top_3[teams[possession]], role_player)
            if pl[0] == True:
                if pl[1] == 2:
                    scores[possession] += 2
                else:
                    scores[possession] += 3
            time -= 14
            possession = (possession + 1) % 2
    if scores[0] == scores[1]:
        scores = overtime(team_1, team_2, scores[0])
    ##    players = []
    ##    for team in teams:
    ##        for player in top_3[team]:
    ##            players.append(player[0])
    ##    for player in players:
    ##        pts = stats[player][0][0] * 2 + stats[player][1][0] * 3
    ##        ast = stats[player][2]
    ##        print(player,pts,"pts",ast,'ast')
    return scores

## determines whether the shooter shoots a two or three pointer
def shot_type(tendencies):
    _2pt_ = tendencies[0]
    _3pt_ = tendencies[1]
    if dec(_2pt_ / (_2pt_ + _3pt_)) == True:
        return _2pt_
    return _3pt_

## returns a true or false depending on a given probability
def dec(probability):
    return random.random() < probability

##determines shooter based on usage rates
def sh(rates):
    zero = range(0,int(100*rates[0]))
    one = range(int(rates[0]*100),int(100*rates[0]+100*rates[1]))
    two = range(int(100*rates[0]+100*rates[1]),int(100*rates[0]+100*rates[1]+100*rates[2]))
    three = range(int(100*rates[0]+100*rates[1]+100*rates[2]),101)
    rd = int(100*random.random())
    if rd in zero:
        return 0
    elif rd in one:
        return 1
    elif rd in two:
        return 2
    else:
        return 3

## determines a made or missed shot, what type of shot it was, who shot it, etc
def play(team,teamlist,rp):
    shooter = sh(usage_r[team])
    ## 0 = 1st option, 1 = 2nd option, 2 = 3rd option, 3 = role player
    if shooter == 3:
        _shot_ = rp[1].index(shot_type(rp[1]))
        make = dec(rp[0][_shot_])
        if make == True:
            if _shot_ == 0:
                return [True,2]
            else:
                return [True,3]
        else:
            if _shot_ == 0:
                return [False,2]
            else:
                return [False,3]
    else:
        p_stats = teamlist[shooter]
        if dec(p_stats[1][2]) == False:
            _shot_ = rp[1].index(shot_type(rp[1]))
            make = dec(rp[0][_shot_])
            if make == True:
                stats[p_stats[0]][2] += 1
                if _shot_ == 0:
                    return [True,2]
                else:
                    return [True,3]
            else:
                if _shot_ == 0:
                    return [False,2]
                else:
                    return [False,3]
        else:
            _shot_ = p_stats[2].index(shot_type(p_stats[2]))
            make = dec(p_stats[1][_shot_])
            if make == True:
                if _shot_ == 0:
                    stats[p_stats[0]][0][0] += 1
                    stats[p_stats[0]][0][1] += 1
                    return [True,2]
                else:
                    stats[p_stats[0]][1][0] += 1
                    stats[p_stats[0]][1][1] += 1
                    return [True,3]
            else:
                if _shot_ == 0:
                    stats[p_stats[0]][0][1] += 1
                    return [False,2]
                else:
                    stats[p_stats[0]][1][1] += 1
                    return [False,3]

## tied games settled in overtime
def overtime(t1,t2,score):
    teams = [t1,t2]
    score_1 = score
    score_2 = score
    scores = [score_1,score_2]
    role_player = [[.41,.33],[4.1,1.3]]
    while scores[0] == scores[1]:
        time = 5 * 60
        possession = 1
        while time > 0:
            pl = play(teams[possession],top_3[teams[possession]],role_player)
            if pl[0] == True:
                if pl[1] == 2:
                    scores[possession] += 2
                else:
                    scores[possession] += 3
            time -= 14
            possession = (possession + 1) % 2
    return scores

main()

schedules = {'76ers':[t[2]]*4+[t[3]]*3+[t[4]]*4+[t[5]]*4+[t[6]]*2+[t[7]]*2+[t[8]]*3+[t[9]]*4+[t[10]]*4+[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*3+[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*3+[t[20]]*2+[t[21]]*4+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Bucks':[t[3]]*4+[t[4]]*4+[t[5]]*4+[t[6]]*2+[t[7]]*2+[t[8]]*3+[t[9]]*3+[t[10]]*4+[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*3+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*4+[t[22]]*3+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Bulls':[t[4]]*4+[t[5]]*4+[t[6]]*2+[t[7]]*2+[t[8]]*3+[t[9]]*4+[t[10]]*4+[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*3+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*4+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*3,\
                 'Cavaliers':[t[5]]*3+[t[6]]*2+[t[7]]*2+[t[8]]*4+[t[9]]*3+[t[10]]*3+[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*4+[t[22]]*3+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Celtics':[t[6]]*2+[t[7]]*2+[t[8]]*4+[t[9]]*3+[t[10]]*3+[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*3+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Clippers':[t[7]]*4+[t[8]]*2+[t[9]]*2+[t[10]]*2+[t[11]]*4+[t[12]]*4+[t[13]]*2+[t[14]]*4+[t[15]]*2+[t[16]]*3+[t[17]]*2+[t[18]]*3+[t[19]]*2+[t[20]]*4+[t[21]]*2+[t[22]]*2+[t[23]]*4+[t[24]]*3+[t[25]]*4+[t[26]]*3+[t[27]]*4+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Grizzlies':[t[8]]*2+[t[9]]*2+[t[10]]*2+[t[11]]*3+[t[12]]*3+[t[13]]*2+[t[14]]*4+[t[15]]*2+[t[16]]*4+[t[17]]*2+[t[18]]*4+[t[19]]*2+[t[20]]*4+[t[21]]*2+[t[22]]*2+[t[23]]*4+[t[24]]*4+[t[25]]*4+[t[26]]*4+[t[27]]*3+[t[28]]*4+[t[29]]*3+[t[30]]*2,\
                 'Hawks':[t[9]]*4+[t[10]]*4+[t[11]]*2+[t[12]]*2+[t[13]]*3+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*4+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Heat':[t[10]]*4+[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*4+[t[22]]*3+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Hornets':[t[11]]*2+[t[12]]*2+[t[13]]*4+[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*3+[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*3+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Jazz':[t[12]]*3+[t[13]]*2+[t[14]]*3+[t[15]]*2+[t[16]]*3+[t[17]]*2+[t[18]]*4+[t[19]]*2+[t[20]]*4+[t[21]]*2+[t[22]]*2+[t[23]]*4+[t[24]]*4+[t[25]]*4+[t[26]]*4+[t[27]]*4+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Kings':[t[13]]*2+[t[14]]*4+[t[15]]*2+[t[16]]*4+[t[17]]*2+[t[18]]*4+[t[19]]*2+[t[20]]*4+[t[21]]*2+[t[22]]*2+[t[23]]*3+[t[24]]*4+[t[25]]*4+[t[26]]*4+[t[27]]*3+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Knicks':[t[14]]*2+[t[15]]*4+[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*3+[t[20]]*2+[t[21]]*3+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*3,\
                 'Lakers':[t[15]]*2+[t[16]]*4+[t[17]]*2+[t[18]]*4+[t[19]]*2+[t[20]]*3+[t[21]]*2+[t[22]]*2+[t[23]]*4+[t[24]]*3+[t[25]]*4+[t[26]]*4+[t[27]]*4+[t[28]]*3+[t[29]]*4+[t[30]]*2,\
                 'Magic':[t[16]]*2+[t[17]]*4+[t[18]]*2+[t[19]]*3+[t[20]]*2+[t[21]]*3+[t[22]]*3+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Mavericks':[t[17]]*2+[t[18]]*4+[t[19]]*2+[t[20]]*4+[t[21]]*2+[t[22]]*2+[t[23]]*4+[t[24]]*4+[t[25]]*3+[t[26]]*4+[t[27]]*4+[t[28]]*3+[t[29]]*4+[t[30]]*2,\
                 'Nets':[t[18]]*2+[t[19]]*4+[t[20]]*2+[t[21]]*4+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*3,\
                 'Nuggets':[t[19]]*2+[t[20]]*3+[t[21]]*2+[t[22]]*2+[t[23]]*3+[t[24]]*4+[t[25]]*3+[t[26]]*4+[t[27]]*4+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Pacers':[t[20]]*2+[t[21]]*4+[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*3,\
                 'Pelicans':[t[21]]*2+[t[22]]*2+[t[23]]*4+[t[24]]*4+[t[25]]*3+[t[26]]*3+[t[27]]*4+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Pistons':[t[22]]*4+[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Raptors':[t[23]]*2+[t[24]]*2+[t[25]]*2+[t[26]]*2+[t[27]]*2+[t[28]]*2+[t[29]]*2+[t[30]]*4,\
                 'Rockets':[t[24]]*4+[t[25]]*4+[t[26]]*3+[t[27]]*4+[t[28]]*4+[t[29]]*3+[t[30]]*2,\
                 'Spurs':[t[25]]*4+[t[26]]*4+[t[27]]*3+[t[28]]*3+[t[29]]*4+[t[30]]*2,\
                 'Suns':[t[26]]*3+[t[27]]*4+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Thunder':[t[27]]*4+[t[28]]*4+[t[29]]*4+[t[30]]*2,\
                 'Timberwolves':[t[28]]*4+[t[29]]*3+[t[30]]*2,\
                 'Trail Blazers':[t[29]]*3+[t[30]]*2,\
                 'Warriors':[t[30]]*2,\
                 'Wizards':[]}
for team in schedules:
    schedule = schedules[team]
    for opp in schedule:
        g = game(team,opp)
        for i in range(2):
            t_stats[team][1][i] += g[i]
            t_stats[opp][1][i] += g[(i+1) % 2]
        if g[0] > g[1]:
            t_stats[team][0][0] += 1
            t_stats[opp][0][1] += 1
        elif g[0] < g[1]:
            t_stats[team][0][1] += 1
            t_stats[opp][0][0] += 1"""

main()
