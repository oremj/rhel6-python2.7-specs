%define binsuffix 27
%define pybasever 2.7
%define version 2.7.3
%define name python
%define release 2

Name: %{name}%{binsuffix}
Version: %{version}
Release: %{release}
Summary: An interpreted, interactive, object-oriented programming language.
Group: Development/Languages
Source0: Python-%{version}.tar.bz2

License: PSF
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

AutoReq: no
Provides: python(abi) = %{pybasever}

BuildRequires: autoconf
BuildRequires: bzip2
BuildRequires: bzip2-devel
BuildRequires: db4-devel 

# expat 2.1.0 added the symbol XML_SetHashSalt without bumping SONAME.  We use
# it (in pyexpat) in order to enable the fix in Python-3.2.3 for CVE-2012-0876:
BuildRequires: expat-devel

BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: libffi-devel
BuildRequires: libGL-devel
BuildRequires: libX11-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: sqlite-devel


BuildRequires: tar
BuildRequires: tcl-devel
BuildRequires: tix-devel
BuildRequires: tk-devel

BuildRequires: zlib-devel

%description
Python is an interpreted, interactive, object-oriented programming
language.  It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface.  Finally, Python is portable: it runs on many
brands of UNIX, on PCs under Windows, MS-DOS, and OS/2, and on the
Mac.

%package devel
Summary: The libraries and header files needed for Python extension development.
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install python-devel if you want to develop Python extensions.  The
python package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%prep
%setup -n Python-%{version}


%build
%configure --enable-unicode=ucs4 --enable-shared --prefix=%{_prefix}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/python{,2}
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/python{,2}-config
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/2to3
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/idle
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/pydoc
%{__rm} -f $RPM_BUILD_ROOT%{_prefix}/bin/smtpd.py
%{__rm} -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
%{__ln_s} %{_libdir}/python2.7/config $RPM_BUILD_ROOT%{_prefix}/lib/python2.7/config
%{__ln_s} %{_libdir}/python2.7/lib-dynload $RPM_BUILD_ROOT%{_prefix}/lib/python2.7/lib-dynload

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_prefix}/lib/python2.7/*
%{_libdir}/python2.7/lib-dynload/*
%{_libdir}/libpython2.7.so*
%{_bindir}/python2.7*
%{_prefix}/lib/python2.7/config
%{_libdir}/python2.7/config/Makefile
%{_prefix}/include/python2.7/pyconfig.h

%doc
%{_mandir}/man1/python2.7.1.gz

%files devel
%defattr(-,root,root,-)
%{_prefix}/include/python2.7/*
%{_libdir}/python2.7/config/*
%{_prefix}/lib/python2.7/config

%changelog
* Mon Sep 24 2012 Jeremiah Orem <oremj@oremj.com> - 2.7.3-1
- Initial RPM release
