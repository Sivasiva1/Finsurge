
class VotingError(Exception):
    def __init__(self, message=" Not a valid age "):
        self.message = message 
class NonIndian(Exception):
      def __init__(self, message="Anti Indian Not Eligible vor voting "):
        self.message = message
class NoVoter(Exception):
    def __init__(self, message = " Dont have a voter Id "):
        self.message = message 
try:
    n = int(input("enter the age :"))
    if n < 25 or n > 60:
        raise VotingError()
    isIndian  = bool(input("Enter you are Indian( True or False ) :"))
    if isIndian !=True:
        raise NonIndian()
    voterid = bool(input("Enter do you have voter id (True or False) :"))
    if voterid !=True:
        raise NoVoter()
except (VotingError,NonIndian,NoVoter) as e:
    print(e.message) 
else:
    print("All is set now you are eligible for voting")
finally:
    print("----------------------Terminated Successfully-------------------------")

