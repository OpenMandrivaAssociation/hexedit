Summary:	View and edit files in hexadecimal or in ASCII
Name:		hexedit
Version:	1.4.2
Release:	1
License:	GPLv2+
Group:		Editors
BuildRequires:	pkgconfig(ncursesw)
Url:		http://rigaux.org/hexedit.html
Source0:	https://github.com/pixel/hexedit/archive/%{version}.tar.gz
Patch0:		hexedit-1.2.13-dont-strip-binary.patch

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be a device
as the file is read a piece at a time. You can modify the file and search
through it.

%prep
%setup -q

%build
./autogen.sh
%configure
%make LIBS='-lncursesw'

%install
%makeinstall

%files
%doc TODO
%{_bindir}/hexedit
%{_mandir}/man1/hexedit.1*
