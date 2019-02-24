import sys, time, datetime
File_Name_AES_Key = "key"
File_Name_RSA_Key = "id_rsa"
File_Name_RSA_Pub_Key = "id_rsa.pub"
try:
    input = sys.argv[1]
    if(len(input) > 7):
        print("Length must be less than 7 bytes")
        exit()
except IndexError:
    print("You need to provide a message to encrypt")
    exit()

# Start stopwatch to measure performance
start_time = time.time()
time.sleep(1)
end_time = time.time()

# Import AES Encrypt and Decrypt


uptime = end_time - start_time
human_uptime = str(datetime.timedelta(seconds=int(uptime)))
print human_uptime