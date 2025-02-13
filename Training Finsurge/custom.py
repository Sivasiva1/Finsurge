class AgeError:
    def __init__(self, message=" enter a valid input "):
        self.message = message 
try:
    n = -1 
    if n < 0:
        raise AgeError(n)
except:
    a = AgeError()
    print(a.message) 

class VotingError:
    def __init__(self, message=" enter a valid input "):
        self.message = message
try:
    n = -1 
    if n < 25 or n > 60:
        raise AgeError(n)
except:
    a = AgeError()
    print(a.message) 

