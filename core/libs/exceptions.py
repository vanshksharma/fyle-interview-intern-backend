class FyleError(Exception):
    status_code = 400

    def __init__(self, status_code, message):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        res = dict()
        res['message'] = self.message
        return res

class JSONParseException(Exception):
    status_code=400
    def __init__(self, status_code,message):
        Exception.__init__(self)
        self.message=message
        self.status_code=status_code
    
    def to_dict(self):
        res=dict()
        res['message']=self.message
        return res

class DataNotFoundException(Exception):
    status_code=601

    def __init__(self, status_code, message):
        Exception.__init__(self)
        self.message=message
        self.status_code=status_code
    
    def to_dict(self):
        res=dict()
        res['message']=self.message
        return res

class IDValidationException(Exception):
    status_code=400

    def __init__(self, status_code, message):
        Exception.__init__(self)
        self.message=message
        self.status_code=status_code
    
    def to_dict(self):
        res=dict()
        res['message']=self.message
        return res

class PayloadValidationException(Exception):
    status_code=400

    def __init__(self, status_code, message) -> None:
        Exception.__init__(self)
        self.message=message
        self.status_code=status_code
    
    def to_dict(self):
        res=dict()
        res['message']=self.message
        return res