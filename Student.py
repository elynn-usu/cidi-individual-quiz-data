import decimal

class Student:
    def __init__(self, canvasID, name, sisUser, sisLogin, email):
        self.canvasID = canvasID
        self.attempts = []
        self.attemptLabels = []
        self.name = name
        self.sisUser = sisUser
        self.sisLogin = sisLogin
        self.email = email

    def getCanvasID(self):
        return self.canvasID

    def getSisUser(self):
        return self.sisUser

    def getSisLogin(self):
        return self.sisLogin

    def getEmail(self):
        return self.email

    def getName(self):
        return self.name

    def addAttempt(self, newAttempt, quizName):
        self.attempts.append(newAttempt)
        self.attemptLabels.append(quizName)

    def getQuizName(self, attemptNum):
        return self.attemptLabels[attemptNum]

    def getNumAttempts(self):
        if len(self.attempts) == 0:
            return 0
        return self.attempts[len(self.attempts) - 1]["attempt"]

    def getScore(self, attemptNum):
        if len(self.attempts) == 0:
            return 0
        return self.attempts[attemptNum]["score"]

    def getTimeBegun(self, attemptNum):
        return self.attempts[attemptNum]["started_at"]

    def getTimeEnded(self, attemptNum):
        return self.attempts[attemptNum]["finished_at"]

    def getTimeSpent(self, attemptNum):
        return self.attempts[attemptNum]["time_spent"]

    def getFinalScore(self):
        return self.attempts[self.getNumAttempts() - 1]["kept_score"]


    def printStudentData(self):
        print(f"-------- {self.canvasID} --------")
        print(self.name)
        for attempt in range(0, self.getNumAttempts()):
            print(f"--Attempt {attempt + 1}--")
            print(f"Score: {self.getScore(attempt)}")
            print(f"Time begun: {self.getTimeBegun(attempt)}")
            print(f"Time ended: {self.getTimeEnded(attempt)}")
            print(f"Time spent: {self.getTimeSpent(attempt)} seconds")
        print("---------------------------\n")
