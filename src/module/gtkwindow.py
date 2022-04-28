class LoginWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("data/main.ui")
        self.window = self.builder.get_object("window")
        self.login = self.builder.get_object("login")
        self.username = self.builder.get_object("username")
        self.password = self.builder.get_object("password")
        self.login.connect("clicked",self.login_event)

    def login_event(self,widget):
        lightdm.username = self.username.get_text()
        lightdm.password = self.password.get_text()
        lightdm.login()


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
