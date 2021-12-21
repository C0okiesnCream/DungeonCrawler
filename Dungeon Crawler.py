#imports
import colorama
import json
import random
from time import sleep
from pynput import keyboard

#classes
class testMob():
    def __init__(self, health, head, chest, hands, legs, feet, damage, weapon, target, roomXY, dungeonXY, dead):
        self.health = health
        self.head = head
        self.chest = chest
        self.hands = hands
        self.legs = legs
        self.feet = feet
        self.damage = damage
        self.weapon = weapon
        self.target = target
        self.roomXY = roomXY
        self.dungeonXY = dungeonXY
        self.dead = dead

    def attack(self):
        #variables
        s = self
        damage = 0
        
        #making sure that the monster has a weapon
        if s.weapon != None:
            damage = s.damage = s.weapon.damage
        else:
            damage = s.damage
        
        #should return the damage from the if-else above
        return damage
    
    def deathCheck(self):
        s = self
        if s.health < 1:
            s.dead = 1
            