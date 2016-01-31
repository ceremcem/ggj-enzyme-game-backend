from aktos_dcs import * 
import calendar 

class Remaining(Actor):
    def action(self): 
        while True: 
            remaining = 1456934400 - calendar.timegm(time.gmtime()) 
            remaining = 'left ' +str(remaining) + "s"
            print "remaining: ", remaining
            self.send({'LedPanelMessage': {'message': remaining}})
            sleep(1)

ProxyActor(brokers="192.168.1.59:5012:5013")
Remaining()
wait_all()
