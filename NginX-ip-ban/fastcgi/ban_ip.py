#!/usr/bin/env python3
import cgi
import datetime

BANNED_IP_FILE = "/usr/local/fastcgi/banned_ips.txt"

def add_ip_to_ban(ip):
    now = datetime.datetime.now()
    expire_time = now + datetime.timedelta(hours=1)

    with open(BANNED_IP_FILE, "a") as f:
        f.write(f"{ip} 1;\n")

    print("Content-Type: text/plain")
    print()
    print(f"IP {ip} has been banned until {expire_time}.")

def main():
    form = cgi.FieldStorage()
    ip = form.getvalue("ip")
    
    if ip:
        add_ip_to_ban(ip)
    else:
        print("Content-Type: text/plain")
        print()
        print("No IP provided.")

if __name__ == "__main__":
    main()
