def format_to_yml(input_file_name, output_file_name):
    f = open("actions/api/country_unformat.txt", "r")
    x = f.read()
    # print(type(x))
    data_list = x.split('\n')
    new_data = ''
    print(data_list)
    i = 0
    new_data = '''{
    "country": ['''
    for item in data_list[:-1]:
        new_data += '''
        {
            "id": '''+str(i)+''',
            "name": "'''+ item + '''"
        },
        '''
        i =i + 1
    i =i + 1
    new_data += '''
        {
            "id": '''+str(i)+''',
            "name": "'''+ data_list[-1] + '''"
        }
    ]
}
    '''

    print(new_data)
    f.close()
    f = open("actions/api/"+output_file_name+".json","w")
    f.write(new_data)

format_to_yml("country_unformat", "country_list1")
# PS D:\pure_dev\gTalkBot\data\lookup_tables> python format.py
