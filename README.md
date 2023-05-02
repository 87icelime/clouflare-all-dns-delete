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
1) Go to [https://dash.cloudflare.com/](https://dash.cloudflare.com/)
<br>![1](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/1.PNG)
2) Select the Domain from where you want to delete all the dns
<br>![2](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/2.PNG)
3) Scroll down and look at the right side. Here youll see you zone id. Simply copy it.
![3](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/3.PNG)
4) Now you can click on the "Get your api key token" or just go to [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)
5) Youll seean interface like the picture below. Follow the instructions mentioned in the image
<br>![4](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/4.PNG)
6) 
<br>![5](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/5.PNG)
7) 
<br>![6](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/6.PNG)
8) 
<br>![8](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/8.PNG)
9)
<br>![9](https://github.com/87icelime/clouflare-all-dns-delete/blob/e379346100e52c639fb6cf0d2339412b16f2eb9f/assets/9.PNG)

> Everyone is welcome to contribute! 



