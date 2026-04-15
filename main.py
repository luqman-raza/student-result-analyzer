names = ["Ali", "Sara", "Ahmed", "Zain"]
marks = []

for i in range(len(names)):
    mark = int(input(f"Enter marks for {names[i]}: "))
    marks.append(mark)




total_student = len(names)
print(f"Total student {total_student}")

def calculate (marks):
    total = sum(marks)
    average = total / len(marks)
    return average
avg = calculate(marks)
print(f"Average marks: {avg}")

def count_pass(marks):
    count = 0
    for m in marks:
        if m >= 50:
            count += 1
    return count
passed = count_pass(marks)
print(f"passed : {passed}")
def fail_count (marks):
    count = 0
    for ma in marks :
        if ma < 50:
            count+=1
    return count
fail = fail_count(marks)
print(f"Failled : {fail}")