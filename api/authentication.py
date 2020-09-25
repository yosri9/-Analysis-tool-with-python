import paramiko
from  api.api_utilities import *

class Authentication():

    def login():

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        print(ApiUtilities.MAIN_API_URL + "  " + ApiUtilities.USERNAME + "  " + ApiUtilities.PASSWORD)
        client.connect(hostname = ApiUtilities.MAIN_API_URL, username = ApiUtilities.USERNAME, password = ApiUtilities.PASSWORD)
        return client





