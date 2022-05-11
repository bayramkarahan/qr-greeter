class LoginWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("data/main.ui")
        self.window = self.builder.get_object("window")
        self.login = self.builder.get_object("login")
        self.username = self.builder.get_object("username")
        self.username_button = self.builder.get_object("username_button")
        self.password = self.builder.get_object("password")
        self.login.connect("clicked",self.login_event)
        self.username_button.connect("clicked",self._userlist_popever_popup)
        self.password.connect("icon-press",self._keyboard_popup)
        self.fill_userlist()

    def fill_userlist(self):
        def set_username(widget):
            self.builder.get_object("username").set_text(widget.get_label())
        for name in lightdm.get_user_list():
            if name.get_name().endswith("-qr"):
                continue
            user = Gtk.Button()
            user.set_label(name.get_name())
            user.connect("clicked",set_username)
            self.builder.get_object("userlist").pack_start(user,0,True,True)
            user.show_all()
        if os.path.exists("/var/lib/lightdm/last-username"):
            f = open("/var/lib/lightdm/last-username","r")
            self.builder.get_object("username").set_text(f.read())

    def login_event(self,widget):
        lightdm.username = self.username.get_text()
        lightdm.password = self.password.get_text()
        lightdm.login()


    def _userlist_popever_popup(self,widget):
        self.builder.get_object("userlist_popever").popup()

    def _keyboard_popup(self,a=None,b=None,c=None):
        self.builder.get_object("keyboard").popup()

def module_init():
    global loginwindow
    global screen
    loginwindow = LoginWindow()
    screen = loginwindow.window.get_screen()
    cursor = Gdk.Cursor(Gdk.CursorType.LEFT_PTR)
    loginwindow.window.get_root_window().set_cursor(cursor)
    loginwindow.window.resize(screen.get_width(), screen.get_height())
    loginwindow.window.set_size_request(screen.get_width(), screen.get_height())
    loginwindow.window.move(0,0)
    loginwindow.window.show_all()
