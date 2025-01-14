# Encrypt and Decrypt the message using inheritance
class Encrypt:
    def __init__(self):
        self.send = ""
        self.resv = []

    # Sender Encrypts the message
    def sender(self):
        self.send = input("Enter the message to send: ")
        self.resv = [ord(i) + 2 for i in self.send]
        print(f"Encrypted message: ", "".join(chr(i) for i in self.resv))

class Decrypt(Encrypt):
    # Receiver Decrypts the message
    def receiver(self):
        print(f"Decrypted message: ", "".join(chr(i-2) for i in self.resv))

obj = Decrypt()
obj.sender()
obj.receiver()
