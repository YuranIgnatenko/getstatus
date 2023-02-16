from telethon.sync import TelegramClient
import os, sys, json, time


target_user = sys.argv[1]
count_scan = sys.argv[2]
session_file = "newSessionStatus"
symsplit = "&"
config_file = 'config.json'
prefix = "file_status_"
postfix = ".log"


class Bot():
    def __init__(self, api_hash, api_id, namefilelog, phone, delay_sec):
        self.ErrorFindUser = "UserNotFound"
        self.api_hash = api_hash 
        self.api_id = api_id
        self.namefile = namefilelog
        self.target_user = phone
        self.status_user = ""
        self.delay_sec = delay_sec
        self.symsplit = symsplit
        self.client = TelegramClient(session_file, api_id, api_hash)
        self.client.start()
        # warn init line
        for dialog in self.client.iter_dialogs():
            break
        self.check_file()

    def check_file(self):
        if os.path.isfile(self.namefile) == False:
            with open(self.namefile, "w+") as file:
                file.read() 

    def get_status(self, user_name):
        try:
            acc = str(self.client.get_entity(user_name).status).split("(")[0]
            return f"{acc}"
        except Exception as e:
            print(e)
            return f"{self.ErrorFindUser}"

    def write_file_line(self, status):
        with open(self.namefile, "a") as file:
            file.write(time.asctime() + self.symsplit + status + "\n")

    def old_status_from_file(self):
        with open(self.namefile, "r") as file:
            data = file.read().strip()
            if data == "":
                return self. ErrorFindUser
            data = data.split("\n")[-1]
            data = data.split(self.symsplit)[-1]
            return data
        
    def run(self):
        result = self.get_status(self.target_user)
        if self.old_status_from_file() != result:
            self.write_file_line(result)



def validate_flags():
    if len(sys.argv) != 3:	
        if len(sys.argv) == 1:
            print("Not found name: username, @username, +7999.. , 8999....")
            sys.exit(0)
        if len(sys.argv) == 2:
            print("Not found count-scans: (any int) or (0-while loop)")
            sys.exit(0)

    
def main():
    validate_flags()

    with open(config_file, 'r') as f:
        config = json.load(f)

    namefile = f"{prefix}{target_user}{postfix}"

    if int(count_scan) == 0:
        while True:
            b = Bot(config["api_hash"], config["api_id"], namefile, target_user, config["delay_sec"])
            b.run()
    else:
        for i in range(int(count_scan)):
            b = Bot(config["api_hash"], config["api_id"], namefile, target_user, config["delay_sec"])
            b.run()


main()
