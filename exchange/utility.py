import websocket


ws = websocket.WebSocketApp('wss://api.bitfinex.com/ws/2')
ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "ticker", "symbol": "tBTCUSD"}')
ws.on_message = lambda self, evt: print(evt)
ws.run_forever()
