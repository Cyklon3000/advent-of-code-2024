reports = []

def sign(num):
    return -1 if num < 0 else (1 if num > 0 else 0)

with open("input.txt", "r") as file:
    for report in file:
        reports.append([int(number) for number in report.strip().split(" ")])

def is_report_safe(report):
    lastLevel = report[0]
    slope = 0
    for l in range(1, len(report)):
        difference = report[l] - lastLevel
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        if slope != 0:
            if sign(difference) != slope:
                return False
        else:
            slope = sign(difference)
        lastLevel = report[l]
    return True

safeReportCount = 0
for report in reports:
    isReportSafe = False
    for deleteIndex in range(len(report)):
        reportVersion = report.copy()
        reportVersion.pop(deleteIndex)
        isReportSafe = isReportSafe or is_report_safe(reportVersion)
    safeReportCount += int(isReportSafe)
print(safeReportCount)