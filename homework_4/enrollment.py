universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats():
    students = []
    tution = []

    for el in universities:
        students.append(el[1])
        tution.append(el[2])

    return {"std": students, "tuF": tution}


def mean(arr):
    a = 0
    sum = 0

    while a < len(arr):
        sum += arr[a]
        a += 1

    return sum/a


def median(arr):
    l = len(arr)
    arr.sort()
    
    if len(arr) % 2 != 0:
        return arr[int(l/2)]
    else:
        return (arr[l/2 - 1] + arr[l/2])/2
    
print("**********************************************************************")

print(f"Total students: {sum(enrollment_stats()["std"])}")
print(f"Total tution: $ {sum(enrollment_stats()["tuF"])}")
print()
print(f"Student mean: {mean(enrollment_stats()["std"]):.2f}")
print(f"Student median: {median(enrollment_stats()["std"])}")
print()
print(f"Tution mean: $ {mean(enrollment_stats()["tuF"]):.2f}")
print(f"Tution median: $ {median(enrollment_stats()["tuF"])}")
print()
print("**********************************************************************")