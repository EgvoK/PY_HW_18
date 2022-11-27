import csv


def titleToCSV(func):
    filename = "report.csv"

    def titleCSV(*args, **kwargs):
        func(*args, **kwargs)
        with open(filename, "w", newline="") as file_report:
            writer = csv.writer(file_report)
            writer.writerow(func(*args, **kwargs))
    return titleCSV


def bodyToCSV(func):
    filename = "report.csv"

    def bodyCSV(*args, **kwargs):
        func(*args, **kwargs)
        with open(filename, "a", newline="") as file_report:
            writer = csv.writer(file_report)
            writer.writerows(func(*args, **kwargs))
    return bodyCSV


def endToCSV(func):
    filename = "report.csv"

    def endCSV(*args, **kwargs):
        func(*args, **kwargs)
        with open(filename, "a", newline="") as file_report:
            writer = csv.writer(file_report)
            writer.writerow(func(*args, **kwargs))
    return endCSV


def titleToTXT(func):
    filename = "report.txt"

    def titleTXT(*args, **kwargs):
        func(*args, **kwargs)
        with open(filename, "w") as file_report:
            file_report.write(func(*args, **kwargs) + "\n")
    return titleTXT


def bodyToTXT(func):
    filename = "report.txt"

    def bodyTXT(*args, **kwargs):
        func(*args, **kwargs)
        content = func(*args, **kwargs)
        with open(filename, "a") as file_report:
            for key in content:
                file_report.write("\n" + str(key) + ": " + str(content[key]))
    return bodyTXT


def endToTXT(func):
    filename = "report.txt"

    def endTXT(*args, **kwargs):
        func(*args, **kwargs)
        with open(filename, "a") as file_report:
            file_report.write("\n\n" + func(*args, **kwargs))
    return endTXT
