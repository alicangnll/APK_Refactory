import sys
import os
from core import APKExtractor, FirebaseExtractor, Janus, GoogleAPIKeyExtractor, StringExtractor, SensitiveInfo

class Run:
	def remove_folder(path):
		for root, dirs, files in os.walk(path, topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
		os.rmdir(path)
	
	def main(apkfile):
		try:
			print("=====================================================")
			print("APK FILE SCANNER | Developed by github.com/alicangnll")
			print("=====================================================")
			# APK String Printer Starting...
			StringExtractor.StringExtractor.main(apkfile)
			strings_matches = SensitiveInfo.SensitiveInfo.check_text_for_sensitive_keywords(str(os.path.splitext(os.path.basename(apkfile))[0]) + "_apk_logs.txt")
			for match in strings_matches:
				with open(str(apkfile).replace(".", "_") + "_sensitiveinfo_text_" + str(round(100000000, 999999999)) + ".txt", "a") as sensitiveinfo:
					sensitiveinfo.write("=====================================================\n")
					sensitiveinfo.write(f"File: {match[0]}\n")
					sensitiveinfo.write(f"Line Number: {match[1]}\n")
					sensitiveinfo.write(f"Line: {match[2]}\n")
					sensitiveinfo.write("=====================================================\n")
			# Google API Key Scanner Started
			googleapi = GoogleAPIKeyExtractor.GoogleAPI.google_apikey_extract(apkfile)
			if googleapi is not False:
				GoogleAPIKeyExtractor.GoogleAPIKeyVulnScan.scan_gmaps(googleapi.replace("'", ""))
				print("[+] Google API Key : " + googleapi.replace("'", ""))
				print("[+] Google API Key completed successfully!")
			else:
				print("[+] Google API Key : Not Found!")
			# Firebase Scanner Starting...
			FirebaseExtractor.Firebase.main(apkfile)
			# Janus Exploitation Started...
			Janus.Janus.main(apkfile)
			# APK Extractor Starting...
			APKExtractor.Extract.main(apkfile)
			# APK Scanner END
		except KeyboardInterrupt:
			print("[+] Cleaning trash files")
			path = os.path.splitext(os.path.basename(apkfile))[0]
			Run.remove_folder(path)
			Run.remove_folder(path + "_src")
		except Exception as e:
			print("ERROR : " + str(e))


try:
	Run.main(sys.argv[1])
except IndexError:
	print("Example Usage : python main.py apk_name.apk")