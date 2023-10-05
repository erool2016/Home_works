
my_dict = {}
def two_names(sent_list, line):
    my_dict['lastname'] = sent_list[0]
    my_dict['firstname'] = sent_list[1]
    my_dict['surname'] = line[2]
    my_dict['organization'] = line[3]
    my_dict['position'] = line[4]
    my_dict['phone'] = line[5]
    my_dict['email'] = line[6]
    return(my_dict)