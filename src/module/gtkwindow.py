from qr import QrWidget

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
        self.builder.get_object("keyboard_show").connect("clicked",self._keyboard_popup)
        self.builder.get_object("main_button").connect("clicked",self._main_button_event)
        self.builder.get_object("qr_button").connect("clicked",self._qr_button_event)
        self.fill_userlist()
        self.apply_css()
        self.qr = QrWidget()
        self.builder.get_object("qrbox").add(self.qr)
        self.builder.get_object("stack").set_visible_child_name("qr")
        self.builder.get_object("refresh").connect("clicked",self.qr.refresh)

    def _main_button_event(self,widget):
        self.builder.get_object("stack").set_visible_child_name("main")

    def _qr_button_event(self,widget):
        self.builder.get_object("stack").set_visible_child_name("qr")

    def apply_css(self):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        css = """
            * {
                font-size: 32px;
            }
            #qrbox {
                background: red;
            }

        """
        provider.load_from_data(bytes(css,"UTF-8"))

    def fill_userlist(self):
        def set_username(widget):
            self.builder.get_object("username").set_text(widget.get_label())
        ulist = []
        for name in lightdm.get_user_list():
            if name.get_name() in ulist:
                continue
            ulist.append(name.get_name())
            if name.get_name().endswith("-qr"):
                continue
            user = Gtk.Button()
            user.set_label(name.get_name())
            user.connect("clicked",set_username)
            self.builder.get_object("userlist").pack_start(user,0,True,True)
            user.show_all()
        if os.path.exists("/var/lib/lightdm/last-username"):
            f = open("/var/lib/lightdm/last-username","r")
            user = f.read()
            if user.endswith("-qr"):
                user = user[:-3]
            self.builder.get_object("username").set_text(user)

    def login_event(self,widget):
        lightdm.username = self.username.get_text()
        lightdm.password = self.password.get_text()
        lightdm.login()


    def _userlist_popever_popup(self,widget):
        self.builder.get_object("userlist_popever").popup()

    def _keyboard_popup(self,widget):
        self.builder.get_object("keyboard").popup()

def module_init():
    global loginwindow
    global screen
    loginwindow = LoginWindow()
    lightdm.msg_handler = log
    screen = loginwindow.window.get_screen()
    #cursor = Gdk.Cursor(Gdk.CursorType.LEFT_PTR)
    cursor = Gdk.Cursor(Gdk.CursorType.BLANK_CURSOR)
    loginwindow.window.get_root_window().set_cursor(cursor)
    loginwindow.window.resize(screen.get_width(), screen.get_height())
    loginwindow.window.set_size_request(screen.get_width(), screen.get_height())
    loginwindow.window.move(0,0)
    loginwindow.window.show_all()
