

def all_names(sent_list, line):
    my_dict = {}
    # print('sent list-',sent_list)

    my_dict['lastname'] = sent_list[0]
    my_dict['firstname'] = sent_list[1]
    my_dict['surname'] = sent_list[2]
    my_dict['organization'] = line[3]
    my_dict['position'] = line[4]
    my_dict['phone'] = line[5]
    my_dict['email'] = line[6]
    # print(my_dict)
    # my_list.append(my_dict)
    # print(my_list)
    return my_dict