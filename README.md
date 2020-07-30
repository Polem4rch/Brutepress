# Brutepress

Wordpress Bruteforce based in CVE-2017-5487

DISCLAIMER: All the scripts should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.

Brutepress will look for users exposed in any wordpress site, retrieve them and brute force them using WPSCAN (required)

Requirements:

WPSCAN installed 

Any dictionary

Usage:

Python3 brutepress.py

Youll be prompted to input a wordpress site, please check if its a http:// or https:// site,
If users are found a list will appear, please choose any from 0, then
add your dictionary path.

When running the wpscan script, will provide some details from the site including:

Headers

Robots.txt

XML-RPC

External WP-CRON

Wordpress Version

Wordpress Theme Used

Plugins

Backups


Please Note:
Some sites might have some kind of protection, some will block the usernames exposure altogether and other might block multiple login attemps, hence blocking the ip.

Special Thanks to Danners
