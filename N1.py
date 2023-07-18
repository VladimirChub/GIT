# def counter(s): # O(N ** 2)
#     for i in s:
#         count = 0
#         for j in a:
#             if i == j:
#                 count += 1
#         print(i,count)

# def counter(s): # O(N * M)
#     for i in set(s):
#             count = 0
#             for j in a:
#                 if i == j:
#                     count += 1
#             print(i,count)

def counter(s): # O(N)
    syms = {}
    for i in s:
        syms[i] = syms.get(i, 0) + 1
    for i, count in syms.items():
        print(i,count)


a = 'aqqsasddaf'
counter(a)

# k = 'ff uu hh gg'
# print(len(k.split()))