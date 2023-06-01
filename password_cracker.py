import hashlib
topPasswords = open("top-10000-passwords.txt").read().split('\n')
knownSalts = open("known-salts.txt").read().split('\n')

def crack_sha1_hash(hash, use_salts = False):
    for p in topPasswords:
        if(hash == hashlib.sha1(p.encode('utf-8')).hexdigest()):
            return p
        if(use_salts):
            for s in knownSalts:
                prepend = s + p
                append = p + s
                if(hash == hashlib.sha1(prepend.encode('utf-8')).hexdigest()):
                    return p
                if(hash == hashlib.sha1(append.encode('utf-8')).hexdigest()):
                    return p
    return "PASSWORD NOT IN DATABASE"