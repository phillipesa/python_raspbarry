import src.common.get_token as auth
import src.common.wifi_connection as wificon
import src.common.osidentify as machine_os

def run():          
    auth.TestGet()
    wificon.Search()
    machine_os.SearchOS()