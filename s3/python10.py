# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:41:27 2024

@author: cerpc
"""

class Fish:
    def swim(self):
        print("Fish is swimming")
    def eat(self):
        print("Fish is eating")
        
fish = Fish()
fish.swim()
fish.eat()



class Game:
    def __init__(self, name):
        self.name = name
        
    def start(self):
        print(self.name, "has started")
        
    def stop(self):
        print(self.name, "has stopped")
        
        
game = Game("Counter Strike")
game.start()
game.stop()