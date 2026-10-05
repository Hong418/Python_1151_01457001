def score_manager():
    if q_id in student:
        name, score = student[q_id]
        print(f"{name} {score}")
    else:
        print("Not found")


student = {}

n = int(input())
for i in range(n):
    a = input().split()
    id = a[0]
    name = a[1]
    score = a[2]
    student[id] = (name, score)

q = int(input())
for i in range(q):
    q_id = input().strip()
    score_manager()