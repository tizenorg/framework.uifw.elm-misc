Name:       elm-misc
Summary:    Elementary config files
Version:    0.1.140
Release:    1
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
BuildRequires: eet-bin

%description
Elementary configuration files

%prep
%setup -q

%build
%if "%{?tizen_profile_name}" == "wearable"
    export ELM_PROFILE=wearable
    export TARGET=2.3-wearable
    export SIZE=HVGA
%elseif "%{?tizen_profile_name}" == "mobile"
    export ELM_PROFILE=mobile
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif

#%if 0%{?tizen_build_binary_release_type_daily}
    export EFL_ABORT_ENABLE=off
#%endif

make

%install
%if "%{?tizen_profile_name}" == "wearable"
    export ELM_PROFILE=wearable
    export TARGET=2.3-wearable
    export SIZE=HVGA
%elseif "%{?tizen_profile_name}" == "mobile"
    export ELM_PROFILE=mobile
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%post
chown root:root /etc/profile.d/ecore.sh
chown root:root /etc/profile.d/edje.sh
chown root:root /etc/profile.d/eina.sh
chown root:root /etc/profile.d/elm.sh
chown root:root /etc/profile.d/evas.sh

%files
%defattr(-,root,root,-)
%{_sysconfdir}/profile.d/*
%{_datadir}/elementary/config/*
%{_datadir}/license/%{name}
%manifest %{name}.manifest
