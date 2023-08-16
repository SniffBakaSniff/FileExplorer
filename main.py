import os

def list_files():
    #os.system("clear")
    os.system("ls")

def show_help():
    print("Commands are exit, open, list, clear, back, help")
    userinput = input('Command - ')
    return userinput

running = True
list_files()
userinput = input('Command - ')

while running:
    if userinput == 'back':
        os.system("clear")
        os.chdir("..")
        list_files()
    
    elif userinput == 'exit':
        running = False
    
    elif userinput == 'list':
        list_files()
    
    elif userinput == 'clear':
        os.system('clear')
    
    elif userinput == 'help':
        userinput = show_help()
    
    elif userinput.startswith('open '):
        selectFile = userinput[5:]    
        if os.path.exists(selectFile):
            if os.path.isfile(selectFile):
                os.system(selectFile)
                list_files
            elif os.path.isdir(selectFile):
                os.chdir(selectFile)
                os.system("clear")
                list_files()
            else:
                print(f'Unknown file or folder type: {selectFile}')
        else:
            print(f'File or folder "{selectFile}" does not exist.')
    
    elif userinput.startswith('rm '):
        selectFile = userinput[3:]    
        if os.path.exists(selectFile):
            if os.path.isfile(selectFile):
                os.remove(selectFile)
                os.system("clear")
                list_files
            elif os.path.isdir(selectFile):
                try:
                    os.removedirs(selectFile)
                    os.system("clear")
                    list_files()
                except OSError as e:
                    print(f'Error deleting directory "{selectFile}": {e}')
            else:
                print(f'Unknown file or folder type: {selectFile}')
        else:
            print(f'File or folder "{selectFile}" does not exist.')

    else: 
        print("Unknown Command, Use help command")
    
    userinput = input('Command - ')
