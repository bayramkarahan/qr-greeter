#!/usr/bin/python3
import gi
gi.require_version('LightDM', '1')
from gi.repository import LightDM
import sys, time

class lightdm_class:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.session = ""
        self.greeter = LightDM.Greeter()
        self.msg_handler = None
        self.login_handler = None

        self._pressed = False
        self._responsed = False

        self.greeter.connect ("authentication-complete", self.__authentication_complete_cb)
        self.greeter.connect ("show_prompt", self.__show_prompt_cb)
        self.greeter.connect("show-message", self.__show_message_cb)
        self.greeter.connect_sync()

    def set(username=None,password=None,session=None):
        if username:
            self.username = username
        if password:
            self.password = password
        if username:
            self.session = session

    def login(self,widget=None):
        if self.greeter.get_is_authenticated():
            print("aaa",file=sys.stderr)
            True
        elif not self._responsed and self.greeter.get_in_authentication():
            print("bbb",file=sys.stderr)
            self._responsed = True
            self.greeter.respond(str(self.password))
        elif not self._pressed:
            print("ccc",file=sys.stderr)
            self._pressed = True
            self.greeter.authenticate(self.username)

    def __show_prompt_cb(self, greeter, text, promptType):
        self.login()

    def __show_message_cb(self, greeter, text, message_type=None, **kwargs):
        if self.msg_handler:
            self.msg_handler(text)
        log(msg)

    def __authentication_complete_cb(self,greeter):
        self.login()
        self._pressed = False
        self._responsed = False
        error = ""
        if self.greeter.get_is_authenticated():
            if self.login_handler:
                self.login_handler()
            if self.session not in self.get_session_list() and self.session != "":
                error += "Invalid sesion : {}".format(self.session) + "\n"
            try:
                log("Login success for {}".format(self.username))
                if not self.greeter.start_session_sync(self.session):
                   error += "Failed to start session: {}".format(self.session) + "\n"
            except:
               sys.exit(0)
        else:
            error += "Authentication failed: {}".format(self.username) + "\n"
        if error != "" :
            log(error)
            if self.msg_handler:
                self.msg_handler(error)

    def get_session_list(self):
        sessions = []
        for session in LightDM.get_sessions():
            sessions.append(session.get_key())
        return sessions

    def get_user_list(self):
        return LightDM.UserList.get_instance().get_users()

    def is_lockscreen(self):
        return self.greeter.get_lock_hint()

    def reboot(self, widget=None):
        if LightDM.get_can_restart():
            LightDM.restart()
        else:
            error = "Failed to reboot system"
            log(error)
            if self.msg_handler:
                self.msg_handler(error)

    def shutdown(self, widget=None):
        if LightDM.get_can_shutdown():
            LightDM.shutdown()
        else:
            error = "Failed to shutdown system"
            log(error)
            if self.msg_handler:
                self.msg_handler(error)

lightdm = None
def module_init():
    global lightdm
    lightdm = lightdm_class()
    try:
        lightdm.greeter.authenticate_autologin()
    except:
        pass
