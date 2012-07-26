#sbs-git:slp/pkgs/e/elm-misc elm-misc 0.1 9e25eb4b63eed4f5a01bd45518c6226f768292ca
Name:       elm-misc
Summary:    Elementary config files
Version:    0.1.30
Release:    1
Group:      TO_BE/FILLED_IN
License:    LGPLv2.1
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz


%description
Elementary configuration files


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
%__cp etc/profile.d/* %{buildroot}%{_sysconfdir}/profile.d/


%post
chown root:root /etc/profile.d/elm.sh
chown root:root /etc/profile.d/evas.sh


%files
%defattr(-,root,root,-)
/etc/profile.d/*


