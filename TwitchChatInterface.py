import queue
import IrcController
import MessageHandler
import time
import threading
from EventHandler import EventHandler
from datetime import datetime

class TCI(object):
    """    
        Bulids connection, receives chat messages from server and emits corrisponding events! 

        This library closely follows twitch docs https://dev.twitch.tv/docs/irc

        All functions or methods used as event callbacks need to have 2 input varibles
         
        Example of how to use this

        .. literalinclude:: example.py

        This is the message object that is sent with event 

        .. code-block::
        
            class Message:
                raw: str # the raw unparsed message string from server
                channel: str # the channel the message is from  
                id: str # id of message 
                prefix: str # there is 3 types of prfixes 
                command: str # the is the command which is also the event name
                text: str # the context of the message 
                username: str # the person who has sent the message
                params: List[str] # this is a break down of the end of message 
                tags: Dict # these are twitch tags look 
    """
    def __init__(self,settings: dict):
      
        # private properties
        self._channels: list = settings.get('channels')
        self._user: str = settings.get('user')
        self._password: str = settings.get('password')
        self._caprequest: str = settings.get('caprequest')
        self._server = IrcController.IrcController(settings.get("server"),settings.get("port"))
        self._messageHandler: MessageHandler = MessageHandler.MessageHandler()
        self._sendQ: queue.SimpleQueue = queue.SimpleQueue()

        # public properties
        self.event: EventHandler = EventHandler
        self.COMMANDS: MessageHandler.COMMANDS = self._messageHandler.COMMANDS
        self.startWithThread=threading.Thread(target=self.start, daemon=True).start
        self.channels: dict = {} 
        self.globalUserState: MessageHandler.globalUSerState = MessageHandler.globalUSerState()

        # Register System Event functions
        self.event.on(self.COMMANDS.CONNECTED, self._onConnected)
        self.event.on(self.COMMANDS.NOTICE, self._onNotice)
        self.event.on(self.COMMANDS.ROOMSTATE, self._onRoomState)
        self.event.on(self.COMMANDS.USERSTATE, self._setUserState)
        self.event.on(self.COMMANDS.MESSAGEIDS.ROOM_MODS, self._setChannelMods)
        self.event.on(self.COMMANDS.GLOBALUSERSTATE, self._setGlobalUserSate)
        self.event.on(self.COMMANDS.ROOMSTATE.EMOTE_ONLY, self._onEmotesOnly)
        self.event.on(self.COMMANDS.ROOMSTATE.FOLLOWERS_ONLY, self._onFollowersOnly)
        self.event.on(self.COMMANDS.ROOMSTATE.SLOW, self._onSlowMode)
        self.event.on(self.COMMANDS.ROOMSTATE.SUBS_ONLY, self._onSubsOnly)
        self.event.on(self.COMMANDS.ROOMSTATE.R9K, self._onR9k)

    def start(self)->None:
        """
        TwitchChatInterface.start - connects to server, logins in and starts send and recieve threads 
        
        """
        self._server.connect()
        self._login()
        threading.Thread(target=self._emptyMsgQ, daemon=True).start()
        threading.Thread(target=self._getMsgs, daemon=True).start()     

    def _getMsgs(self)->None:
        """
        TwitchChatInterface._getMsgs [summary]
        """
        data=""
        while self._server.isConnected():
            time.sleep(.1)
            data = self._server.receive()
            if data is not None:
                messageParts: list(str) = data.split("\r\n")
                for messagePart in messageParts:
                    self.event.emit(self,self.COMMANDS.RECEIVED, messagePart)
                    event, msg = self._messageHandler.handleMessage(messagePart)
                    if event is not None:
                        self.event.emit(self, event, msg)

    def _emptyMsgQ(self)->None:
        """
        TwitchChatInterface._emptyMsgQ [summary]
        """
        while self._server.isConnected():
            if not self._sendQ.empty():
                self._server.send(self._sendQ.get())
                time.sleep(1)

    def _login(self)->None:
        """[summary]
        """

        self._sendQ.put(f"CAP REQ :{self._caprequest}")
        self._sendQ.put(f"PASS {self._password}")          
        self._sendQ.put(f"NICK {self._user}")

    def _onConnected(self, sender: object, message)->None:
        """
        TwitchChatInterface._onConnected - event callback function
        
        :param sender: what is reasponsible for event
        :type sender: object
        :param message: irc message
        :type message: Message
        """
        if self._channels is not None:
            self.join(self._channels) 

    def _onRoomState(self, sender: object, message)->None:
        """
        _onRoomState [summary]
        
        :param sender: what is reasponsible for event
        :type sender: object
        :param message: irc message
        :type message: Message
        """
        if len(message.tags) >= 3:
            self._setRoomState(message)
        elif len(message.tags) <= 2:
            self._updateRoomState(message)
                    
    def _onNotice(self, sender: object, message)->None:
        """
        _onNotice [summary]
        .
        :param sender: what is reasponsible for event
        :type sender: object
        :param message: irc message
        :type message: Message
        """
        self.event.emit(self, message.id, message) 

    def _setRoomState(self, message)->None:
        """
        _setRoomState [summary]
        
        :param channel: [description]
        :type channel: str
        :param tags: [description]
        :type tags: list
        """
        if message.channel not in self.channels:
            self.channels[message.channel]: MessageHandler.Channel  = MessageHandler.Channel()

        self.channels[message.channel].roomID = message.tags.get(self.COMMANDS.ROOMSTATE.ROOM_ID)
        self.channels[message.channel].name = message.channel

        for key in message.tags:
            if key != self.COMMANDS.ROOMSTATE.ROOM_ID:
                setattr(self.channels[message.channel].roomState, key.replace('-','_'), message.tags.get(key))
        self._getMods(message.channel)

    def _updateRoomState(self, message)->None:
        """
        _updateRoomState [summary]
        
        :param channel: [description]
        :type channel: str
        :param tags: [description]
        :type tags: dict
        """
        for key in message.tags:
            if key != self.COMMANDS.ROOMSTATE.ROOM_ID:
                setattr(self.channels[message.channel].roomState, key.replace('-','_'), message.tags.get(key))
                self.event.emit(self, key, message)

    def _setChannelMods(self, sender: object, message)->None:
        """
        _setChannelMods [summary]
        
        :param sender: [description]
        :type sender: object
        :param message: [description]
        :type message: Message
        """
        self.channels[message.channel].mods = message.params[1].split(':')[1].split(',')
    
    def _setUserState(self, sender, message):
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        if message.channel not in self.channels:
            self.channels[message.channel]: MessageHandler.Channel  = MessageHandler.Channel()
        for key in message.tags:
            setattr(self.channels[message.channel].userState, key.replace('-','_'), message.tags.get(key))
        
    def _setGlobalUserSate(self, sender, message)->None:
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        for key in message.tags:
            setattr(self.globalUserState, key.replace('-','_'), message.tags.get(key))
        
    def _getMods(self, channel: str)->None:
        """
        getMods [summary]
        
        :param channel: [description]
        :type channel: str
        """
        self.sendMessage(channel,"/mods")
    
    def _onEmotesOnly(self, sender, message):
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        if message.tags[self.COMMANDS.ROOMSTATE.EMOTE_ONLY]:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.EMOTE_ONLY_ON, self.channels[message.channel])
        else:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.EMOTE_ONLY_OFF, self.channels[message.channel])

    def _onFollowersOnly(self, sender, message):
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        if message.tags[self.COMMANDS.ROOMSTATE.FOLLOWERS_ONLY] > -1:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.FOLLOWERS_ONLY_ON, self.channels[message.channel])
        else:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.FOLLOWERS_ONLY_OFF, self.channels[message.channel])

    def _onSlowMode(self, sender, message):
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        if message.tags[self.COMMANDS.ROOMSTATE.SLOW] > 0:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.SLOW_ON, self.channels[message.channel])
        else:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.SLOW_OFF, self.channels[message.channel])

    def _onSubsOnly(self, sender, message):
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        if message.tags[self.COMMANDS.ROOMSTATE.SUBS_ONLY]:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.SUBS_ONLY_ON, self.channels[message.channel])
        else:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.SUBS_ONLY_OFF, self.channels[message.channel])

    def _onR9k(self, sender, message):
        """[summary]
        
        :param sender: [description]
        :type sender: [type]
        :param message: [description]
        :type message: [type]
        """
        if message.tags[self.COMMANDS.ROOMSTATE.R9K]:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.R9K_ON, self.channels[message.channel])
        else:
            self.event.emit(self, self.COMMANDS.ROOMSTATE.R9K_OFF, self.channels[message.channel])
    
    def _addChannel(self, channel: str)->None:
        """[summary]
        
        :param channel: [description]
        :type channel: str
        """
        if channel not in self.channels:
            channel = self._formatChannelName(channel)
            self.channels[channel]: MessageHandler.Channel = MessageHandler.Channel()
            self.channels[channel].name = channel

    def _removeChannel(self, channel: str)->None:
        """[summary]
        
        :param channel: [description]
        :type channel: str
        """
        if channel in self.channels:
            channel = self._formatChannelName(channel)
            del(self.channels[channel])
    
    def _formatChannelName(self, channel:str)->str:
        """[summary]
        
        :param channel: [description]
        :type channel: str
        :return: [description]
        :rtype: str
        """
        return channel if channel.startswith("#") else f"#{channel}"

    def join(self, channels: list)->None:
        """
        join [summary]
        
        :param channels: [description]
        :type channels: list
        """
        for channel in channels:
            channel = self._formatChannelName(channel)
            self._addChannel(channel)
            self._sendQ.put(f"JOIN {channel}" if '#' in channel else f"JOIN #{channel}")
    
    def part(self, channels: list):
        """[summary]
        
        :param channels: [description]
        :type channels: list
        """
        for channel in channels:
            channel = self._formatChannelName(channel)
            self._removeChannel(channel)
            self._sendQ.put(f"PART {channel}" if '#' in channel else f"PART#{channel}")

    def sendMessage(self, channel: str, message: str)->None:
        """
        sendMessage [summary]
        
        :param channel: [description]
        :type channel: str
        :param message: [description]
        :type message: str
        """
        self._sendQ.put(f"PRIVMSG {'#' if '#' not in channel else ''}{channel} :{message}")

    def sendWhisper(self, channel: str, username: str, message: str)->None:
        """
        sendWhisper [summary]
        
        :param channel: [description]
        :type channel: str
        :param username: [description]
        :type username: str
        :param message: [description]
        :type message: str
        """
        self._sendQ.put(f"PRIVMSG {'#' if '#' not in channel else ''}{channel} :/w {username} {message}")

    def timeoutUser(self, channel: str, username: str, duration: int)->None:
        """
        timeoutUser [summary]
        
        :param channel: [description]
        :type channel: str
        :param username: [description]
        :type username: str
        :param duration: [description]
        :type duration: int
        """
        self._sendQ.put(f"PRIVMSG #{'#' if '#' not in channel else ''}{channel} :/timeout {username} {duration}")
   
    def onMessage(self, func)->None:
        """
        onMessage [summary]
        
        :param func: [description]
        :type func: 
        """
        self.event.on(self.COMMANDS.MESSAGE, func)
    
    def onWhisper(self, func):
        """
        onWhisper [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.WHISPER, func)

    def onRoomState(self, func):
        """
        onRoomState [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE, func)

    def onMsgId(self, msgid, func):
        """
        onMsgId [summary]
        
        :param msgid: [description]
        :type msgid: [type]
        :param func: [description]
        :type func: [type]
        """
        self.event.on(msgid, func)
    
    def onNotice(self, func):
        """
        onNotice [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.NOTICE, func)

    def onReceived(self, func):
        """
        onReceived [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.RECEIVED, func)

    def onConnected(self, func):
        """
        onConnected[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.CONNECTED, func)

    def onLoginError(self, func):
        """
        onLoginError [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.LOGIN_UNSUCCESSFUL, func)

    def onGlobalUserState(self, func):
        """
        onGlobalUserState [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.GLOBALUSERSTATE, func)

    def onUserState(self, func):
        """
        onUserState [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.USERSTATE, func)
    
    def onUserNotice(self, func):
        """
        onUserNotice [summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.USERNOTICE, func)

    def onEmotesOnlyOn(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.EMOTE_ONLY_ON, func)

    def onEmotesOnlyOff(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.EMOTE_ONLY_OFF, func)

    def onSubsOnlyOn(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.SUBS_ONLY_ON, func)

    def onSubsOnlyOff(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.SUBS_ONLY_OFF, func)  

    def onFollersOnlyOn(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.FOLLOWERS_ONLY_ON, func)
    
    def onFollersOnlyOff(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.FOLLOWERS_ONLY_OFF, func)

    def onSlowModeOn(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.SLOW_ON, func)

    def onSlowModeOff(self, func):
        """[summary]
        
        :param func: [description]
        :type func: [type]
        """
        self.event.on(self.COMMANDS.ROOMSTATE.SLOW_OFF, func)