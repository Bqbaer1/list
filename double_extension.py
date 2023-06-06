import requests

# response = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/web-extensions.txt")
extensions = ['.php', '.phtml', '.php4', '.php5', '.php7', '.phps', '.php3', '.phps', '.phpt', '.phar']


with open("wordlist.txt", "w") as file:
    # special_chars = ['%20', '%0a', '%00', '%0d0a', '/', '.\\', '.', '…', ':']


        for ext in extensions:
         #   file.write(f"shell{char}{ext}.jpg\n")
          #  file.write(f"shell{ext}{char}.jpg\n")
           # file.write(f"shell.jpg{char}{ext}\n")
            #file.write(f"shell.jpg{ext}{char}\n")
           
           file.write(f"shell{ext}.jpg\n")
          
           file.write(f"shell.jpg{ext}\n")
