from data_task_03 import *


def getReport(title, body, end):
    new_report = Report(title, body, end)
    while True:
        select = input("1 - Get report in .csv format;\n2 - Get report in .txt format;\n0 - Exit."
                       "\nEnter action number: ")

        if select == "0":
            print("Exit...")
            break

        elif select == "1":
            new_report.getCSVTitle()
            new_report.getCSVBody()
            new_report.getCSVEnd()

        elif select == "2":
            new_report.getTXTTitle()
            new_report.getTXTBody()
            new_report.getTXTEnd()

        else:
            print("Error! Incorrect action!")


# getReport("Quarterly report", {"Order quantity": 1000, "Customer count": 800, "Turnover amount": 1234567.9,
#                                "Profit amount": 50000, "Tax amount": 20000, "Net profit amount": 30000},
#           "Signature: J.H. Fray")
