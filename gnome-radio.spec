Name:           gnome-radio
Version:        14.0.0
Release:        1
Summary:        GNOME Radio 3 for GNOME 42
License:        GPLv3+
URL:            https://people.gnome.org/~ole/%{name}
Source:         https://download.gnome.org/sources/gnome-radio/14.0/gnome-radio-%{version}.tar.xz

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
Requires:       gstreamer1.0-plugins-base
Requires:       gstreamer1.0-plugins-ugly
Requires:       geocode-glib
Requires:       gtk+3.0
Requires:       geoclue

%description
GNOME Radio 3 is a Free Software program that allows you easily
listen to National Public Radio (NPR) broadcasts under GNOME 42.

GNOME Radio 3 is developed on the GNOME 42 desktop platform and
it requires GTK+ 3.0, Clutter and GStreamer 1.0 for playback.

Enjoy National Public Radio (NPR) broadcasts under GNOME 42.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-schemas
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/gnome-radio.svg
