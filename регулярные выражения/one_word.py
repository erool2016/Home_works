import re

def one_name(sent_list, line):
    my_dict = {}
    my_dict['firstname'] = sent_list[0]
    if len(re.findall(r'[\w]+', line[1])) ==2:
        # print('two names',line[1])
        words = re.findall(r'[\w]+', line[1])
        my_dict['lastname'] = words[0]
        my_dict['surname'] = words[1]
        my_dict['organization'] = line[3]
        my_dict['position'] = line[4]
        my_dict['phone'] = line[5]
        my_dict['email'] = line[6]
        # my_list.append(my_dict)
        # print('2_pole_is_2_simbol',my_list)
        return my_dict
    else:
        my_dict['lastname'] = line[0]
        my_dict['firstname'] = line[1]
        my_dict['surname'] = line[2]
        my_dict['organization'] = line[3]
        my_dict['position'] = line[4]
        my_dict['phone'] = line[5]
        my_dict['email'] = line[6]
        # my_list.append(my_dict)
        # print('1_pole_is_1_simbol', my_list)
        return my_dict