# other tutorial:http://www.pythonforbeginners.com/code-snippets-source-code/how-to-use-ftp-in-python
from ftplib import FTP
ftp = FTP('host.name.org')
ftp.login('username','password')
ftp.cwd('../') #change current working directory
ftp.retrlines('LIST') # ls command over FTP
ftp.retrbinary('RETR README', open('README','wb').write) #write a binary file locally called README
ftp.quit()
