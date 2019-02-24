import sys, time, datetime
File_Name_AES_Key = "key"
File_Name_RSA_Key = "id_rsa"
File_Name_RSA_Pub_Key = "id_rsa.pub"
count=1
try:
    input = sys.argv[1]
    if(len(input) > 7):
        print("Length must be less than 7 bytes")
        exit()
except IndexError:
    print("You need to provide a message to encrypt")
    exit()

# Start stopwatch to measure AES performance
AES_start_time = time.time()
# AES Encrypt and Decrypt count times
for x in range(0, count):
    # do encryption and decryption
    time.sleep(3)

# calculate average time
AES_end_time = time.time()
AES_uptime = AES_end_time - AES_start_time
AES_average_time = str(datetime.timedelta(seconds=int(AES_uptime/count)))

# Start stopwatch to measure RSA performance
RSA_start_time = time.time()
# RSA Encrypt and Decrypt count times
for x in range(0, count):
    # do encryption and decryption
    time.sleep(3)

RSA_end_time = time.time()
RSA_uptime = RSA_end_time - RSA_start_time
RSA_average_time = str(datetime.timedelta(seconds=int(RSA_uptime/count)))

# Print Averages
print("Average AES encryption and decryption time: " + AES_average_time)
print("Average RSA encryption and decryption time: " + RSA_average_time)