Name:           metacity
Version:        3.36.1
Release:        1
Summary:        Window Manager for the MATE and GNOME Flashback desktops
License:        GPLv2+
URL:            https://download.gnome.org/sources/metacity/
Source0:        https://download.gnome.org/sources/metacity/3.36/%{name}-%{version}.tar.xz

BuildRequires:  gtk3-devel glib2-devel gsettings-desktop-schemas-devel pango-devel libcanberra-devel
BuildRequires:  startup-notification-devel libXcomposite-devel libXfixes-devel libXrender-devel
BuildRequires:  libXrender-devel libXdamage-devel libXrender-devel libXcursor-devel libgtop2-devel
BuildRequires:  libXinerama-devel libSM-devel libICE-devel libX11-devel desktop-file-utils itstool
BuildRequires:  autoconf, automake, gettext-devel, libtool, gnome-common yelp-tools zenity
BuildRequires: vulkan-devel
BuildRequires: pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires: pkgconfig(gio-2.0) >= 2.44.0
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(libgtop-2.0)

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
%doc AUTHORS 
%license COPYING 
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
* Thu Jul 30 2020 hanhui <hanhui15@huawei.com> - 3.37.1-1
- update to 3.36.1

* Sat Oct 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.30.1-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:change the directory of the license files

* Tue Sep 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.30.1-1
- Package init



