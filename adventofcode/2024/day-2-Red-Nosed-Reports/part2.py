def checkAscending(report):
    previous = report[0]
    for x in range(1, len(report)):
        # print(x, report[x])
        if previous > report[x] or not (1 <= abs(report[x] - previous) <= 3):
            # print("ascending!", previous, "is larger than", report[x])
            return False
        previous = report[x]
    return True
    

def checkDescending(report):
    previous = report[0]
    for x in range(1, len(report)):
        # print(x, report[x])
        if previous < report[x] or not (1 <= abs(previous - report[x]) <= 3):
            # print("descending!", previous, "is smaller than", report[x])
            return False
        previous = report[x]
    return True


# Version with ignoring one error, but dropped the effort
# def checkAscending(report):
#     ignored = 0
#     previous = report[0]
#     print("ascending")
#     x = 1
#     while x < len(report):
#         print(report, previous, report[x])
#         current = report[x]
        
#         if previous > current:
#             print(previous, "is larger than", current)
#             if ignored == 0:
#                 ignored += 1
#                 previous = current
#                 x += 1
#                 continue
#             else:
#                 return False

#         if not (1 <= abs(current - previous) <= 3):
#             print("abs error", previous, current, "results in", abs(previous - current), "∉ (1, 3)")
#             if ignored == 0:
#                 ignored += 1
#                 # previous = report[x]
#                 if x == 1:
#                     previous = report[x]
#                 x += 1
#                 continue
#             else:
#                 return False
        
#         previous = report[x]
#         x += 1
#     return True
    

# Version with ignoring one error, but dropped the effort
# def checkDescending(report):
#     ignored = 0
#     previous = report[0]
#     print("descending")
#     x = 1
#     while x < len(report):
#         print(report, previous, report[x])
#         current = report[x]
        
#         if previous < current:
#             print(previous, "is smaller than", current)
#             if ignored == 0:
#                 ignored += 1
#                 previous = current
#                 x += 1
#                 continue
#             else:
#                 return False
        
#         if not (1 <= abs(previous - current) <= 3):
#             print("abs error", previous, current, "results in", abs(previous - current),  "∉ (1, 3)")
#             if ignored == 0:
#                 ignored += 1
#                 # previous = report[x]
#                 if x == 1:
#                     previous = report[x]
#                 x += 1
#                 continue
#             else:
#                 return False
        
#         previous = report[x]
#         x += 1
#     return True

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
            for k in range(0, len(report)):
                print("List without ", k, "is ")
                report_without_nth = report[:k] + report[(k + 1):]
                if checkAscending(report_without_nth):
                    print(report_without_nth, "Safe")
                    safe_reports += 1
                    break
                else:
                    print(report_without_nth, "Unsafe")
        else:
            for k in range(0, len(report)):
                print("List without ", k, "is ")
                report_without_nth = report[:k] + report[(k + 1):]
                if checkDescending(report_without_nth):
                    print(report_without_nth, "Safe")
                    safe_reports += 1
                    break
                else:
                    print(report_without_nth, "Unsafe")
        
        print()
    print("Number of safe reports:", safe_reports)

if __name__ == "__main__":
    # get_safe_reports("example_input.txt")
    # get_safe_reports("input_safe.txt")
    # get_safe_reports("input_unsafe.txt")
    get_safe_reports("input.txt")


