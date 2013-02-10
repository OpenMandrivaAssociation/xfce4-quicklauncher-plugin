Summary:	Quicklauncher plugin for the Xfce panel
Name:		xfce4-quicklauncher-plugin
Version:	1.9.4
Release:	12
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-quicklauncher-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-quicklauncher-plugin/%{name}-%{version}.tar.bz2
Patch0:		01_save-settings.patch
Patch1:		02_fix-missing-english-translation.patch
Patch2:		xfce4-quicklauncher-plugin-1.9.4-parameters.patch
Patch3:		xfce4-quicklauncher-plugin-1.9.4-panel-load.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-quicklauncher-plugin

%description
This plugin allows you to have lots of launchers in the panel, displaying 
them on several lines.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std 

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.9.4-11mdv2012.0
+ Revision: 791559
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.9.4-10
+ Revision: 790055
- Rebuild for xfce 4.10

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.4-9mdv2011.0
+ Revision: 615610
- the mass rebuild of 2010.1 packages

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-8mdv2010.1
+ Revision: 462489
- Patch2: corrent executable name for xfce setting manager
- Patch3: fix plugin loading (mdvbz #54998)

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 1.9.4-7mdv2010.0
+ Revision: 446107
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-6mdv2009.1
+ Revision: 349475
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-5mdv2009.1
+ Revision: 295005
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.9.4-4mdv2009.0
+ Revision: 269792
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-3mdv2009.0
+ Revision: 194671
- Patch0: save settings at exit
- Patch1: add missing english translation

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-2mdv2008.1
+ Revision: 110129
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING and INSTALL files
- use upstream name
- new version

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.2-2mdv2008.0
+ Revision: 30476
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.2-1mdv2008.0
+ Revision: 30253
- new version

