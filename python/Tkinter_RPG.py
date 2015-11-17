import tkinter
import random
import time

classes = ['warrior','mage','assassin', 'archer']

def start():
    name = input('What is your name?')
    job = input('What job will you have?(assassin, warrior, mage, archer)')
    me = Job(name,job)
class Job():
    def __init__(self,name,job):
        self.stats = {
            'job': job,
            'name': name
        }
        if stats['job'] == 'warrior':
            pass
        elif stats['job'] == 'mage'

