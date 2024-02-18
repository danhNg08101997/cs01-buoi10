'''
lst_number = [2,7,11,15]
Mô tả: Tìm hai số trong một danh sách số nguyên sao cho tổng của chúng bằng một giá trị target cho trước
Ví dụ:
Input: nums = [2,7,11,15], target = 9
Output: [0,1] (vì nums[0] + nums[1] = 2+7 = 9) ngược lại nếu không có
'''

def two_sum(lst, target):
    output = []
    dict_num = {}
    for num in lst:
        rest = target - num
        if rest in dict_num:
            output = [num, rest]
            break
        dict_num[num] = rest
    return output


lst_number = [2, 7, 11, 15]
print(two_sum(lst_number, 26))