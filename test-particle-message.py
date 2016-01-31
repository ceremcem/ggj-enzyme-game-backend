__author__ = 'ceremcem'

from aktos_dcs import *
class TestParticle(Actor):
    def handle_ParticleMessage(self, msg):
        print "got particle message: ", msg
ProxyActor()
TestParticle()
wait_all()