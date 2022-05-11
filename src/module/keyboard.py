def keyboard():
    password_entry = loginwindow.password
    vvbox=Gtk.Box()
    vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    vboxb=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    buttons=" 1234567890?{[«\nqwertyuıopğü/:\nasdfghjklşi(€\n<zxcvbnmöç.+@¶"
    buttonsb=" !\"^$%&'#|=*}]»\nQWERTYUIOPĞÜ\\;\nASDFGHJKLŞİ)¢\n>ZXCVBNMÖÇ,-₺_"

    
    def del_event(widget):
        password_entry.set_text(password_entry.get_text()[:-1])
    def key_event(widget):
        password_entry.set_text(password_entry.get_text()+widget.get_label())
    num=0
    for i in buttons.split("\n"):
        box=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.set_homogeneous(True)
        vbox.add(box)
        num=num+1
        if num == 3:
            def chg_event(widget):
                vboxb.show_all()
                vbox.hide()
            chg=Gtk.Button("⇪")
            chg.connect("pressed",chg_event)
            box.add(chg)
        for j in i:
            key=Gtk.Button(j)
            key.connect("pressed",key_event)
            box.add(key)
        if num == 3:
            delbut=Gtk.Button("⌫")
            delbut.connect("pressed",del_event)
            box.add(delbut)
            
    num=0
    for i in buttonsb.split("\n"):
        box=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        vboxb.add(box)
        box.set_homogeneous(True)
        num=num+1
        if num == 3:
            def chgb_event(widget):
                vbox.show_all()
                vboxb.hide()
            chgb=Gtk.Button("⇧")
            chgb.connect("pressed",chgb_event)
            box.add(chgb)
        for j in i:
            key=Gtk.Button(j)
            key.connect("pressed",key_event)
            box.add(key)
        if num == 3:
            delbut=Gtk.Button("⌫")
            delbut.connect("pressed",del_event)
            box.add(delbut)
    vvbox.add(vbox)
    vvbox.add(vboxb)
    vvbox.show_all()
    vboxb.hide()
    return vvbox

def module_init():
    box = loginwindow.builder.get_object("keyboard_box")
    box.add(keyboard())