class EventEmitter:
    def __init__(self):
        # event handler object contains arrays of lambdas || functions
        self.event_handlers = {}
        self.default_handler = None

    def emit(self, event_name):
        handlers = self.event_handlers.get(event_name)
        if handlers:
            for handler in handlers:
                handler(event_name)
        else:
            if self.default_handler:
                self.default_handler("default event")

    def listen(self, event_name, callback):
        if self.event_handlers.get(event_name):
            self.event_handlers[event_name].append(callback)
        else: 
            self.event_handlers[event_name] = [callback]

    def default(self, callback):
        if self.default_handler:
            return print("ERROR: Default Handler Already Exists")
        else: 
            self.default_handler = callback


Input = EventEmitter()