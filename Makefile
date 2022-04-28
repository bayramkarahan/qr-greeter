build:
	: please run make install
install: clean
	mkdir -p $(DESTDIR)/usr/share/qr-greeter/
	mkdir -p $(DESTDIR)/usr/share/xgreeters/
	mkdir -p $(DESTDIR)/usr/bin
	mkdir -p $(DESTDIR)/usr/share/lightdm/lightdm.conf.d/
	cp -prfv ./src/* $(DESTDIR)/usr/share/qr-greeter/
	chmod +x $(DESTDIR)/usr/share/qr-greeter/*
	install src/data/lightdm.conf $(DESTDIR)/usr/share/lightdm/lightdm.conf.d/99-qr-greeter.conf
	ln -s ../qr-greeter/data/greeter.desktop $(DESTDIR)/usr/share/xgreeters/qr.desktop || true
	ln -s ../share/qr-greeter/main.py $(DESTDIR)/usr/bin/qr-greeter || true

clean:
	find -iname "__pycache__" | xargs rm -rfv
	find -iname "*.ui~" | xargs rm -rfv
