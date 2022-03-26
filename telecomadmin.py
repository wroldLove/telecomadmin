import json
from cmath import e
from prettytable import PrettyTable
import requests

log = '''
  __         .__                                          .___      .__        
_/  |_  ____ |  |   ____   ____  ____   _____ _____     __| _/_____ |__| ____  
\   __\/ __ \|  | _/ __ \_/ ___\/  _ \ /     \\__  \   / __ |/      \|  |/    \ 
 |  | \  ___/|  |_\  ___/\  \__(  <_> )  Y Y  \/ __ \_/ /_/ |  Y Y  \  |   |  \\
 |__|  \___  >____/\___  >\___  >____/|__|_|  (____  /\____ |__|_|  /__|___|  /
           \/          \/     \/            \/     \/      \/     \/        \/ 
'''


def getPwd(token, mac):
    url = "https://nos9.189cube.com/device/api?token={}&MAC={}".format(
        token, mac)

    data = {
        "Params": [],
        "MethodName": "GetTAPasswd",
        "RPCMethod": "CallMethod",
        "ObjectPath": "/com/ctc/igd1/Telecom/System",
        "InterfaceName": "com.ctc.igd1.SysCmd",
        "ServiceName": "com.ctc.igd1"
    }

#heads抓包获得
    heads = {
        "Content-Type": "application/json",
        "SDKVersion": "3.5.6",
        "phoneNum": "",
        "phoneOS": "",
        "systemVersion": "15.200000",
        "AppKey": "",
        "User-Agent": "YueMeTV/3.5.2 (iPhone; iOS 15.2; Scale/2.00)"
    }
    results = requests.post(url=url,data=json.dumps(data),headers=heads)
    
    try:
        return json.loads(results.text)["Params"][0]
    except Exception:
        return 

#token,mac必填
if __name__ == "__main__":
    print(log)
    token = ""
    mac = ""
    pwd = getPwd(token=token, mac=mac)
    x = PrettyTable()
    x.add_column("user",["telecomadmin"])
    x.add_column("pwd",[pwd])
    print(x)
