Summary:	Organize your preferred applications on the GNOME Panel
Summary(pl):	Umieszcza ulubione aplikacje u¿ytkownika na panelu GNOME
Name:		gnome-applet-quick-lounge
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/quick-lounge/quick-lounge-applet-%{version}.tar.gz
URL:		http://quick-lounge.sourceforge.net/
BuildRequires:	gnome-panel-devel
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
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

%find_lang quick-lounge-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
GCONF_CONFIG_SOURCE=`%{_bindir}/gconftool-2 --get-default-source` %{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/quick-lounge.schemas

%files -f quick-lounge-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%config %{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_libdir}/lib*.so*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/quick-lounge
