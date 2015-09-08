Name:       elm-misc
Summary:    Elementary config files
Version:    0.1.142
Release:    1
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
BuildRequires: model-build-features
BuildRequires: eet-bin

%description
Elementary configuration files

%prep
%setup -q

%build
%if "%{?tizen_profile_name}" == "wearable"
    %if "%{?model_build_feature_formfactor}" == "circle"
       export ELM_PROFILE=wearable
       export TARGET=2.3-wearable-circle
       export SIZE=c1
    %else
       export ELM_PROFILE=wearable
       export TARGET=2.3-wearable
       export SIZE=HVGA
	%endif
%else
    export ELM_PROFILE=mobile
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif
export EFL_ABORT_ENABLE=off

make

%install
%if "%{?tizen_profile_name}" == "wearable"
    %if "%{?model_build_feature_formfactor}" == "circle"
       export ELM_PROFILE=wearable
       export TARGET=2.3-wearable-circle
       export SIZE=c1
    %else
       export ELM_PROFILE=wearable
       export TARGET=2.3-wearable
       export SIZE=HVGA
	%endif
%else
    export ELM_PROFILE=mobile
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif
export EFL_ABORT_ENABLE=off

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
%{_datadir}/themes/*
%{_datadir}/elementary/config/*
%{_datadir}/license/%{name}
%manifest %{name}.manifest
