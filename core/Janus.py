import os
import sys
from androguard.core.bytecodes.apk import APK

class suppress_output: 
    def __init__(self,suppress_stdout=False,suppress_stderr=False): 
        self.suppress_stdout = suppress_stdout 
        self.suppress_stderr = suppress_stderr 
        self._stdout = None 
        self._stderr = None    
    
    def __enter__(self): 
        devnull = open(os.devnull, "w") 
        if self.suppress_stdout: 
            self._stdout = sys.stdout 
            sys.stdout = devnull        
        if self.suppress_stderr: 
            self._stderr = sys.stderr 
            sys.stderr = devnull
    def __exit__(self, *args): 
        if self.suppress_stdout: 
            sys.stdout = self._stdout 
        if self.suppress_stderr: 
            sys.stderr = self._stderr

class Janus:
    def is_apk_vulnerable(apk):
        with suppress_output(suppress_stdout=True,suppress_stderr=True): a = APK(apk)
        global sdk, android
        sdk, android = "27", "8.0.0"
        if a.is_signed():
            if a.is_signed_v1():
                return True
            if a.is_signed_v2() or a.is_signed_v3():
                sdk, android = "24", "7.0.0"
                return False
            if a.get_min_sdk_version() < sdk:
                return True
            else:
                return False  
        else: 
            return None

    def main(apk):
        check = Janus.is_apk_vulnerable(apk)
        if check is True:
            print(f"[+] Janus Vulnerability : APK {apk} is vulnerable to Janus attack (For More Information : https://github.com/ari5ti/Janus-Exploit).")
        elif check is None:
            print(f"[+] Janus Vulnerability : APK {apk} is not signed.")
        else:
            print("[+] Janus Vulnerability : APK is NOT VULNERABLE!")