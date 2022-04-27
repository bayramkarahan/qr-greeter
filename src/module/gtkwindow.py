class LoginWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("data/main.ui")

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
    if not lightdm.is_lockscreen():
        loginwindow.lock_button.hide()
