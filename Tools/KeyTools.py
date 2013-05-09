__author__ = 'jurek'
import threading
class GenerateKey(threading.Thread): #Thread in which generating GPG Keys will be performed
    def __init__(self,key_to_save, gpg):
        threading.Thread.__init__(self)
        self.key_to_save = key_to_save
        self.gpg = gpg
    def find_id(self): # Find
        for key in self.gpg.list_keys():
            if key['fingerprint'] == self.key_to_save.key_fingerprint:
                self.key_to_save.key_id = key['keyid']
    def run(self):
        input_data = prepareInputData(self.key_to_save,self.gpg)
        key = self.gpg.gen_key(input_data)
        fingerprint = key.fingerprint
        self.key_to_save.key_fingerprint = fingerprint
        self.find_id()
        self.key_to_save.save()
def prepareInputData(key,gpg):
    result = gpg.gen_key_input(key_type=key.key_type,key_length=key.key_length,name_real=key.key_real,name_comment=key.key_comment,name_email=key.key_email,passphrase=key.key_password)
    return result
