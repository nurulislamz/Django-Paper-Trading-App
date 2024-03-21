from websocket import create_connection
import simplejson as json

class tiingoWebSocket:
    def __init__(self, api_key):
        self.base_url = "wss://api.tiingo.com/"
        self.api_key = api_key
    
        self.subscribe = {
                'eventName':'subscribe',
                'authorization': self.api_key,
                }
        
        self.unsubscribe = {
                'eventName':'unsubscribe',
                'authorization': self.api_key,
                }

    def __test(self):
        ws.send(json.dumps(subscribe))
        for i in range(2):
            print(ws.recv())
            
    def get_live_crypto_data(self):
        ws = create_connection("wss://api.tiingo.com/crypto")
        
        self.subscribe = self.subscribe.add({'eventData' : {'threshold' : 2}})
        
        ws.send(json.dumps(self.subscribe))
        for i in range(2):
            print(ws.recv())

        ws.send(json.dumps(self.unsubscribe))        
        