main_list = ['apple', 'mango', 'pear', '', 'pineapple', '', 'orange', '', '']
# main_list = []
print(list(dict.fromkeys(main_list)))
try:
    main_list = list(dict.fromkeys(main_list))
    main_list.remove('')
    print(main_list)
except:
    print("list is empty")
