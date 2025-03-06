def checkAscending(report):
    ignored = 0
    previous = report[0]
    print("ascending")
    x = 1
    while x < len(report):
        print(report, previous, report[x])
        current = report[x]
        
        if previous > current:
            print(previous, "is larger than", current)
            if ignored == 0:
                ignored += 1
                previous = current
                x += 1
                continue
            else:
                return False

        if not (1 <= abs(current - previous) <= 3):
            print("abs error", previous, current, "results in", abs(previous - current), "∉ (1, 3)")
            if ignored == 0:
                ignored += 1
                # previous = report[x]
                if x == 1:
                    previous = report[x]
                x += 1
                continue
            else:
                return False
        
        previous = report[x]
        x += 1
    return True
    

def checkDescending(report):
    ignored = 0
    previous = report[0]
    print("descending")
    x = 1
    while x < len(report):
        print(report, previous, report[x])
        current = report[x]
        
        if previous < current:
            print(previous, "is smaller than", current)
            if ignored == 0:
                ignored += 1
                previous = current
                x += 1
                continue
            else:
                return False
        
        if not (1 <= abs(previous - current) <= 3):
            print("abs error", previous, current, "results in", abs(previous - current),  "∉ (1, 3)")
            if ignored == 0:
                ignored += 1
                # previous = report[x]
                if x == 1:
                    previous = report[x]
                x += 1
                continue
            else:
                return False
        
        previous = report[x]
        x += 1
    return True

def isAscending(report):
    score = 0
    previous = report[0]
    for x in range(1, len(report)):
        current = report[x]
        if previous < current:
            # print(previous, "is smaller than", current)
            score += 1
        previous = current
    if score > 1:
        return True
    return False

def get_safe_reports(report_file):
    reports = []
    
    with open(report_file, 'r') as file:
        for line in file:
            splitted = line.strip("\n").split(" ")
            int_report = []
            for level in splitted:
                int_report.append(int(level))
            reports.append(int_report)

    # print(reports)
    
    safe_reports = 0
    for report in reports:
        if isAscending(report):
            if checkAscending(report):
                print(report, "Safe")
                safe_reports += 1
            else:
                print(report, "Unsafe")
        else:
            if checkDescending(report):
                print(report, "Safe")
                safe_reports += 1
            else:
                print(report, "Unsafe")
        
        print()
    print("Number of safe reports:", safe_reports)

if __name__ == "__main__":
    # get_safe_reports("example_input.txt")
    get_safe_reports("input_safe.txt")
    # get_safe_reports("input_unsafe.txt")
    # get_safe_reports("input.txt")


