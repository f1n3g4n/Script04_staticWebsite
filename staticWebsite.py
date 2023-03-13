#!/usr/bin/python3
# Script by F1neg4n

import os


def welcome():
    welc = 'Static Website'
    info = '[INFO] Python script to create base for static website'
    os.system('clear')
    print(welc + '\n' + '*' * len(welc))
    print(info)
    print('------------')
    return

def projectName():
    welcome()
    try: 
        projectName = input('[+] Enter the name project: ')
        while(projectName == ''):
            projectName = input('[+] Please, enter the name project: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[-] Interrupted by user!')
        exit()
    return projectName

def createProject():
    name = projectName()
    if(os.path.exists(name) == True):
        os.system('clear')
        welcome()
        print('[-] The project name has taken!')
        exit()
    else:
        os.system('clear')
        welcome()
        print('[+] Creating new project "'+name+'"...')
        os.system('mkdir ' + name)
        os.chdir(name + '/')
        os.system('mkdir static')
        os.system('touch index.html')
        os.chdir('static/')
        os.system('mkdir css js img')
        os.chdir('css/')
        os.system('touch style.css')
        os.chdir('../')
        os.chdir('js/')
        os.system('touch index.js')
        print('[+] Done!')
    return


if __name__ == '__main__':
    createProject()
