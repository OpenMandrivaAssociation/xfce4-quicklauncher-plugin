Summary:	Quicklauncher plugin for the Xfce panel
Name:		xfce4-quicklauncher-plugin
Version:	1.9.4
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-quicklauncher-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-quicklauncher-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3
BuildRequires:	xfce-panel-devel >= 4.3
BuildRequires:	libxfcegui4-devel >= 4.3
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-quicklauncher-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This plugin allows you to have lots of launchers in the panel, displaying 
them on several lines.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
rm -rf  %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*