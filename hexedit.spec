Summary: View and edit files in hexadecimal or in ASCII
Name: hexedit
Version: 1.2.12
Release: %mkrel 8
License: GPL
Group: Editors
BuildRequires: ncurses-devel
Url: http://merd.net/pixel/hexedit.html
Source: http://merd.net/pixel/%{name}-%{version}.src.tar.bz2
BuildRoot: %{_tmppath}/%{name}

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be a device
as the file is read a piece at a time. You can modify the file and search
through it.


%prep
%setup -q -n %{name}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING TODO %{name}-%{version}.lsm
%{_bindir}/*
%{_mandir}/*/*


