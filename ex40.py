#Exercise 40 Modules, Classes and objects

class Song(object):

    def __init__(self,lyrics,rightnow):
        self.lyrics = lyrics
        if rightnow:
            print("Straight away")
            self.sing_me_a_song()



    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy"," bday"," to ","you"],1)

halla_bol = Song(["Karta"," ja"," goal pe goal"],False)


halla_bol.sing_me_a_song()