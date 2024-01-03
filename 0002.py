# n1, n2 = 10, 20
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)
# print(n1 != n2)
# print(1 == 1 and 3 == 3)
# print(1 == 1 or 2 == 3)
# hours = int(input("Enter hours: "))
# if hours >= 12:
#     print("PM")
#     print("asdf")
# else:
#     print("AM")
hours = int(input("Enter hours: "))
if 12 <= hours < 24:
        print("PM")
elif 0 <= hours < 12:
        print("AM")
else:
        print("Incorrect hours!")