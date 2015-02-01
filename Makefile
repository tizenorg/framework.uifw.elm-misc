prefix ?= /usr
datadir ?= $(prefix)/share
sysconfdir ?= /etc

ELM_PROFILE ?= mobile
PROFILE_DIR = $(DESTDIR)/$(sysconfdir)/profile.d/
CONFIG_DIR = $(DESTDIR)/$(datadir)/elementary/config/$(ELM_PROFILE)

INSTALL = install -c
EET_EET = eet

all:
	for t in $(TARGET); do \
		for s in $(SIZE); do \
			cd $$t/$$s/profile.d && \
				echo "export ELM_PROFILE="\"$(ELM_PROFILE)\" >> elm.sh ; \
				if [ $(EFL_ABORT_ENABLE) = "on" ]; then \
					echo "export EINA_LOG_ABORT=1" >> eina.sh ; \
					echo "export EINA_LOG_ABORT_LEVEL=1" >> eina.sh ; \
				fi ; \
			cd - ;\
			cd $$t/$$s/config && \
				$(EET_EET) -e base.cfg config base.src 1 ; \
				$(EET_EET) -e color.cfg config color.src 1 ; \
				$(EET_EET) -e font.cfg config font.src 1 ; \
			cd - ; \
		done \
	done

clean:
	for t in $(TARGET); do \
		for s in $(SIZE); do \
			cd $$t/$$s/config && \
			rm -rf *.cfg
			cd - ; \
		done \
	done

install:
	for t in $(TARGET); do \
		for s in $(SIZE); do \
			cd $$t/$$s && \
				mkdir -p $(PROFILE_DIR) $(CONFIG_DIR) && \
				$(INSTALL) profile.d/*.sh $(PROFILE_DIR) && \
				$(INSTALL) config/*.cfg $(CONFIG_DIR) && \
				$(INSTALL) config/profile.desktop $(CONFIG_DIR) && \
				$(INSTALL) config/icon.png $(CONFIG_DIR) ; \
			cd - ; \
		done \
	done
