import paramiko
from  api.api_utilities import *

class Authentication():

    def login( userName , password ):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(hostname = ApiUtilities.MAIN_API_URL , username = userName, password = password)
        return client





