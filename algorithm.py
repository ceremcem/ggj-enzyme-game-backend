__author__ = 'ceremcem'

from aktos_dcs import *

class DecisionActor(Actor):
    def __init__(self, waiting_for=[]):
        Actor.__init__(self)
        self.waiting_for = waiting_for
        self.got = []

    def check_ok(self):
        if set(self.got) == set(self.waiting_for):
            print "sending destroy message for ", self.waiting_for
            self.send_destroy()
            self.send_health_message(True)
        else:
            print "wrong decision!"
            self.send_health_message(False)
            self.send_uncheck()
        for i in self.waiting_for:
            try:
                self.got.remove(i)
            except:
                pass

    def receive(self, msg):
        payload = msg['payload']

        for i, j in payload.items():
            #print "got ", i, "message..."
            if i in self.waiting_for:
                if i not in self.got:
                    self.got.append(i)
                print "got ", i, "message which I interested in..., got: ", self.got


        if len(self.got) == len(self.waiting_for):
            for i in self.waiting_for:
                if i in self.got:
                    self.check_ok()

    def handle_HealthMessage(self, msg):
        self.got = []

    def send_destroy(self):
        self.send({'ParticleMessage': {'destroy': self.waiting_for}})

    def send_uncheck(self):
        self.send({'ParticleMessage': {'uncheck': self.waiting_for}})

    def send_health_message(self, increase=None):
        self.send({'HealthMessage': {'val': increase}})


#ProxyActor(brokers="192.168.1.59:5012:5013")
ProxyActor()
DecisionActor(waiting_for=['Enzim1', 'S'])
DecisionActor(waiting_for=['Enzim2', 'A', 'E'])
DecisionActor(waiting_for=['Enzim3', 'B'])
DecisionActor(waiting_for=['Enzim4', 'C'])
DecisionActor(waiting_for=['Enzim5', 'D'])
wait_all()