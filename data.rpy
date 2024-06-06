init -2 python:

    def save_playtime(d):
        renpy.store.playtime += renpy.get_game_runtime()
        renpy.clear_game_runtime()
        d["playtime"] = renpy.store.playtime

    config.save_json_callbacks = [save_playtime]

    class Contact (object):
        def __init__(self, name, job, morale=0, moralemax=10):
            self.name = name
            self.job = job
            self.morale = morale
            self.moralemax = moralemax
    

        def morale_up(self,amount):
            if self.morale == 10:
                self.morale += 0
            else:
                self.morale += amount
            return self.morale

        def morale_down(self,amount):
            if self.morale == 0:
                self.morale -= 0
            else:
                self.morale -= amount
            return self.morale


    class Trait(object):
        def __init__(self, name, amount=0, max=20):
            self.name = name
            self.amount= amount
            self.max = max

        def trait_up(self, amount):
            if self.amount == 20:
                self.amount += 0
            else:
                self.amount += amount
            return self.amount

        def trait_down(self, amount):
            if self.amount == 0:
                self.amount -= 0
            else:
                self.amount -= amount
            return self.amount
