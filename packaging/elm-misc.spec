Name:       elm-misc
Summary:    Elementary config files
Version:    0.1.32
Release:    1
Group:      TO_BE/FILLED_IN
License:    APLv2
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
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/LICENSE %{buildroot}/usr/share/license/%{name}



%files
%defattr(-,root,root,-)
/etc/profile.d/*
/usr/share/license/%{name}
%manifest %{name}.manifest
