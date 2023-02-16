# getstatus
> Descript
```
Console script.

Detect online/offline mode user
and save history log in/out telegram
```

Save in file `file_status_<username>.log`


***

> Install
```
git clone git@github.com:YuranIgnatenko/getstatus.git
```
***

> Requirements

```bash
# python3
pip3 install telethon
```

***

> Configure
```bash
# path: ~/getstatus/config/config.json
{
    "api_hash":"8d7sfsdf7sd8yf8g78s7dfy87gdfy8gv",
    "api_id":"998877",
    "delay_sec":0
}
```

***

> First Launch

```bash
cd ~/getstatus/
python3 getstatus.py test 1
# Enter phone-number
# Wait Check-message code
# Enter code
```

> Examples:
``` bash
# using:
bash run.sh [target]

# set target-user:
bash run.sh Alice 
bash run.sh @Alice_998877 
bash run.sh +79008007060 
bash run.sh 89008007060 
