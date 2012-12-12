%bcond_without	uclibc

Summary:	View and edit files in hexadecimal or in ASCII
Name:		hexedit
Version:	1.2.12
Release:	11
License:	GPLv2+
Group:		Editors
BuildRequires:	pkgconfig(ncursesw)
Url:		http://merd.net/pixel/hexedit.html
Source0:	http://merd.net/pixel/%{name}-%{version}.src.tar.bz2
Patch0:		hexedit-1.2.12-dont-strip-binary.patch
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be a device
as the file is read a piece at a time. You can modify the file and search
through it.

%package -n	uclibc-%{name}
Summary:	View and edit files in hexadecimal or in ASCII (uClibc build)
Group:		Editors

%description -n	uclibc-%{name}
hexedit shows a file both in ASCII and in hexadecimal. The file can be a device
as the file is read a piece at a time. You can modify the file and search
through it.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .nostrip~

# too lazy to fix out of source build..
%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%if %{with uclibc}
pushd .uclibc
%uclibc_configure
%make
popd
%endif

%configure
%make

%install
%if %{with uclibc}
%makeinstall -C .uclibc bindir=%{buildroot}%{uclibc_root}%{_bindir}
%endif

%makeinstall

%files
%doc TODO %{name}-%{version}.lsm
%{_bindir}/hexedit
%{_mandir}/man1/hexedit.1*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/hexedit
%endif

%changelog
* Wed Dec 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.12-11
- rebuild on ABF

* Tue Oct 30 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.12-10
+ Revision: 820723
- do uclibc build
- leave stripping of binary to rpm (P0)
- cleanups

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-9mdv2011.0
+ Revision: 665410
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-8mdv2011.0
+ Revision: 605855
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-7mdv2010.1
+ Revision: 520117
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.12-6mdv2010.0
+ Revision: 425143
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-5mdv2009.1
+ Revision: 316760
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.12-4mdv2009.0
+ Revision: 221152
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.2.12-3mdv2008.1
+ Revision: 150254
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Jan 12 2007 Pixel <pixel@mandriva.com> 1.2.12-2mdv2007.1
+ Revision: 108021
- use mkrel
- Import hexedit

* Fri Sep 23 2005 Pixel <pixel@mandriva.com> 1.2.12-1mdk
- new release

* Wed Sep 21 2005 Pixel <pixel@mandriva.com> 1.2.11-1mdk
- new release

* Wed Aug 04 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.10-1mdk
- New release 1.2.10

* Mon Mar 15 2004 Pixel <pixel@mandrakesoft.com> 1.2.9-1mdk
- new release (brown paper bag version)
  - fix searching larger than 3 characters long strings

* Tue Jan 20 2004 Pixel <pixel@mandrakesoft.com> 1.2.8-1mdk
- new release
  - replace the unsafe getstr() with getnstr() (thanks to Richard Chadderton)

