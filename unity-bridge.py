__author__ = 'ceremcem'
from aktos_dcs import *
from aktos_dcs_lib import *

if __name__ == "__main__":
    class TestSocketServerClient(Actor):
        def action(self):
            while True:
                self.send({'SocketServerSendMessage': {'data': "test socket server sending msg\n", "client": "all"}})
                sleep(2)

        def receive(self, msg):
            forward = msg['payload']
            print "forward", forward
            self.send({'SocketServerSendMessage': {'data': pack(forward), "client": "all"}})


        def handle_SocketServerMessage(self, msg):

            print "client sent data: ", msg["data"]
            try:
                msg_dict =  json.loads(msg['data'])
                self.send(msg_dict)
                print "msg forwarded: ", msg_dict
            except:
                pass

    ProxyActor()
    SocketServerActor('0.0.0.0', 1234)
    TestSocketServerClient()
    wait_all()


