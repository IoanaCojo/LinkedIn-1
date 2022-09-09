


class Merge2SortedList():
    def mergeTwoLists(sefl, list1, list2):
        


'''
    def mergeTwoLists(sefl, list1, list2):

        result = []

        list1Len = len(list1)
        list2Len = len(list2)

        point = 0

        list1point = 0
        list2point = 0
        while point < list1Len + list2Len and (list1point <= list1Len or list2point <= list2Len) :
            if list1[list1point] < list2[list2point]:
                result.append(list1[list1point])
                list1point += 1
            elif list1[list1point] > list2[list2point]:
                result.append(list2[list2point])
                list2point += 1
            else:
                result.append(list1[list1point])
                result.append(list2[list2point])
                list1point += 1
                list2point += 1
                point += 1
            point += 1
        if list1point != list1Len:
            while list1point != list1Len:
                result.append(list1[list1point])
                list1point +=1
        if list2point != list2Len:
            while list1point != list1Len:
                result.append(list2[list2point])
                list1point +=1



        test = Merge2SortedList
        test.mergeTwoLists([1, 2], [1, 1, 1])
'''


