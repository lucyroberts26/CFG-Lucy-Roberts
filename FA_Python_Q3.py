def calculate_classes():
    num_students = int(input("How many students do you have? "))
    min_classes = max(2, (num_students + 29) // 30)
    students_per_class = num_students // min_classes
    extra_students = num_students % min_classes

    group = {}

    for i in range(min_classes):
        if i < extra_students:
            group[f"Class {i + 1}"] = students_per_class + 1
        else:
            group[f"Class {i + 1}"] = students_per_class

    return f"Proposed Allocation: {min_classes}", group

num_classes, group = calculate_classes()
print(num_classes)
print(group)
