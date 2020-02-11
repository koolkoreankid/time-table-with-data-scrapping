d = [[[1, 3], [2, 5], [3, 8]], [[4], [5], [6]]]

l = [("blue", 5, "4"), ("red", "6"), ("yellow", "8")]
ll = [("blue", 5, "4"), ("red", "6"), ("yellow", "8"), [("ed", 1, 2), ("cool", 2)]]
# print(d[0][0][1])
ll.append([("coo2l", 4)])
l.append(("2", 5 ,6))

total = []
subject_1 = [("lec A2", "start", "end"), ("lec A1", "start", "end"), [("tut1", "Start", "end"), ("tut2", "start", "end")]]
subject_2 = [("lec B2", "start", "end"), ("lec B1", "start", "end"), [("tut1", "Start", "end"), ("tut2", "start", "end")]]
total.append(subject_1)
total.append(subject_2)


print(l[3][2])
print(len(l[1]))
print(ll)
print(total)
print(total[0][2][0])


class subject:
    def __init__(self, name, day, period):
        self.name = name
        self.day = day
        self.period = period
    
    def __repr__(self):
        return "student('{}', {}, '{}')".format(self.name, self.day, self.period) # enables to print it as typed
    


lists = [(1, 2, 55), (2, 34,4), (9, 9, 9)]
del lists[-1]
print(lists)

# lists[0].append((1,4,3,4))
# lists[0].append((2, 4, 5,6))
# lists.append([(1, 4, 5)])


print(lists)
# for i in range(2):
#     name = input("name")
#     day = input("day")
#     period = input("period")
#     lists.append(subject(name, day, period))

# print(repr(lists))

a = [[('A-LEC (7937)', 'We', '1:30PM', '2:15PM'), ('A-LEC (7937)', 'Mo', '10:30AM', '12:15PM')], ('AT01-TUT (7844)', 'Th', '10:30AM', '12:15PM'), ('AT02-TUT (8362)', 'Th', '10:30AM', '12:15PM'), ('AT03-TUT (8363)', 'Th', '10:30AM', '12:15PM')]
print(a[1][1][1])

def lol():
    return ["ehyy", "EQWRw"]

print(lol()[1])

class di:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def __repr__(self):
        return "personal({}, {})".format(self.one, self.two)

