import requests

class StateList:
    def __init__(self, conn):
        self.conn = conn
        self.list = []

    def all(self, use_cache=True):
        if use_cache is False or not self.list:
            url = self.conn.host + "api/states"
            for i in requests.get(url, headers=self.conn.headers).json():
                _domain = None
                _object_id = None
                _name = None
                _attributes = None
                _context = None
                
                if "domain" in i:
                    _domain = i["domain"]
                if "object_id" in i:
                    _object_id = i["object_id"]
                if "name" in i:
                    _name = i["name"]
                if "attributes" in i:
                    _attributes = i["attributes"]
                if "context" in i:
                    _context = i["context"]

                new_state = State(i["state"], i["entity_id"], i["last_updated"], i["last_changed"],
                                    _domain, _object_id, _name, _attributes, _context)
                self.list.append(new_state)

        return self.list

    def clear(self):
        self.list.clear()


class State:
    def __init__(self, state, entity_id, last_updated, last_changed, 
                domain=None, object_id=None, name=None, attributes=None, context=None):
        self.state = state
        self.entity_id = entity_id
        self.last_updated = last_updated
        self.last_changed = last_changed
        self.domain = domain
        self.object_id = object_id
        self.name = name
        self.attributes = attributes
        self.context = context

    def friendly_name(self):
        if "friendly_name" in self.attributes:
            name = self.attributes.get("friendly_name")
        elif self.name:
            name = self.name
        else:
            name = self.entity_id
        return name