#imports
from tkinter import *
import twitter
import pandas as pd
import os

#API KEYS
Tw = twitter.Api(
consumer_key = 
"Rk5UBngGCOaUo5zkYLpe7V7je",
consumer_secret = "kaTB3spCOWlNiElrWCWeEskXpqU86CLwypA1UcnSPy9uiKuz74",
access_token_key = 
"903158339499986944-f7lQtt8K8TTh6RrDaB3qzrttAtTaGZC",
access_token_secret = 
"lwPeMA34AA9Hp6apEQErxfXyfHq4gXNQnoydv4pL1gx75")


#Variables
numTweets = 30  #total max number of tweets to search
labels = []     #stores all the labels made
csvList = []    #stores data to save to a CSV


#This will Query Twitter and display the results 
def getTweets():
    #get the Query
    tweet = Tw.GetSearch(raw_query =
    "q=IoT%20&count={}&src=typd".format(numTweets))
    
    #Reset Variables
    counter = 0
    csvList = []

    #Create Labels
    for t in tweet:
        if counter < 10:
            try:
                #creates the Label
                splitTweet = t.text.split("RT ")
                
                tweetGUI = Label(master,
                text = 
                "{}".format(counter+1) + ': ' + 
                t.user.screen_name + " ID: " 
                + "{}".format(t.id) + 
                '\n' + splitTweet[1] + '\n')
                
                tweetGUI.pack()
                labels.append(tweetGUI)
                
                #save data to the CSV List
                csvList.append([t.user.screen_name,
                "ID: {}".format(t.id),
                "{}".format(splitTweet[1]),
                counter+1])
                
                #Increase counter to limit searches to 10
                counter += 1
            except:
                #Note: Some unicodes throw erros
                #This will catch those errors
                pass
    return csvList  #Stores all the queried tweets

#Get New Tweets
#Will only work after a certain time fram
#Best guess is that twitter limites API Queries
#Note to self: Look into removing this limit
def refresh():
    for l in labels:
        l.pack_forget()
    global csvList
    csvList = getTweets()
    

#Save to a database CSV file
def saveCSV():
    global csvList
    if not csvList == []:
        #removes the old file
        #for an iterative database, this line can be deleted
        #however we will then need to implement a scrollbar to search through
        #all return strings
        if os.path.exists("database.csv"):
            os.remove("database.csv")
        
        df = pd.DataFrame(csvList)
        df.to_csv("database.csv",index = False,header = False)
    else:
        print("not Saved")

#read and display CSV        
def readCSV():
    pd.set_option('display.max_colwidth',400)
    df = pd.read_csv("database.csv",header=None)
    
    #remove all old labels
    for l in labels:
        l.pack_forget()
        
    #display the data
    for index,row in df.iterrows():
        tweetGUI = Label(master,
        text = 
        "{}".format(row[3]) + ': {}'.format(row[0]) + " ID: " 
        + "{}".format(row[1]) + 
        '\n {}'.format(row[2]) + '\n')
        tweetGUI.pack()
        labels.append(tweetGUI)


if __name__ == '__main__':
    print("Test Program")
    master = Tk()
    
    #Title of program
    master.title("Test Title")
    
    
    #creates GUI window
    guiFrame = Frame(master)
    
   
    #Places all Labels and widgets into the GUI
    guiFrame.pack()
    
   
    #Creates a Refresh Button and places it into the GUI
    button = Button(master, text="Refresh", command=refresh)
    button.pack()
    
    #Creates a Save Button and places it into the GUI
    button2 = Button(master, text="Save", command=saveCSV)
    button2.pack()
    
    #Creates a Offline Button and places it into the GUI
    button3 = Button(master, text="Offline", command=readCSV)
    button3.pack()
    
    #Show and Get Tweets
    #showTweets(getTweets(), numTweets)
    csvList = getTweets()
  
    #Continue until close
    master.mainloop()
