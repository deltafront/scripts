__author__ = 'charlie'

class Device(object):
    def __init__(self):
        self.id = None
        self.label = None
        self.subscribers = []
        self.subscriptions = []
        self.user_id = None
        self.wifi = {}
