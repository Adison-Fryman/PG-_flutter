# code to automate phfutter insert for CSV file --> database in PG admin

#testing original string
#test='''pgfutter_windows_amd64.exe --db "*****" --schema "public" --port "5432" --user "postgres" --pw "*******" csv college_football_data_mode_c.csv'''

default_values = {
    'filename_pgfutter':'pgfutter_windows_amd64.exe',
    'database_name':'ENTER YOUR DATABASE HERE',
    'port': '5432',
    'user': 'postgres',
    'password': 'ENTER YOUR PASSWORD HERE',
    'full_file_name': 'ENTER YOUR FILE NAME HERE'
}

# save your default values here for safe keeping
default_pgfutter_values_backup ={
    'filename_pgfutter':'pgfutter_windows_amd64.exe',
    'database_name':'',
    'port': '5432',
    'user': 'postgres',
    'password': '',
    'full_file_name': ''
}
#These lines compiar the original manual string to the code generated one.
# If yours works right away, don't worry about this step.
# If you have to make adjustments to syntax or spacing for it to work this is here for you to view them side by side.
#print(test)
#print(f'''{default_values["filename_pgfutter"] } --db "{default_values["database_name"]}" --schema "public" --port "{default_values["port"]}" --user "{default_values["user"]}" --pw "{default_values["password"]}" csv {default_values["full_file_name"]}.csv''')

print('This program is to auto generate the phfutter insert for CSV file --> database in PG admin')
command = input('''
To view your defaults enter VD,
To edit your defaults enter ED,
To print string enter P,
To exit enter E: ''')


def edit_values():
    print( '''Your default value for filename_pgfutter: pgfutter_windows_amd64.exe''')
    change=input('Enter you new value here or leave it blank to keep value as is: ')
    if change:
        default_values["filename_pgfutter"] = change
    else:
        change=''
    print( '''Your default value for database_name:test3''')
    change=input('Enter you new value here or leave it blank to keep value as is: ')
    if change:
        default_values['database_name'] = change
    else:
        change = ''
    print( '''Your default value for 'port': 5432''')
    change=input('Enter you new value here or leave it blank to keep value as is: ')
    if change:
        default_values['port'] = change
    else:
        change=''
    print( '''Your default value for user: postgres''')
    change=input('Enter you new value here or leave it blank to keep value as is: ')
    if change:
        default_values['user'] = change
    else:
        change = ''
    print( '''Your default value for password: ADIin2code!''')
    change=input('Enter you new value here or leave it blank to keep value as is: ')
    if change:
        default_values['password'] = change
    else:
        change=''
    print( '''Your default value for full_file_name : ''')
    change=input('Enter you new value here or leave it blank to keep value as is: ')
    if change:
        default_values['full_file_name'] = change
    else:
        change = ''

    print('Review your new default Values')
    navigator('VD')


def navigator(command):
    while True:
        if command.upper()=='VD':
            print('')
            for item in default_values.items():
             print(item)
            command = input('''
To edit your defaults enter ED,
To print string enter P,
To exit enter E: ''')
        elif command.upper()=='ED':
            edit_values()
        elif command.upper()=='P':
            print(f'''{default_values["filename_pgfutter"]} --db "{default_values["database_name"]}" --schema "public" --port "{default_values["port"]}" --user "{default_values["user"]}" --pw "{default_values["password"]}" csv {default_values["full_file_name"]}.csv''')
            command = input('''
TO edit your defaults again enter ED,
To view your defaults again enter VD,
To exit enter E: ''')
        elif command.upper() == 'E':
            exit()
        elif command.upper() =='A':
            return f'''{default_values["filename_pgfutter"]} --db "{default_values["database_name"]}" --schema "public" --port "{default_values["port"]}" --user "{default_values["user"]}" --pw "{default_values["password"]}" csv {default_values["full_file_name"]}.csv'''
        else:
            print(''' 
            HEY-That is not a valid entry!
            'To view your defaults enter VD,
             To edit your defaults enter ED,
             To print string enter P,
             To exit enter E'
            ''')
            command = input('Try again here:  ')

navigator(command)



#def auto_print(pgfutter_values):
# code to be added later when ready. Plan is to fully automate the insertion of the line into shell from within this program.
