Summary:	Organize your preferred applications on the GNOME Panel
Summary(pl):	Umieszcza ulubione aplikacje u¿ytkownika na panelu GNOME
Name:		gnome-applet-quick-lounge
Version:	2.2.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/quick-lounge-applet/2.2/quick-lounge-applet-%{version}.tar.bz2
# Source0-md5:	d28cfa7046c3a5ae74f68e7c8b9c321e
Patch0:		%{name}-locale-names.patch
URL:		http://quick-lounge.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel >= 2.4.0
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
Buildrequires:	scrollkeeper
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Organize your preferred applications on the GNOME Panel.

%description -l pl
Umieszcza ulubione aplikacje u¿ytkownika na panelu GNOME.

%prep
%setup -q -n quick-lounge-applet-%{version}
%patch0 -p1

mv po/{no,nb}.po
rm po/*.gmo

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_datadir}/locale

%find_lang quick-lounge-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f quick-lounge-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%config %{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_libdir}/quick-lounge-applet
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/quick-lounge
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/*
