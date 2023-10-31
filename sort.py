from typing import List


def sortNums(list_nums: List[int]):
    start_list = 0
    end_list = len(list_nums) -   1
    # print(end_list)
    while start_list < end_list :
        list_nums[start_list] , list_nums[end_list] = list_nums[end_list] , list_nums[start_list]
        start_list += 1
        end_list -= 1

    print(f'list nums : {list_nums}')
    return list_nums



sortNums([1,2,3,4,5,6])