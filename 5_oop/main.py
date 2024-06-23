class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player_name):
        new_player = Players(player_name, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        if len(self.players) > 0:
            for p in self.players:
                print(f"{p.name}")
        else:
            print("No players")

    def remove_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                print(f"{p.name} 제거 완료 in {self.team_name}")
                return

    def show_xp(self):
        xp_sum = 0
        for p in self.players:
            xp_sum += p.xp
        print(f"{self.team_name}'s total XP = {xp_sum}")

class Players:
    def __init__(self, player_name, team_name):
        self.name = player_name
        self.xp = 1500
        self.team = team_name

###

dboo = Team("dboo")

dboo.add_player('jdb')
dboo.add_player('kkh')
dboo.show_players()
dboo.show_xp()

dboo.remove_player('kkh')
dboo.show_players()
dboo.show_xp()

dboo.remove_player('jdb')
dboo.show_players()
dboo.show_xp()