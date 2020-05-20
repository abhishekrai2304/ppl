class ErrorInMyCode(Exception):
    def __init__(self, d):
        self.data = d

    def __str__(self):
        return  repr(self.data)
try:
    raise ErrorInMyCode(2000)
except ErrorInMyCode as ae:
    print("Received error:", ae.data)