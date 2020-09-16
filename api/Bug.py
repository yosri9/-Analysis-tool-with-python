from api.authentication import *

bugTypes=["Warning" ,"Error" ,"Fail" ,"Debug" ,"Information" , "Trace"]


def fetchBugs():
    username =""
    password = ""
    client = Authentication.login(username, password)
    for bugType in bugTypes:
        client.exec_command(bugExtractorCommand(bugType))

    client.close()

    client = Authentication.login(username, password)

    ssh_sftp = client.open_sftp()
    for bugType in bugTypes:
        print(ApiUtilities.PATH + bugType + ".txt", ApiUtilities.LOCAL_FOLDER_PATH + bugType + ".txt")
        ssh_sftp.get(ApiUtilities.PATH + bugType + ".txt", ApiUtilities.LOCAL_FOLDER_PATH + bugType + ".txt")
    ssh_sftp.close()
    client.close()



def bugFile(bugType):
    file = open(ApiUtilities.LOCAL_FOLDER_PATH + bugType + ".txt", "r")
    return file


def bugExtractorCommand(bugType):
    command=""
    if bugType == "Trace":
        grep = ""
        command = "  cut -d \" \" -f 2- " + ApiUtilities.PATH + ApiUtilities.LOG_FILE + " |sort | uniq -c | sort -nr" + grep + "> " + ApiUtilities.PATH + bugType + ".txt "

    else:
        grep = "| grep \'(" + bugType[0] + ")\'"

    return command

