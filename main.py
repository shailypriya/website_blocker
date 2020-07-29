#from datetime import date
#from datetime import time

from datetime import *

host_path = "C:\\Windows\\System32\\drivers\\etc"
redirect = "127.0.0.1"

website_list = ["www.facebook.com","www.instagram.com"]

start_date = datetime(2020,7,29)
end_date = datetime(2020,7,30)
today_date = datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if start_date <= today_date < end_date:
        with open(host_path,"r+") as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
        print("All sites are blocked!")
        break
    else:  #end_date < today_date
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
        print("All sites are unblocked!")
        break

