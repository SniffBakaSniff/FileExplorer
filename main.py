import os, shutil

def list_files():
    os.system("ls")

def show_help():
    print("Commands are exit, open, list, clear, back, help, mkfile, mkdir, move")
    

running = True
list_files()

while running:
    userinput = input('Command - ')

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
        show_help()

    elif userinput.startswith('help '):
        command = userinput[5:]
        if command == 'help':
            print(f"Help for '{command}': Get help with commands for FileExplorer program.")
        elif command == 'exit':
            print(f"Help for '{command}': Terminate the FileExplorer program.")
        elif command == 'open':
            print(f"Help for '{command}': Open a specific file using your computer's default program.")
        elif command == 'list':
            print(f"Help for '{command}': See a clear list of files and folders in the current directory.")
        elif command == 'clear':
            print(f"Help for '{command}': Clean up the screen for a neat interface.")
        elif command == 'back':
            print(f"Help for '{command}': Go up one level in the directory structure.")
        elif command == 'mkdir':
            print(f"Help for '{command}': Create a new folder with a custom name.")
        elif command == 'mkfile':
            print(f"Help for '{command}': Make a new file with a specific name and extension.")
        elif command == 'rm':
            print(f"Help for '{command}': Delete a file or folder.")
        elif command == 'move':
            print(f"Help for '{command}': Move a file to a different location.")
        else:
            print("Unknown Command or No command specified. Use 'help' followed by a command name to get assistance.")
        
    
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
                list_files()
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

    elif userinput.startswith('mkdir '):
        dirName = userinput[6:]
        try:
            os.mkdir(dirName)
            os.system("clear")
            list_files()
            print(f'Directory "{dirName}" has been created.')
        except Exception as e:
            print(f'An error occurred: {e}')

    elif userinput.startswith('mkfile '):
        File_Path = userinput[7:]
        if '.' not in File_Path:
            print('Invalid file path. Please provide a valid file name with extension.')
        else:
            try:
                with open(File_Path, 'w') as file:
                    file.write('')
                os.system("clear")
                list_files()
                print(f'File "{File_Path}" has been created.')
            except Exception as e:
                print(f'An error occurred: {e}')

    elif userinput.startswith('move '):
        #selectFile = userinput[5:]
        command_parts = userinput.split(' ', 2)
        if len(command_parts) == 3:
            sorce = command_parts[1]
            destination = command_parts[2]
            try:
                shutil.move(sorce, destination)
                os.system("clear")
                list_files()
                print(f'Moved "{sorce}" to "{destination}"')
            except Exception as e:
                print(f'An error occurred: {e}')
    
    else: 
        print("Unknown Command, Use help command")
    
    
print("Goodbye!")
