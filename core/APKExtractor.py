import subprocess
import zipfile
import os
from core.Config import cfrDir, dexDir, FNULL

class Dex2:
	def dex2jar(dexdir, xpath, infile, outfile):
		try:
			print("[+] Dex2Jar Starting")
			subprocess.call(['sh', dexdir + "/d2j-dex2jar.sh", xpath + '/' + infile, '-o', xpath + '/' + outfile, '-f'])
			print("[+] Dex2Jar " + infile + " OK")
		except Exception as e:
			print("ERROR : " + str(e))

	def cfr(dexDir, xpath, srcpath, jar):
		try:
			print("[+] CFR Starting")
			subprocess.call(['java','-Xms512m', '-Xmx1024m', '-jar', cfrDir, xpath + '/' + jar, '--outputdir', srcpath, '--silent', 'true', '--caseinsensitivefs', 'true'], stdout=FNULL)
			print("[+] CFR :" + jar + " OK")
		except Exception as e:
			print("ERROR : " + str(e))

	def verify_tools(dex2jar_path, cfr_path):
		if not os.path.exists(dex2jar_path):
			print("[-] Error: 'dex2jar' it's missing from the tools directory")
			return False
		
		if not os.path.exists(cfr_path):
			print("[-] Error: 'cfr.jar' it's missing from the tools directory")
			return False
		return True
	
class Extract:
	def main(apkfile):
		print("[+] APK Extractor Starting...")
		verify = Dex2.verify_tools(dexDir, cfrDir)
		if verify is True:
			print("[+] All startup files verified! Starting...")
			xpath = os.path.splitext(os.path.basename(apkfile))[0]
			srcpath = xpath + "_src"
			zip_ref = zipfile.ZipFile(apkfile, 'r')
			zip_ref.extractall(xpath)
			zip_ref.close()
			for root, dirs, files in os.walk(xpath):
				for file in files:
					if file.endswith(".dex"):
						jar = os.path.splitext(file)[0] + ".jar"
						Dex2.dex2jar(dexDir, xpath, file, jar)
						Dex2.cfr(dexDir, xpath, srcpath, jar)
			print("[+] APK Extractor completed successfully!")
		else:
			print(verify)
		print("Completed")