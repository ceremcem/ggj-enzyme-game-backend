__author__ = 'ceremcem'
from aktos_dcs import *
class TestHealth(Actor):
    def action(self):
        while True:
            print "sending..."
            self.send({'HealthMessage': {'val': True}})
            sleep(2)
            self.send({'HealthMessage': {'val': False}})
            sleep(2)

ProxyActor()
TestHealth()
wait_all()