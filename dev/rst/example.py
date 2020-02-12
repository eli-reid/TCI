import TwitchChatInterface
    
settings = {"server": "irc.chat.twitch.tv", # the server address
            "port" : 6667,  #server port as interger
            "user" : "mybotsname", # you bots username
            "password" : "oauth: ", # password as twitch oauth
            "channels" : ["channel1","channel2"], # replace with any channels yopu want the bot join
            "caprequest" : "twitch.tv/tags twitch.tv/commands twitch.tv/membership" 
            }
# All functions or methods used as event callbacks need to have 2 input varibles 
#   sender: is what triggered event 
#   message: is the message

def handleMessage(sender, message):
    print(f"[{message.channel}] {message.username}: {message.text}")

def handleConnect(sender, message):
    print ("connected!", message)

def main():
    # setup server instance with settings as dict
    twitchChat = TwitchChatInterface.TwitchChatInterface(settings)

    # add function or method for a message event 
    twitchChat.onMessage(handleMessage)

    # add function or method for a server connected event 
    twitchChat.onConnected(handleConnect)

    # this starts the server and logins 
    twitchChat.start()

    # send a messaage to a channel
    twitchChat.sendMessage("channel1","Hello World!")

if __name__ == "__main__":
    main()