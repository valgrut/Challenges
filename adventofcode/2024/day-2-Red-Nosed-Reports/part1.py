def isAscending(report):
    previous = report[0]
    for x in range(1, len(report)):
        # print(x, report[x])
        if previous > report[x] or not (1 <= abs(report[x] - previous) <= 3):
            # print("ascending!", previous, "is larger than", report[x])
            return False
        previous = report[x]
    return True
    

def isDescending(report):
    previous = report[0]
    for x in range(1, len(report)):
        # print(x, report[x])
        if previous < report[x] or not (1 <= abs(previous - report[x]) <= 3):
            # print("descending!", previous, "is smaller than", report[x])
            return False
        previous = report[x]
    return True


def isSafe(report):
    if report[0] > report[1]:
        return isDescending(report)
    elif report[0] < report[1]:
        return isAscending(report)
    else: 
        return False


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    
    reports = []
    
    with open(input_file, 'r') as file:
        for line in file:
            splitted = line.strip("\n").split(" ")
            int_report = []
            for level in splitted:
                int_report.append(int(level))
            reports.append(int_report)

    # print(reports)
    
    safe_reports = 0
    for report in reports:
        if isSafe(report):
            safe_reports += 1
    
    print("Number of safe reports:", safe_reports)
