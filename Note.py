class Note:
    def __init__(self, caption, text, date="") -> None:
        self.head = str(caption)
        self.body = str(text)
        self.date = (date)

    def partsPublish(self):
        return {self.date, self.head, self.body}

    def getDate(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    def printNote(self):
        print(self.getDate())
        print(self.head)
        print(self.body)

    def shortInfo(self):
        return f"{self.getDate()} - {self.head}"