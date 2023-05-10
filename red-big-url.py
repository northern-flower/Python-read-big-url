import urllib.request as urllib2

file = urllib2.urlopen('https://app.jobboost.io/feed/zKeRYqfpcHz-vacant-paid')

with open('filename.txt','w') as f:
    while True:
        tmp = file.read(2048)
        print(tmp)                
        if not tmp:
            break 
        f.write(tmp)
