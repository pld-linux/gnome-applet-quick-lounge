Summary:	Organize your preferred applications on the GNOME Panel
Summary(pl):	Umieszcza ulubione aplikacje u¿ytkownika na panelu GNOME
Name:		gnome-applet-quick-lounge
Version:	2.0.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/quick-lounge-applet/2.0/quick-lounge-applet-%{version}.tar.bz2
# Source0-md5:	b3791f2a67dcb9d9475479b5aab6d424
URL:		http://quick-lounge.sourceforge.net/
BuildRequires:	gnome-desktop-devel >= 2.1.0
BuildRequires:	gnome-panel-devel >= 2.2.0
Buildrequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.1.0
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Organize your preferred applications on the GNOME Panel.

%description -l pl
Umieszcza ulubione aplikacje u¿ytkownika na panelu GNOME.

%prep
%setup -q -n quick-lounge-applet-%{version}

%build
%configure \
	--disable-schemas-install \
	--disable-static
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang quick-lounge-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f quick-lounge-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%config %{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/quick-lounge
%{_pixmapsdir}/*.png
