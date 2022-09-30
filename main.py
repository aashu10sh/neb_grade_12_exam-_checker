import requests
BETWEEN = 60
import time
from datetime import datetime
import pytz
NEPAL_TIMEZONE = pytz.timezone("Asia/Kathmandu")

class config():
    api_key_of_bot = "YOUR_BOT_API_KEY"
    chat_id = "YOUR_CHAT_ID_OF_BOT_CURRENTLY_TALKING_TO" #https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

class check_if_its_out():
    def __init__(self,url="https://neb.ntc.net.np/"):
        self.between = BETWEEN
        self.url = url

    def telegram_send(self,message:str):
        params = {
                "chat_id":config.chat_id,
                "text":message
        }
        
        resp = requests.get(f"https://api.telegram.org/bot{config.api_key_of_bot}/sendMessage",params=params)
        
        
        return None

    def check_website(self):
        return requests.get(self.url,verify=False).text
    
    @staticmethod
    def log_data(data:str):
        with open('data.dat','a') as writer:
            writer.write(f"{data} :: {datetime.now(NEPAL_TIMEZONE)} \n")
    

    def main(self):
        count = 0
        while True:
            print("Website Checked {} times".format(count))
            try:
                if "COMING SOON " in self.check_website():
                    message = "Not Out Yet"
                    self.telegram_send(message)
                    check_if_its_out.log_data(message)
                else:

                    self.telegram_send("Maybe its out boys, check fast")
                print("after ")
                print(self.between)
                time.sleep(self.between)
                count = count+1

            except KeyboardInterrupt as e:
                print("Keyboard press detected, quitting",e)
                exit(1)
            except Exception as e:
                print(e)
                self.telegram_send(str(e))


if  __name__ == "__main__":
   checker_now = check_if_its_out()
   checker_now.main()
