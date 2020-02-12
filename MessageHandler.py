from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class RoomState:
    """Data Type
    
    :param type: [description]
    :type type: [type]
    """
    emote_only: int  = field(default=0)
    rituals: int = field(default=0)
    followers_only: int  = field(default=0)
    r9k: int = field(default=0)
    slow: int  = field(default=0)
    subs_only: int = field(default=0)

@dataclass
class Message:
    """ Data Type """
    raw: str = ""
    channel: str = field(default="")
    id: str = field(default="")
    prefix: str = field(default="")
    command: str = field(default="")
    text: str = field(default="")
    username: str = field(default="")
    params: List[str] = field(default_factory=list)
    tags: Dict = field(default_factory=dict)

@dataclass
class globalUSerState:
    badge_info: str = field(default="")
    badges: Dict = field(default_factory=dict)
    color: str = field(default="")
    display_name: str = field(default="")
    emote_sets: str = field(default="")
    turbo: str = field(default="")
    user_id: str = field(default="")
    user_type: str = field(default="")
    
@dataclass
class UserNotice:
    """
     [summary]
    """
    badge_info: str = field(default="")
    badges: Dict = field(default_factory=dict)
    color: str = field(default="")
    display_name: str = field(default="")
    emote_sets: str = field(default="")
    turbo: str = field(default="")
    user_id: str = field(default="")
    user_type: str = field(default="")

@dataclass
class UserState:
    """ Data Type """
    badge_info: str = field(default="")
    badges: Dict = field(default_factory=dict)
    color: str = field(default="")
    display_name: str = field(default="")
    emote_sets: str = field(default="")
    turbo: str = field(default="")
    user_id: str = field(default="")
    user_type: str = field(default="")

@dataclass
class Channel:
    """ Data Type     """
    name: str = field(default="")
    roomID: str = field(default="")
    mods: list = field(default_factory=list)
    roomState: RoomState = field(default_factory=RoomState)
    userState: UserState = field(default_factory=UserState)

def IDEHelper(cls):
    """IDEHelper - changes magic functions to use _VALUE in constants with subtags
    
    :return: cls
    :rtype: class
    """
    def __eq__(self, value):
        return self._VALUE == value
    def  __hash__(self):
        return hash(self._VALUE)
    def  __str__(self):
        return self._VALUE
    cls.__eq__ = __eq__
    cls.__hash__ = __hash__
    cls.__str__ = __str__
    return cls

@dataclass(frozen=True)
class _MESSAGEIDS:
    """ Message id constants """

    ALREADY_BANNED: str = "already_banned"
    ALREADY_EMOTE_ONLY_OFF: str = "already_emote_only_off"
    ALREADY_EMOTE_ONLY_ON: str = "already_emote_only_on"
    ALREADY_R9K_OFF: str = "already_r9k_off"
    ALREADY_R9K_ON: str = "already_r9k_on"
    ALREADY_SUBS_OFF: str = "already_subs_off"
    ALREADY_SUBS_ON: str = "already_subs_on"
    BAD_BAN_ADMIN: str = "bad_ban_admin"
    BAD_BAN_ANON: str = "bad_ban_anon"
    BAD_BAN_BROADCASTER: str = "bad_ban_broadcaster"
    BAD_BAN_GLOBAL_MOD: str = "bad_ban_global_mod"
    BAD_BAN_MOD: str = "bad_ban_mod"
    BAD_BAN_SELF: str = "bad_ban_self"
    BAD_BAN_STAFF: str = "bad_ban_staff"
    BAD_COMMERCIAL_ERROR: str = "bad_commercial_error"
    BAD_DELETE_MESSAGE_BROADCASTER: str = "bad_delete_message_broadcaster"
    BAD_DELETE_MESSAGE_MOD: str = "bad_delete_message_mod"
    BAD_HOST_ERROR: str = "bad_host_error"
    BAD_HOST_HOSTING: str = "bad_host_hosting"
    BAD_HOST_RATE_EXCEEDED: str = "bad_host_rate_exceeded"
    BAD_HOST_REJECTED: str = "bad_host_rejected"
    BAD_HOST_SELF: str = "bad_host_self"
    BAD_MARKER_CLIENT: str = "bad_marker_client"
    BAD_MOD_BANNED: str = "bad_mod_banned"
    BAD_MOD_MOD: str = "bad_mod_mod"
    BAD_SLOW_DURATION: str = "bad_slow_duration"
    BAD_TIMEOUT_ADMIN: str = "bad_timeout_admin"
    BAD_TIMEOUT_ANON: str = "bad_timeout_anon"
    BAD_TIMEOUT_BROADCASTER: str = "bad_timeout_broadcaster"
    BAD_TIMEOUT_DURATION: str = "bad_timeout_duration"
    BAD_TIMEOUT_GLOBAL_MOD: str = "bad_timeout_global_mod"
    BAD_TIMEOUT_MOD: str = "bad_timeout_mod"
    BAD_TIMEOUT_SELF: str = "bad_timeout_self"
    BAD_TIMEOUT_STAFF: str = "bad_timeout_staff"
    BAD_UNBAN_NO_BAN: str = "bad_unban_no_ban"
    BAD_UNHOST_ERROR: str = "bad_unhost_error"
    BAD_UNMOD_MOD: str = "bad_unmod_mod"
    BAN_SUCCESS: str = "ban_success"
    CMDS_AVAILABLE: str = "cmds_available"
    COLOR_CHANGED: str = "color_changed"
    COMMERCIAL_SUCCESS: str = "commercial_success"
    DELETE_MESSAGE_SUCCESS: str = "delete_message_success"
    EMOTE_ONLY_OFF: str = "emote_only_off"
    EMOTE_ONLY_ON: str = "emote_only_on"
    FOLLOWERS_OFF: str = "followers_off"
    FOLLOWERS_ON: str = "followers_on"
    FOLLOWERS_ONZERO: str = "followers_onzero"
    HOST_OFF: str = "host_off"
    HOST_ON: str = "host_on"
    HOST_SUCCESS: str = "host_success"
    HOST_SUCCESS_VIEWERS: str = "host_success_viewers"
    HOST_TARGET_WENT_OFFLINE: str = "host_target_went_offline"
    HOSTS_REMAINING: str = "hosts_remaining"
    INVALID_USER: str = "invalid_user"
    MOD_SUCCESS: str = "mod_success"
    MSG_BANNED: str = "msg_banned"
    MSG_BAD_CHARACTERS: str = "msg_bad_characters"
    MSG_CHANNEL_BLOCKED: str = "msg_channel_blocked"
    MSG_CHANNEL_SUSPENDED: str = "msg_channel_suspended"
    MSG_DUPLICATE: str = "msg_duplicate"
    MSG_EMOTEONLY: str = "msg_emoteonly"
    MSG_FACEBOOK: str = "msg_facebook"
    MSG_FOLLOWERSONLY: str = "msg_followersonly"
    MSG_FOLLOWERSONLY_FOLLOWED: str = "msg_followersonly_followed"
    MSG_FOLLOWERSONLY_ZERO: str = "msg_followersonly_zero"
    MSG_R9K: str = "msg_r9k"
    MSG_RATELIMIT: str = "msg_ratelimit"
    MSG_REJECTED: str = "msg_rejected"
    MSG_REJECTED_MANDATORY: str = "msg_rejected_mandatory"
    MSG_ROOM_NOT_FOUND: str = "msg_room_not_found"
    MSG_SLOWMODE: str = "msg_slowmode"
    MSG_SUBSONLY: str = "msg_subsonly"
    MSG_SUSPENDED: str = "msg_suspended"
    MSG_TIMEDOUT: str = "msg_timedout"
    MSG_VERIFIED_EMAIL: str = "msg_verified_email"
    NO_HELP: str = "no_help"
    NO_MODS: str = "no_mods"
    NOT_HOSTING: str = "not_hosting"
    NO_PERMISSION: str = "no_permission"
    R9K_OFF: str = "r9k_off"
    R9K_ON: str = "r9k_on"
    RAID_ERROR_ALREADY_RAIDING: str = "raid_error_already_raiding"
    RAID_ERROR_FORBIDDEN: str = "raid_error_forbidden"
    RAID_ERROR_SELF: str = "raid_error_self"
    RAID_ERROR_TOO_MANY_VIEWERS: str = "raid_error_too_many_viewers"
    RAID_ERROR_UNEXPECTED: str = "raid_error_unexpected"
    RAID_NOTICE_MATURE: str = "raid_notice_mature"
    RAID_NOTICE_RESTRICTED_CHAT: str = "raid_notice_restricted_chat"
    ROOM_MODS: str = "room_mods"
    SLOW_OFF: str = "slow_off"
    SLOW_ON: str = "slow_on"
    SUBS_OFF: str = "subs_off"
    SUBS_ON: str = "subs_on"
    TIMEOUT_NO_TIMEOUT: str = "timeout_no_timeout"
    TIMEOUT_SUCCESS: str = "timeout_success"
    TOS_BAN: str = "tos_ban"
    TURBO_ONLY_COLOR: str = "turbo_only_color"
    UNBAN_SUCCESS: str = "unban_success"
    UNMOD_SUCCESS: str = "unmod_success"
    UNRAID_ERROR_NO_ACTIVE_RAID: str = "unraid_error_no_active_raid"
    UNRAID_ERROR_UNEXPECTED: str = "unraid_error_unexpected"
    UNRAID_SUCCESS: str = "unraid_success"
    UNRECOGNIZED_CMD: str = "unrecognized_cmd"
    UNSUPPORTED_CHATROOMS_CMD: str = "unsupported_chatrooms_cmd"
    UNTIMEOUT_BANNED: str = "untimeout_banned"
    UNTIMEOUT_SUCCESS: str = "untimeout_success"
    USAGE_BAN: str = "usage_ban"
    USAGE_CLEAR: str = "usage_clear"
    USAGE_COLOR: str = "usage_color"
    USAGE_COMMERCIAL: str = "usage_commercial"
    USAGE_DISCONNECT: str = "usage_disconnect"
    USAGE_EMOTE_ONLY_OFF: str = "usage_emote_only_off"
    USAGE_EMOTE_ONLY_ON: str = "usage_emote_only_on"
    USAGE_FOLLOWERS_OFF: str = "usage_followers_off"
    USAGE_FOLLOWERS_ON: str = "usage_followers_on"
    USAGE_HELP: str = "usage_help"
    USAGE_HOST: str = "usage_host"
    USAGE_MARKER: str = "usage_marker"
    USAGE_ME: str = "usage_me"
    USAGE_MOD: str = "usage_mod"
    USAGE_MODS: str = "usage_mods"
    USAGE_R9K_OFF: str = "usage_r9k_off"
    USAGE_R9K_ON: str = "usage_r9k_on"
    USAGE_RAID: str = "usage_raid"
    USAGE_SLOW_OFF: str = "usage_slow_off"
    USAGE_SLOW_ON: str = "usage_slow_on"
    USAGE_SUBS_OFF: str = "usage_subs_off"
    USAGE_SUBS_ON: str = "usage_subs_on"
    USAGE_TIMEOUT: str = "usage_timeout"
    USAGE_UNBAN: str = "usage_unban"
    USAGE_UNHOST: str = "usage_unhost"
    USAGE_UNMOD: str = "usage_unmod"
    USAGE_UNRAID: str = "usage_unraid"
    USAGE_UNTIMEOUT: str = "usage_untimeout"
    WHISPER_BANNED: str = "whisper_banned"
    WHISPER_BANNED_RECIPIENT: str = "whisper_banned_recipient"
    WHISPER_INVALID_ARGS: str = "whisper_invalid_args"
    WHISPER_INVALID_LOGIN: str = "whisper_invalid_login"
    WHISPER_INVALID_SELF: str = "whisper_invalid_self"
    WHISPER_LIMIT_PER_MIN: str = "whisper_limit_per_min"
    WHISPER_LIMIT_PER_SEC: str = "whisper_limit_per_sec"
    WHISPER_RESTRICTED: str = "whisper_restricted"
    WHISPER_RESTRICTED_RECIPIENT: str = "whisper_restricted_recipient"

@IDEHelper
@dataclass(frozen=True)
class _CLEARCHAT(str):
    """
    _CLEARCHAT [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE = "CLEARCHAT"
    BAN_DURATION: str = "ban-duration"

@IDEHelper
@dataclass(frozen=True)
class _CLEARMSG(str):
    """
    _CLEARMSG [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE: str = "CLEARMSG"
    LOGIN: str = "login"
    MESSAGE: str = "message"
    TARGET_MSG_ID: str = "target-msg-id"

@IDEHelper   
@dataclass(frozen=True)
class _GLOBALUSERSTATE(str):
    """
    _GLOBALUSERSTATE [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE: str = "GLOBALUSERSTATE"
    ON_SET:str = "GLOBALUSERSTATESET"
    BADGE_INFO: str = 'badge-info'
    BADGES: str = 'badges'
    COLOR: str = 'color'
    DISPLAY_NAME: str = 'display-name'
    EMOTE_SETS: str = 'emote-sets'
    TURBO: str = 'turbo'
    USER_ID: str = 'user-id'
    USER_TYPE: str = 'user-type'

@IDEHelper
@dataclass(frozen=True)
class _PRIVMSG(str):
    """
    _PRIVMSG [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE: str = "PRIVMSG"
    BADGE_INFO: str = 'badge-info'
    BADGES: str = 'badges'
    BITS: str = 'bits'
    COLOR: str = 'color'
    DISPLAY_NAME: str = 'display-name'
    EMOTES: str = 'emotes'
    ID: str = 'id'
    MOD: str = 'mod'
    ROOM_ID: str = 'room-id'
    EMOTE_SETS: str = 'emote-sets'
    SUBSCRIBER: str = 'subscriber'
    TMI_SENT_TS: str = 'tmi-sent-ts'
    TURBO: str = 'turbo'
    USER_ID: str = 'user-id'
    USER_TYPE: str = 'user-type'  

@IDEHelper
@dataclass(frozen=True)
class _ROOMSTATE(str):
    """
    _ROOMSTATE [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE: str = "ROOMSTATE"
    ROOM_ID = "room-id"
    EMOTE_ONLY: str = "emote-only"
    EMOTE_ONLY_ON: str = "emote-only-on"
    EMOTE_ONLY_OFF: str = "emote-only-off"
    FOLLOWERS_ONLY: str = "followers-only"
    FOLLOWERS_ONLY_ON: str = "followers-only-on"
    FOLLOWERS_ONLY_OFF: str = "followers-only-off"
    R9K: str = "r9k"
    R9K_ON: str = "r9k-on"
    R9K_OFF: str = "r9k-off"
    SLOW: str = "slow"
    SLOW_ON: str = "slow-on"
    SLOW_OFF: str = "slow-off"
    SUBS_ONLY: str = "subs-only"
    SUBS_ONLY_ON: str = "subs-only-on"
    SUBS_ONLY_OFF: str = "subs-only-off"

@IDEHelper
@dataclass(frozen=True)
class _USERNOTICE(str):
    """
    _USERNOTICE [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE: str = "USERNOTICE"
    BADGE_INFO: str = 'badge-info'
    BADGES: str = 'badges'
    BITS: str = 'bits'
    COLOR: str = 'color'
    DISPLAY_NAME: str = 'display-name'
    EMOTES: str = 'emotes'
    ID: str = 'id'
    MOD: str = 'mod'
    ROOM_ID: str = 'room-id'
    EMOTE_SETS: str = 'emote-sets'
    SUBSCRIBER: str = 'subscriber'
    TMI_SENT_TS: str = 'tmi-sent-ts'
    TURBO: str = 'turbo'
    USER_ID: str = 'user-id'
    USER_TYPE: str = 'user-type'
    MSG_PARAM_CUMULATIVE_MONTHS: str = "msg-param-cumulative-months"
    MSG_PARAM_DISPLAYNAME: str = "msg-param-displayName"
    MSG_PARAM_LOGIN: str = "msg-param-login"
    MSG_PARAM_MONTHS: str = "msg-param-months"
    MSG_PARAM_PROMO_GIFT_TOTAL: str = "msg-param-promo-gift-total"
    MSG_PARAM_PROMO_NAME: str = "msg-param-promo-name"
    MSG_PARAM_RECIPIENT_DISPLAY_NAME: str = "msg-param-recipient-display-name"
    MSG_PARAM_RECIPIENT_ID: str = "msg-param-recipient-id"
    MSG_PARAM_RECIPIENT_USER_NAME: str = "msg-param-recipient-user-name"
    MSG_PARAM_SENDER_LOGIN: str = "msg-param-sender-login"
    MSG_PARAM_SENDER_NAME: str = "msg-param-sender-name"
    MSG_PARAM_SHOULD_SHARE_STREAK: str = "msg-param-should-share-streak"
    MSG_PARAM_STREAK_MONTHS: str = "msg-param-streak-months"
    MSG_PARAM_SUB_PLAN: str = "msg-param-sub-plan"
    MSG_PARAM_SUB_PLAN_NAME: str = "msg-param-sub-plan-name"
    MSG_PARAM_VIEWERCOUNT: str = "msg-param-viewerCount"
    MSG_PARAM_RITUAL_NAME: str = "msg-param-ritual-name"
    MSG_PARAM_THRESHOLD: str = "msg-param-threshold"

@IDEHelper
@dataclass(frozen=True)
class _USERSTATE(str):
    """
    _USERSTATE [summary]
    
    :param str: [description]
    :type str: [type]
    """
    _VALUE: str = "USERSTATE"
    BADGE_INFO: str = "badge-info"
    BADGES: str = "badges"
    COLOR: str = "color"
    DISPLAY_NAME: str = "display-name"
    EMOTE_SETS: str = "emote-sets"
    MOD: str = "mod"
    SUBSCRIBER: str = "subscriber"
    TURBO: str = "turbo"
    USER_TYPE: str = "user-type"
    BADGE_INFO: str = "badge-info"
    BADGES: str = "badges"
    COLOR: str = "color"
    DISPLAY_NAME: str = "display-name"
    EMOTE_SETS: str = "emote-sets"
    MOD: str = "mod"
    SUBSCRIBER: str = "subscriber"
    TURBO: str = "turbo"
    USER_TYPE: str = "user-type"

@dataclass(frozen=True)
class COMMANDS:
    """
     [summary]
    """
    LOGIN_UNSUCCESSFUL: str = "LOGIN_UNSUCCESSFUL"
    MESSAGE: str = "PRIVMSG"
    JOIN: str = "JOIN"
    RECEIVED: str = "RECEIVED"
    CONNECTED: str = "372"
    ERROR: str = "ERROR"
    DISCONNECTED: str = "DISCONNECTED"
    USERNAME: str = "001"
    NAMES: str = "353"
    WHISPER: str = "WHISPER"
    PART: str = "PART"
    TMI_TWITCH_TV: str = "tmi.twitch.tv"
    NOTICE: str = "NOTICE"
    RECONNECT: str  = "RECONNECT" 
    HOSTTARGET: str = "HOSTTARGET"
    GLOBALUSERSTATE: _GLOBALUSERSTATE = _GLOBALUSERSTATE()
    CLEARCHAT: _CLEARCHAT = _CLEARCHAT()
    CLEARMSG: _CLEARMSG = _CLEARMSG()
    USERNOTICE: _USERNOTICE = _USERNOTICE()
    USERSTATE: _USERSTATE =  _USERSTATE()
    ROOMSTATE: _ROOMSTATE = _ROOMSTATE()
    MESSAGEIDS: _MESSAGEIDS = _MESSAGEIDS()

class MessageHandler():
    """ MessageHandler - Handles twitch IRC messages and emits events based on Commands and msgid tags """
    def __init__(self):
        self.COMMANDS: COMMANDS = COMMANDS()
        self.LOGIN_FAILURE_RESAONS: list = (":tmi.twitch.tv NOTICE * :Login unsuccessful", \
                                            ":tmi.twitch.tv NOTICE * :Login authentication failed", \
                                            ":tmi.twitch.tv NOTICE * :Error logging in", \
                                            ":tmi.twitch.tv NOTICE * :Invalid NICK" \
                                            )

    def handleMessage(self, IrcMessage: str)->tuple:
        """ MessageHandler.handleMessage - breaks down data string from irc server returns tuple (event: str, message: Message) or
            returns tuple of (None, None)
        
        :param IrcMessage: a irc recieved message for server
        :type IrcMessage: str
        :return: a tuple with event string and Message data type populasted with all parsed message data
        :rtype: tuple
        """
        eventTuple = None, None
        self._parseMesaage(IrcMessage)
        if self._isMessage(self.message):
            self._populateMessageValues()
            eventTuple = self._getEventTuple()        
        return eventTuple

    def _parseMesaage(self, IrcMessage):
        self.message = self._parse(IrcMessage)
        if self._isMessage(self.message):
            self._parseMessageEmotes()
            self._parseMessageTags()
            self._transformIRCv3Tags()

    def _parseMessageEmotes(self):
        if ("emotes" in self.message.tags and isinstance(self.message.tags.get("emotes"), str)):
            emotes: dict = {}
            emoticons = self.message.tags.get("emotes").split("/")
            for emoticon in emoticons:
                key, value = emoticon.split(":")
                if value is not None:
                    emotes[key] = value.split(",")
            self.message.tags["emotes"] = emotes

    def _parseMessageTags(self):
         if ("badges" in self.message.tags and isinstance(self.message.tags.get("badges"), str)):
            badges = self.message.tags.get("badges").split(",")
            self.message.tags["badges"]: dict = {}
            for badge in badges:
                key, value = badge.split("/")
                if value is not None:
                    self.message.tags["badges"][key] = value
                
    def _getEventTuple(self)->tuple:
        # Handle message with prefix "tmi.twitch.tv"
        if self._isInvalidLogin(self.message.raw):
            return self._getInvalidLoginEventTuple()
        if self._isTMI(self.message.prefix):
           return self._getTmiEventTuple()
        elif self._isJTV(self.message.prefix): 
            return self._getJtvEventTuple()
        elif self._isValidCommand(self.message.command):
            return self._getCommandEventTuple()
            
        return None, None # invalid message

    def _getTmiEventTuple(self)->tuple:
        if self.message.command == self.COMMANDS.NOTICE:
            return self._getNoticeEventTuple()
        else:
            return self.message.command, self.message

    def _getNoticeEventTuple(self)->tuple:
        if self._isValidMsgId(self.message.id):
            return self.COMMANDS.NOTICE, self.message
        
    def _getInvalidLoginEventTuple(self)->tuple:
        return self.COMMANDS.LOGIN_UNSUCCESSFUL, self.message.raw.replace(":tmi.twitch.tv NOTICE * :",'')

    def _getJtvEventTuple(self)->tuple:
        return self.message.command, self.message

    def _getCommandEventTuple(self)->tuple:
        return self.message.command, self.message

    def _populateMessageValues(self):
        self._populateMessageChannel() 
        self._populateMessageText() 
        self._populateMessageUsername()
        self._populateMessageId()

    def _populateMessageChannel(self):
        self.message.channel: str = self.message.params[0] if len(self.message.params) > 0 else None
        
    def _populateMessageText(self):
        self.message.text: str = self.message.params[1] if len(self.message.params) > 1 else None

    def _populateMessageId(self):
        self.message.id: str = self.message.tags.get("msg-id")

    def _populateMessageUsername(self):
        self.message.username: str = self.message.tags.get("display-name")

    def _isValidCommand(self,command)->bool:
        return command in self.COMMANDS.__dict__.values()

    def _isValidMsgId(self, msgId)->bool:
        return msgId in self.COMMANDS.MESSAGEIDS.__dict__.values()
    
    def _isInvalidLogin(self, rawMessage)->bool:
        return rawMessage in self.LOGIN_FAILURE_RESAONS

    def _isJTV(self, prefix)->bool:
        return prefix == "jtv"
    
    def _isTMI(self, prefix)->bool:
        return prefix == self.COMMANDS.TMI_TWITCH_TV
    
    @staticmethod
    def _isMessage(message)->bool:
        return isinstance(message, Message) 

    def _transformIRCv3Tags(self):
        """ MessageHandler._TransformIRCv3Tags reformats message tags
        
        :param message: message object
        :type message: Message
        :return: message with updated tags
        :rtype: Message
        """

        if self.message.tags:
            for key in self.message.tags:
                if key not in ("emote-sets", "ban-duration", "bits"):
                    if isinstance(self.message.tags[key], bool):
                        self.message.tags[key] = None
                    elif self.message.tags[key] in ('0', '1'):
                        self.message.tags[key] = bool(int(self.message.tags[key]))

    @staticmethod
    def _badges(tags: dict)->dict:
        """ MessageHandler._badges - Parse tags['badges'] from str to dict and update tags['badges']
        
            :param tags: tags from parsed IRC message
            :type event: dict

            :return: tags
            :rtype: dict
        """

        if ("badges" in tags and isinstance(tags.get("badges"), str)):
            badges = tags.get("badges").split(",")
            tags["badges"]: dict = {}
            for badge in badges:
                key, value = badge.split("/")
                if value is None:
                    return tags
                tags["badges"][key] = value
        return tags
        
    @staticmethod
    def _emotes(tags: dict)->dict:
        """ MessageHandler._emotes - Parse tags['emotes'] from str to list and update tags['emotes']
        
            :param tags: tags from parsed IRC message
            :type event: dict

            :return: tags
            :rtype: dict
        """
        if ("emotes" in tags and isinstance(tags.get("emotes"), str)):
            emotes: dict = {}
            emoticons = tags.get("emotes").split("/")
            for emoticon in emoticons:
                key, value = emoticon.split(":")
                if value is None:
                    return tags
                emotes[key] = value.split(",")
            tags["emotes"] = emotes
        return tags

    @staticmethod
    def _parse(data: str)->Message:
        """ MessageHandler._parse - Parses IRC messages to Message type
        
            :param data: string from IRC server
            :type event: str
            :return: message
            :rtype: Message
        """
        message = Message()
        if not isinstance(data, str):
            raise TypeError("MessageHandler._parse requires input of type str")
        message.raw = data      
        position: int = 0
        nextspace: int = 0

        if len(data) < 1:
            return None

        if data.startswith("@"): 
            nextspace = data.find(" ")

            if nextspace == -1:
                return None  # invalid message form

            tags = data[1:nextspace].split(";")

            for tag in tags:
                key, value = tag.split("=")
                message.tags[key] = value or True

            position = nextspace + 1

        while data[position] == " ":
            position += 1

        if data[position] == ":":
            nextspace = data.find(" ", position)

            if nextspace == -1: 
                return None # invalid message form

            message.prefix = data[position + 1:nextspace]
            position = nextspace + 1

            while data[position] == " ":
                position += 1

        nextspace = data.find(" ", position)

        if nextspace == -1:
            if len(data) > position:
                message.command = data[position:]
                return message

            return None # invalid message form

        message.command = data[position:nextspace]

        position = nextspace + 1

        while data[position] == " ":
            position += 1

        dataLen = len(data)

        while position < dataLen:
            nextspace = data.find(" ", position)

            if data[position] == ":": 
                message.params.append(data[position + 1:])
                break

            if nextspace != -1:
                message.params.append(data[position:nextspace])
                position = nextspace + 1

                while data[position] == " ":
                    position += 1
                continue

            if nextspace == -1:
                message.params.append(data[position:])
                break

        return message