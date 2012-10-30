Summary:	View and edit files in hexadecimal or in ASCII
Name:		hexedit
Version:	1.2.12
Release:	10
License:	GPLv2+
Group:		Editors
BuildRequires:	pkgconfig(ncursesw)
Url:		http://merd.net/pixel/hexedit.html
Source0:	http://merd.net/pixel/%{name}-%{version}.src.tar.bz2
Patch0:		hexedit-1.2.12-dont-strip-binary.patch

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be a device
as the file is read a piece at a time. You can modify the file and search
through it.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .nostrip~

%build
%configure
%make

%install
%makeinstall

%files
%doc TODO %{name}-%{version}.lsm
%{_bindir}/hexedit
%{_mandir}/man1/hexedit.1*
