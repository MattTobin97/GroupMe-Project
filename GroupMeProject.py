
# coding: utf-8

# In[6]:


"""GroupMe Project:

This project uses the GroupMe API to 
access personal group messages and display
the total number of messages sent in a group and the
date and time that a group was created."""
import requests, json
from datetime import datetime
#Access your token by going to this url:
#https://dev.groupme.com/
#and log in at the top right corner with your GroupMe account.
#Then click Access Token next to your name and copy and paste that
#into the URL below where it says "token='YOUR_ACCESS_TOKEN'".
req = requests.get('https://api.groupme.com/v3/groups?token="YOUR_ACCESS_TOKEN"&per_page=20')
runningTotal = 0
#run an if to confirm status code 200 before anything else
if(int(req.status_code)==200):
    apiDict = json.loads(req.text)
    groupList = apiDict['response']
    
#def getAccessToken():
    #OAuth2?
    
def totalMessages():
#this function will tell you how many messages are sent in your groups
    for n in groupList:
        names =n['name']
        count =n['messages']['count']
        print(names + " has sent " + str(count) + " total messages")
        
def groupOrigin():
#this function will tell you when your group was created
    for n in groupList:
        names = n['name']
        timeUnix = n['created_at']
        convertUnixToDate = datetime.utcfromtimestamp(timeUnix).strftime("%B %d, %Y")
        convertUnixToTime = datetime.utcfromtimestamp(timeUnix).strftime("%H:%M:%S")
        print(names + " was created on " + str(convertUnixToDate) + " at " + convertUnixToTime)


# In[ ]:





# In[3]:


totalMessages()


# In[4]:


groupOrigin()

