__author__ = 'ceremcem'


from aktos_dcs import *

class Enzim1(Actor):
    def handle_S(self, msg):
        sleep(1)
        self.send({'A': {}})

class Enzim2(Actor):
    def action(self):
        self.waiting_for = ['A', 'E']
        self.got = []

    def handle_A(self, msg):
        self.got.append('A')
        self.check_product()

    def handle_E(self, msg):
        self.got.append('E')
        self.check_product()

    def check_product(self):
        if set(self.got) == set(self.waiting_for):
            self.got.remove('A')
            self.got.remove('E')
            self.send({'B': {}})

class Enzim3(Actor):
    def handle_B(self, msg):
        sleep(1)
        self.send({'C': {}})

class Enzim4(Actor):
    def handle_C(self, msg):
        sleep(1)
        self.send({'D': {}})

class Enzim5(Actor):
    def handle_D(self, msg):
        sleep(1)
        self.send({'E': {}})
        self.send({'Ure': {}})


class Observer(Actor):
    def receive(self, msg):
        topics = ['A', 'B', 'C', 'D', 'E', 'S', 'Ure']
        for i, j in msg["payload"].items():
            if i in topics:
                print "Produced: ", i
                try:
                    self.products[i] += 1
                except KeyError:
                    self.products[i] = 1
                panel_str = ""
                for k in topics:
                    try:
                        panel_str += "" + str(self.products[k]) + "."
                    except:
                        panel_str += "" + str(0) + "."

                panel_str = panel_str.replace('ure', 'u')
                self.send({'LedPanelMessage': {'message': unicode(panel_str)}})


ProxyActor(brokers="192.168.1.59:5012:5013")
Enzim1()
Enzim2()
Enzim3()
Enzim4()
Enzim5()
Observer()
Actor().send({'S': {}})
Actor().send({'E': {}})
wait_all()