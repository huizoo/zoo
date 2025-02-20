# #1 2 3 4 5 4 3 2 1
#
# def abc(level, max_level) :
#     print(level, end=' ')
#     if level == max_level :
#         return
#
#     abc(level+1, max_level)
#     print(level, end=' ')
#
# abc(1, 5)



# def abc(level) :
#     print('@', end = ' ')
#     if level == 2 :
#         return
#     for i in range(2) :
#         abc(level+1)
#         print('@', end=' ')
# abc(0)



def abc(level):
    print('@', end=' ')
    if level==2:
        print('@', end=' ')
        return

    print('@', end=' ')
    for i in range(2):
        print('@', end=' ')
        abc(level+1)
        print('@', end=' ')
    print('@', end=' ')

abc(0)
