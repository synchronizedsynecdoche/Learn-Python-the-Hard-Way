from sys import exit
from random import randint
from sys import argv
script, filename=argv

if filename=="":
    pass
else:
    print "You've found the cheat!"
    LogSlide.finish()
    
class Temple(object):
    
    def enter(self):
        print "You're not supposed to see this"
        #Temple.enter() shouldn't be called
        exit(1)
        
        
class Engine(object):
    
    def __init__(self,scene_map):
        pass
    def play(self):
        pass
    
class Death(Temple):
    def enter(self):
        pass

class GoldRoom(Temple):
    def enter(self):
        pass

class Hallway(Temple):
    def enter(self):
        pass

class HallwayBoobytrapped(Temple):
    def enter(self):
        pass

class SkullRoom(Temple):
    def enter(self):
        pass

class LogSlide(Temple):
    def enter(self):
        pass
    def finish(self):
        print "Congrats, you escaped!"        
    
#create a new map, starting in the room 'hallway'
temple=Temple('hallway')
#create a new game
game=Engine(temple)
#play the game
game.play()
