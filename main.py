import os, shutil, datetime

def list_files():
    os.system("ls")

def show_help():
    print("Commands are exit, open, list, clear, back, help, mkfile, mkdir, move, rename, copy, search, info")
    

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
        elif command == 'rename':
            print(f"Help for '{command}': Rename a file or folder.")
        elif command == 'copy':
            print(f"Help for '{command}': Copy a file or folder.")
        elif command == 'search':
            print(f"Help for '{command}': Search for a file in the current directory and its subdirectories.")
        elif command == 'info':
            print(f"Help for '{command}': Get information about a file, including size and timestamps.")
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

    elif userinput.startswith('rename '):
        command_parts = userinput.split(' ', 2)
        if len(command_parts) == 3:
            old_name = command_parts[1]
            new_name = command_parts[2]

            if os.path.exists(old_name):
                try:
                    os.rename(old_name, new_name)
                    os.system("clear")
                    list_files()
                    print(f'Renamed "{old_name}" to "{new_name}"')
                except Exception as e:
                    print(f'An error occurred: {e}')
            else:
                print(f'File or folder "{old_name}" does not exist.')
        
    elif userinput.startswith('copy '):
        command_parts = userinput.split(' ', 2)
        if len(command_parts) == 3:
            source = command_parts[1]
            destination = command_parts[2]

            if os.path.exists(source):
                try:
                    shutil.copy(source, destination)
                    os.system("clear")
                    list_files()
                    print(f'Copied "{source}" to "{destination}"')
                except Exception as e:
                    print(f'An error occurred: {e}')
            else:
                print(f'Source file or folder "{source}" does not exist.')
    
    elif userinput.startswith('search '):
        filename = userinput[7:]

        def search_file(start_dir, filename):
            for root, dirs, files in os.walk(start_dir):
                if filename in files:
                    return os.path.join(root, filename)
            return None

        result = search_file(os.getcwd(), filename)
        if result:
            print(f'File "{filename}" found at: {result}')
        else:
            print(f'File "{filename}" not found.')
    
    elif userinput.startswith('info '):
        filename = userinput[5:].strip()
        if os.path.exists(filename):
            try:
                file_info = os.stat(filename)
                size_mb = file_info.st_size / (1024 * 1024)
                print(f'Info for "{filename}":')
                print(f'  Size: {size_mb} mb')
                print(f'  Created: {datetime.datetime.fromtimestamp(file_info.st_ctime).strftime("%Y-%m-%d %H:%M:%S")}')
                print(f'  Modified: {datetime.datetime.fromtimestamp(file_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")}')
                print(f'  Accessed: {datetime.datetime.fromtimestamp(file_info.st_atime).strftime("%Y-%m-%d %H:%M:%S")}')

            except Exception as e:
                print(f'An error occurred: {e}')
        else:
            print(f'File "{filename}" not found.')
    
    else: 
        print("Unknown Command, Use help command")
    
print("Goodbye!")
