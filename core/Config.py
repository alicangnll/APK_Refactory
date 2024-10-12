import os
name_of_the_DEX2JAR_directory = "dex2jar"
name_of_the_cfr_jar = "tools/cfr/cfr.jar"
dexDir = "tools/" + name_of_the_DEX2JAR_directory
cfrDir = name_of_the_cfr_jar
SENSITIVE_KEYWORDS = ['token', 'TOKEN', 'TOKENS', 'tokens', ' key ', 'password', 'secret', 'SECRET', 'confidential', '_key', '_token', 'api_key', 'firebaseio']
FNULL = open(os.devnull, 'w')