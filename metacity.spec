Name:           metacity
Version:        3.30.1
Release:        1
Summary:        Window Manager for the MATE and GNOME Flashback desktops
License:        GPLv2+
URL:            https://download.gnome.org/sources/metacity/
Source0:        https://download.gnome.org/sources/metacity/3.30/%{name}-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM --revert unminimize windows with initial IconicState
# https://gitlab.gnome.org/GNOME/metacity/issues/4 
Patch1:         metacity-ggo04.patch

BuildRequires:  gtk3-devel glib2-devel gsettings-desktop-schemas-devel pango-devel libcanberra-devel
BuildRequires:  startup-notification-devel libXcomposite-devel libXfixes-devel libXrender-devel
BuildRequires:  libXrender-devel libXdamage-devel libXrender-devel libXcursor-devel libgtop2-devel
BuildRequires:  libXinerama-devel libSM-devel libICE-devel libX11-devel desktop-file-utils itstool
BuildRequires:  autoconf, automake, gettext-devel, libtool, gnome-common yelp-tools zenity

Requires:       startup-notification gsettings-desktop-schemas zenity
Provides:       firstboot(windowmanager) = metacity

%description
Metacity is a small window manager, using GTK+ to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

%package        devel
Summary:        Development files and Header files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1 
rm -f src/org.gnome.metacity.gschema.valid

%build
CPPFLAGS="$CPPFLAGS -I$RPM_BUILD_ROOT%{_includedir}"
export CPPFLAGS
rm -f configure
(if ! test -x configure; then autoreconf -i -f; fi;
 %configure  --disable-schemas-compile)

make CPPFLAGS="$CPPFLAGS" LIBS="$LIBS" %{?_smp_mflags}

%install
%make_install
%delete_la_and_a

%ldconfig_scriptlets

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING 
%{_bindir}/metacity*
%{_libdir}/libmetacity.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-control-center/keybindings/*
%{_datadir}/locale/*

%files  devel
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/metacity/libmetacity/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmetacity.so

%files  help
%defattr(-,root,root)
%doc HACKING doc/metacity-theme.dtd NEWS rationales.txt README doc/theme-format.txt
%{_mandir}/man1/*.gz
%{_datadir}/metacity/icons/*

%changelog
* Tue Sep 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.30.1-1
- Package init



