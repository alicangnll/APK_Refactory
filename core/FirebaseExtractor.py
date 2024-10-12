from subprocess import Popen, PIPE, STDOUT
class Firebase:
	def main(apk):
		print("[+] Firebase Extractor is Starting...")
		firebaseio_search = f'strings {apk} | grep -iE ".*\.firebaseio\.com"'
		firebase = Popen(firebaseio_search, shell=True, stdout=PIPE, stderr=STDOUT).communicate()[0]
		firebase = firebase.decode('utf-8').strip()

		firebase_appspot_search = f'strings {apk} | grep -iE ".*\.appspot\.com"'
		firebase_appspot = Popen(firebase_appspot_search, shell=True, stdout=PIPE, stderr=STDOUT).communicate()[0]
		firebase_appspot = firebase_appspot.decode('utf-8').strip()
		if firebase == "":
			print("[+] Firebase DB : NOT FOUND")
		else:
			cutfrom = firebase.index('http')
			apkFirebaseURL = firebase[cutfrom:]
			print("[+] Firebase Extractor completed successfully!")
			print("[+] Firebase DB : " + apkFirebaseURL)
		
		print("[+] AppSpot Extractor is Starting...")
		if firebase_appspot == "":
			print("[+] AppSpot : NOT FOUND")
		else:
			print("[+] AppSpot : " + firebase_appspot)
			print("[+] AppSpot Extractor completed successfully!")