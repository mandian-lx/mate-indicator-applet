%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Panel applet indicator
Name:		mate-indicator-applet
Version:	1.8.0
Release:	1
License:	LGPLv2+ GPLv3
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(indicator-0.4)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
Requires:	mate-panel

%description
A small applet to display information from various applications consistently
in the panel. The indicator applet exposes Ayatana Indicators in the MATE
Panel. Ayatana Indicators are an initiative by Canonical to provide crisp and
clean system and application status indication. They take the form of an icon
and associated menu, displayed (usually) in the desktop panel. Existing
indicators include the Message Menu, Battery Menu and Sound menu.

%prep
%setup -q
%apply_patches
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING
%{_libexecdir}/indicator-applet*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-panel/applets/*.mate-panel-applet
%{_iconsdir}/hicolor/*/*/*

