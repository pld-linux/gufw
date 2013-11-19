Summary:	A graphical user interface for Ubuntu's Uncomplicated Firewall
Name:		gufw
Version:	13.10.3
Release:	0.1
License:	GPL 3.0
Group:		Networking/Admin
Source0:	https://launchpad.net/gui-ufw/gufw-13.10/13.10/+download/gui-ufw-%{version}.tar.gz
# Source0-md5:	26997dc8b251aed1df00477d54d33d5c
URL:		http://gufw.org/
BuildRequires:	intltool
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	desktop-file-utils
Requires:	gobject-introspection
Requires:	gtk-webkit3
Requires:	notification-daemon
Requires:	python-dbus
Requires:	python-netifaces
Requires:	python-pygobject3
Requires:	ufw
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical user interface for Ubuntu's Uncomplicated Firewall.

%prep
%setup -q -n gui-ufw-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT


install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_iconsdir}/hicolor/48x48/apps}
cp -p data/icons/48x48/apps/%{name}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps
cp -p %{name}.desktop.in $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/README

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc README INSTALL
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/app_profiles
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/app_profiles/*.gufw_app
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/app_profiles/*.gufw_service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/app_profiles/*.jhansonxi
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/app_profiles/*.ufw_app
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-pkexec
%{_mandir}/man8/%{name}.8*
%{_datadir}/%{name}
%{_datadir}/polkit-1/actions/com.ubuntu.pkexec.%{name}.policy
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
