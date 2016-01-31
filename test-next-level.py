__author__ = 'ceremcem'
from aktos_dcs import *
class TestLevel(Actor):
    def action(self):
        while True:
            print "sending..."
            self.send({'LevelMessage': {'val': True}})
            sleep(5)

ProxyActor()
TestLevel()
wait_all()