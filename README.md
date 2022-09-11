# MixList
MixList it this script  hele to  generate Password list and username mix with your account username and passowrd to try bypass
Broken brute-force protection, IP block
* [Test lab at PortSwigger](https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block)
## How to use 
-----------------------
* git clone https://www.github.com/jac11/MixList.git
* cd MixList 
* chmod +x MixList.py
### Command 
-------------------
```
MixList.py -VU carlos -MU wiener -W  passwords -R 100 -MP peter -O list
````
### breakdown the command :
----------------
* ./MisList.py "the name of the script"
* -VU "the username of vctim target account
* -MU "my username of my aconut" note : if you traget vcitm facebook " your username is real of your facebook accout"
* -W the  Path of the word list will be use to brute force
* -R how many passord and user name you will be generate
* -MP 'my password for my account" real password
* -O output file of the lists will be generate "Note : if you give "-O list" output of the username list become "list_Mix_name" and list of passpwrd become "list_Mix_pass" all file you will found at same dir "MixList"
### Note:
   * be defult MixList have smail password wordlist so you can use or you can give any anther password wordlist
   * support Json Format 
### 
------------------------------------------
[vidoe from Port SWigger  Acdmy  ](https://www.youtube.com/watch?v=BoA-ms_h3HY)
_____________________________________
### Commcet me :
 * jac11devel@gmail.com
 * thank you
