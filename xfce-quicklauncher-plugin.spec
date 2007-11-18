%define oname xfce4-quicklauncher-plugin

Summary:	Quicklauncher plugin for the Xfce panel
Name:		xfce-quicklauncher-plugin
Version:	1.9.4
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-quicklauncher-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-quicklauncher-plugin/xfce4-quicklauncher-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3
BuildRequires:	xfce-panel-devel >= 4.3
BuildRequires:	libxfcegui4-devel >= 4.3
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This plugin allows you to have lots of launchers in the panel, displaying 
them on several lines.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{oname}

%clean
rm -rf  %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*
