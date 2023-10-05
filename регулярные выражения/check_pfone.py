import re

def six_num(num):
    # print(f'6_num,\n {num}')
    return f'+7({num[1]}){num[2]}-{num[3]}-{num[4]} доб {num[5]}'
def fift_num(num):
    # print(f'5_num,\n {num}')
    return f'+7({num[1]}){num[2]}-{num[3]}-{num[4]}'
def four_num(num):
    # print(f'4_num,\n {num}')
    num_1 = re.findall(r'\d', num[3])
    # print(f'num_1 = {num_1}')
    return f'+7({num[1]}){num[2]}-{num_1[0]}{num_1[1]}-{num_1[2]}{num_1[3]}'
def one_num(num):
    # print(f'1_num,\n {num}')
    num_ = re.findall(r'\d', num[0])
    # print(num_)
    return f'+7({num_[1]}{num_[2]}{num_[3]}){num_[4]}{num_[5]}{num_[6]}-{num_[7]}{num_[8]}-{num_[9]}{num_[10]}'



def check_pfone_num(my_list):
    # print(f'check_pfone_num,\nmy_list = {my_list}')
    for item in my_list:
        # print(f'item phone= {item["phone"]}\n')
        num = re.findall(r'\d+', item['phone'])
        # print(f'num = {num}')
        if len(num) == 6:
            print(six_num(num))
            item['phone'] = six_num(num)
        if len(num) == 5:
            print(fift_num(num))
            item['phone'] = fift_num(num)
        if len(num) == 4:
            print(four_num(num))
            item['phone'] = four_num(num)
        if len(num) == 1:
            print(one_num(num))
            item['phone'] = one_num(num)
        # for items in my_list:
        #     print('new items',items)

