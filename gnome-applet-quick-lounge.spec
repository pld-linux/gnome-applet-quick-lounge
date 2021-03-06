Summary:	Organize your preferred applications on the GNOME Panel
Summary(pl.UTF-8):	Umieszcza ulubione aplikacje użytkownika na panelu GNOME
Name:		gnome-applet-quick-lounge
Version:	2.14.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/quick-lounge-applet/2.14/quick-lounge-applet-%{version}.tar.gz
# Source0-md5:	ab78149818931a4cba03e59a675c151f
URL:		http://quick-lounge.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.12.0-2
BuildRequires:	gnome-desktop-devel >= 2.12.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-menus-devel >= 2.12.0
BuildRequires:	gnome-panel-devel >= 2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.12.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Organize your preferred applications on the GNOME Panel.

%description -l pl.UTF-8
Umieszcza ulubione aplikacje użytkownika na panelu GNOME.

%prep
%setup -q -n quick-lounge-applet-%{version}

%build
cp -f /usr/share/automake/config.sub .
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_datadir}/locale

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang quick-lounge-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install quick-lounge.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall quick-lounge.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f quick-lounge-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/quick-lounge-applet
%attr(755,root,root) %{_libdir}/quick-lounge-applet
%{_libdir}/bonobo/servers/*.server
%{_iconsdir}/hicolor/*/apps/*.png
%{_sysconfdir}/gconf/schemas/quick-lounge.schemas
