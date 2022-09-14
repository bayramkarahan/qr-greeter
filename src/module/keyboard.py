def keyboard():
    password_entry = loginwindow.password
    vvbox=Gtk.Box()
    vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    vboxb=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    #buttons=" 1234567890?\nfgğıodrnhpqw\nuieaütkmlyşx\n<jövcçzsb.,\n{[«/:(-_+@"
    #buttonsb=" !\"^$%&'#|=*\nFGĞIODRNHPQW\nUİEAÜTKMLYŞX\n>JÖVCÇZSB:;\n}]»\\;)¢₺€¶"
     buttons=" 1234567890?\nqwertyuıopğü\nasdfghjklşi\n<<zxcvbnmöç.,\n{[«/:(-_+@"
     buttonsb=" !\"^$%&'#|=*\nQWERTYUIOPĞÜ\nASDFGHJKLŞİ\n>ZXCVBNMÖÇ:;\n}]»\\;)¢₺€¶"



    def del_event(widget):
        password_entry.set_text(password_entry.get_text()[:-1])
    def clr_event(widget):
        password_entry.set_text("")
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
            chg=Gtk.Button(label="⇪")
            chg.connect("pressed",chg_event)
            box.add(chg)
        for j in i:
            key=Gtk.Button(label=j)
            key.connect("pressed",key_event)
            box.add(key)
        if num == 3:
            delbut=Gtk.Button(label="⌫")
            delbut.connect("pressed",del_event)
            box.add(delbut)
        if num == 5:
            clrbut=Gtk.Button(label="🗑")
            clrbut.connect("pressed",clr_event)
            box.add(clrbut)
            entbut=Gtk.Button(label="enter")
            entbut.connect("clicked",loginwindow.login_event)
            box.add(entbut)

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
            chgb=Gtk.Button(label="⇧")
            chgb.connect("pressed",chgb_event)
            box.add(chgb)
        for j in i:
            key=Gtk.Button(label=j)
            key.connect("pressed",key_event)
            box.add(key)
        if num == 3:
            delbut=Gtk.Button(label="⌫")
            delbut.connect("pressed",del_event)
            box.add(delbut)
        if num == 5:
            clrbut=Gtk.Button(label="🗑")
            clrbut.connect("pressed",clr_event)
            box.add(clrbut)
            entbut=Gtk.Button(label="enter")
            entbut.connect("clicked",loginwindow.login_event)
            box.add(entbut)

    vvbox.add(vbox)
    vvbox.add(vboxb)
    vvbox.show_all()
    vboxb.hide()
    return vvbox

def module_init():
    box = loginwindow.builder.get_object("keyboard_box")
    box.add(keyboard())
