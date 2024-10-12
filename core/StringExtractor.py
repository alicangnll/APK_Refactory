class StringExtractor:
    @staticmethod
    def findstrings(thedata):
        count = 0  # This keeps track of consecutive printable characters
        charslist = []  # Place to keep characters
        printable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/\.,1234567890!@#$%^&*(){}[]"
        found_strings = []  # List to store found strings

        for character in thedata:
            if character in printable:
                charslist.append(character)
                count += 1
            else:
                if count >= 4:
                    found_strings.append(''.join(charslist[-count:]))
                count = 0
        
        if count >= 4:
            found_strings.append(''.join(charslist[-count:]))
        
        return found_strings

    def main(name):
        fd = open(name, "rb")
        data = fd.read().decode("utf-8", "ignore")
        fd.close()
        print("[+] String Extractor is Starting...")
        string = StringExtractor.findstrings(data)

        with open(str(name).replace(".", "_") + "_logs.txt", "w") as logging:
            for strval in string:
                logging.write(strval + "\n")
            print("[+] Logs saved to " + name + "_logs.txt")
        print("[+] String Extractor completed successfully!")