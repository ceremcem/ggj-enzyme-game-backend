__author__ = 'ceremcem'

from aktos_dcs import *

class Test(Actor):
    def action(self):
        while True:
            self.send({'LedPanelMessage': {'message': 'mesut' }})
            sleep(2)

ProxyActor(brokers="192.168.1.59:5012:5013")
Test()
wait_all()