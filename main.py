import rsa

# TODO Change this to a useful interface

# Generate our keys
n, e, d = rsa.generate_keys(4)

print("n:\t" + str(n))
print("e:\t" + str(e))
print("d:\t" + str(d))

# Create the message to encrypt
message = 1024

print("Original message: " + str(message))

print("Encrypting {} with public key: n={} | e={}:".format(message, n, e))

# Encrypt using public key
ciphertext = rsa.encrypt(message, n, e)

print("ciphertext: " + str(ciphertext))

print("Decrypting {} with private key: d={} | n={}:".format(ciphertext, d, n))

# Decrypt using private key
decrypted_message = rsa.decrypt(ciphertext, d, n)

print("decrypted: " + str(decrypted_message))
