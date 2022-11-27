from func_task_03 import *


class Report:
    def __init__(self, title, body, end):
        self.title = title
        self.body = body
        self.end = end

    @titleToCSV
    def getCSVTitle(self):
        parsed_title = [self.title]
        return parsed_title

    @bodyToCSV
    def getCSVBody(self):
        parsed_body = list(self.body.items())
        return parsed_body

    @endToCSV
    def getCSVEnd(self):
        parsed_end = [self.end]
        return parsed_end

    @titleToTXT
    def getTXTTitle(self):
        return self.title

    @bodyToTXT
    def getTXTBody(self):
        return self.body

    @endToTXT
    def getTXTEnd(self):
        return self.end