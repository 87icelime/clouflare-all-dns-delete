# Delete all DNS records from Cloudflare
> [Note : Due to api rate limitation, This code can only delete upto 100 records at once, Rerun the code if you want to delete more than 100 DNS Records]

### Requirements 
* IDE 
* Python3
* Package : requests 2.29.0 or higher 
* Cloudflare API Key 
* Cloudflare ZONE ID

### GUIDE 
1) Replace `YOUR_API_KEY` with the api key you will get from the cloudflare
2) Replace `YOUR_ZONE_ID` with your zone id 
3) run the code

### Where can I get my Cloudflare API & Zone ID? 
1) Go to https://dash.cloudflare.com/
<br>![](./assets/1.png)
2) Select the Domain from where you want to delete all the dns
<br>![](./assets/2.png)
3) Scroll down and look at the right side. Here youll see you zone id. Simply copy it.
![3](./assets/3.png)
4) Now you can click on the "Get your api key token" or just go to [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)
5) Youll seean interface like the picture below. Follow the instructions mentioned in the image
<br>![4](./assets/4.png)
6) 
<br>![5](./assets/5.png)
7) 
<br>![6](./assets/6.png)
8) 
<br>![8](./assets/8.pnng)
9)
<br>![9](./assets/9.png)



