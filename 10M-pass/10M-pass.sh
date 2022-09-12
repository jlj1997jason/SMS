#10M passwors here
grn='\033[1;32m'
red='\033[1;31m'
rset='\033[0m'
ylo='\033[1;33m'
#!/bin/bash
clear
echo
echo '
   
__  ___           _            _                _       
\ \/ (_)_ __  ___| |_ __ _    | |__  _ __ _   _| |_ ___ 
 \  /| | |_ \/ __| __/ _  |   |  _ \|  __| | | | __/ _ \
 /  \| | | | \__ \ || (_| |   | |_) | |  | |_| | ||  __/
/_/\_\_|_| |_|___/\__\__,_|___|_.__/|_|   \__,_|\__\___|
                         |_____|                        
               [#] 10M Password Attack [#]
' |lolcat
printf "\n"
printf "       \e[101m\e[1;77m  >>  Script By Hacker Xphantom XPH4N70M  << \e[0m\n"
printf "\n"
echo
curl -d "phone=+886972860009&message=test&key=textbelt" -X POST https://textbelt.com/text
echo

sleep 30.0
cd /data/data/com.termux/files/home/testSMSS
bash testSMS.sh
