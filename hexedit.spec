%bcond_without	uclibc

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

%description
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
