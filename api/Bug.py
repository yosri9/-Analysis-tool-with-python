from api.authentication import *
from os import path

bugTypes = ["Warning", "Error", "Fail", "Debug", "Information", "Trace"]


class FetchBugs():

    def fetchBugs():

        client = Authentication.login(ApiUtilities.username, ApiUtilities.password)
        command = ""
        for bugType in bugTypes:
            command += bugExtractorCommand(bugType) + "; "
        client.exec_command(command)


        print(command)

        client.close()

        client = Authentication.login(ApiUtilities.username, ApiUtilities.password)
        ssh_sftp = client.open_sftp()
        # Download bugs file
        for bugType in bugTypes:
            # download bugFile
            ssh_sftp = client.open_sftp()
            print(ApiUtilities.PATH + bugType + ".txt", ApiUtilities.LOCAL_FOLDER_PATH + '/' + bugType + ".txt")
            ssh_sftp.get(ApiUtilities.PATH + bugType + ".txt", ApiUtilities.LOCAL_FOLDER_PATH + '/' + bugType + ".txt")
            ssh_sftp.close()

        client.exec_command("rm " + ApiUtilities.PATH + "Warning.txt " + ApiUtilities.PATH + "Error.txt " +
                            ApiUtilities.PATH + "Fail.txt " + ApiUtilities.PATH + "Debug.txt " + ApiUtilities.PATH + "Information.txt "
                            + ApiUtilities.PATH + "Trace.txt")

        client.close()


def bugFile(bugType):
    print('open')
    file = open(ApiUtilities.LOCAL_FOLDER_PATH + '/' + bugType + ".txt", "r")
    return file


def bugExtractorCommand(bugType):
    grep = ""
    command = "  cut -d \" \" -f 2- " + ApiUtilities.LOG_FILE_PATH + " |sort | uniq -c | sort -nr" + grep + "> " + ApiUtilities.PATH + bugType + ".txt "

    if bugType != "Trace":
        grep = "| grep \'(" + bugType[0] + ")\'"
        command = "  cut -d \" \" -f 2- " + ApiUtilities.LOG_FILE_PATH + " |sort | uniq -c | sort -nr" + grep + "> " + ApiUtilities.PATH + bugType + ".txt "

    return command
