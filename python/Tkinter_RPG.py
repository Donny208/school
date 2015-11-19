import tkinter
import random
import time

classes = ['warrior','mage','assassin', 'archer']


class Role:
    def __init__(self,name,job):
        self.stats = {
            'job': job.lower(),
            'name': name
        }
        if self.stats['job'] == 'warrior' or self.stats['job'] == 'w':
            self.stats['health'] = 150
            self.stats['job'] = 'warrior'
        elif self.stats['job'] == 'mage' or self.stats['job'] == 'm':
            self.stats['health'] = 100
            self.stats['job'] = 'mage'
            
name = input('What is your name?')
job = input('What job will you have?(warrior, mage)')
me = Role(name,job)
