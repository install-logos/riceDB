import os
import json
import shutil

def package(rice, prog, path):
    path = path.replace('~',os.environ['HOME'])

    if(not os.path.isdir(path)):
        os.mkdir(path)

    os.chdir(os.environ['HOME'] + '/.riceDB')

    if (not os.path.exists('./' + prog)):
        return (False, "The program specified does not have any rices")

    else:
        os.chdir('./' + prog)

        if (os.path.exists('./.active')):
            active = open('.active').readline().rstrip().replace(" ","")

            if (active == rice):
                os.chdir('./' + rice)
                json_data = open('sysinfo.json')
                data = json.load(json_data)
                json_data.close()
                key = list(data.keys())

                for k in key:
                    loc = data[k].replace("~",os.environ['HOME'])
                    copy2(loc + k, path)

            #TODO: Find a more efficient way to do this
            else:
                if (not os.path.exists('./' + rice)):
                    return (False, "Rice specified does not exist")

                else:
                    os.chdir('./' + rice)
                    files = os.listdir('./')

                    for f in files:
                        copy2(f, path)

        else:
            if (not os.path.exists('./' + rice)):
                return (False, "Rice specified does not exist")

            else:
                os.chdir('./' + rice)
                files = os.listdir('./')

                for f in files:
                    copy2(f, path)

        print("Please enter the following metadata for your rice:")
        print("Name:")
        metadata = {}
        name = input()
        metadata['Name'] = name.replace(' ','')
        print("Author (optionnal, ie : you can leave it blank if you want):")
        author = input()
        metadata['Author'] = author
        print ("Description:")
        description = input()
        metadata['Description'] = description
        return (True,"")

