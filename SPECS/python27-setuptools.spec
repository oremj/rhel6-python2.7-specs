%define __python python2.7
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")} 

%global srcname distribute

Name:           python27-setuptools
Version:        0.6.28
Release:        1%{?dist}
Summary:        Easily build and distribute Python packages

Group:          Applications/System
License:        Python or ZPLv2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        http://pypi.python.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        psfl.txt
Source2:        zpl.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python27-devel

# Legacy: We removed this subpackage once easy_install no longer depended on
# python-devel
Provides: python27-setuptools-devel = %{version}-%{release}
Obsoletes: python27-setuptools-devel < 0.6.7-1

# Provide this since some people will request distribute by name
Provides: python27-distribute = %{version}-%{release}

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.

%prep
%setup -q -n %{srcname}-%{version}
find -name '*.txt' | xargs chmod -x
#find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

rm -rf %{buildroot}%{python_sitelib}/setuptools/tests
rm -rf %{buildroot}%{python_sitelib}/*egg-info/*.orig

install -p -m 0644 %{SOURCE1} %{SOURCE2} .

find %{buildroot}%{python_sitelib} -name '*.exe' | xargs rm -f
chmod +x %{buildroot}%{python_sitelib}/setuptools/command/easy_install.py

rm -f %{buildroot}/%{_bindir}/easy_install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt docs
%{python_sitelib}/*
%{_bindir}/easy_install-2.7


%changelog
* Mon Sep 24 2012 Jeremiah Orem <oremj@oremj.com> - 0.6.28-1
- build for python2.7

* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.10-3
- cherrypick upstream patch for easy_install (ignore locally installed
packages: patch0)
- provide "python-distribute"
- add README.txt and other .txt documentation files to the payload
Resolves: rhbz#613138

* Mon Jun 28 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.10-2
- delete stray ".orig" file
- change %%define to %%global ; use %%{buildroot} rather than env var
- move %%check lower down
- explicitly list executables

* Mon Mar  8 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.10-1
- Switch over to using the "distribute" project; rebase to 0.6.10 (rhbz:570350)
- Remove svn patch as upstream has chosen to go with an easier change for now.
- Move easy_install back into the main package as the needed files have been
  moved from python-devel to the main python package.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6c9-5.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6c9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c9-4
- Apply SVN-1.6 versioning patch (rhbz #511021)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6c9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6c9-2
- Rebuild for Python 2.6

* Sun Nov 23 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c9-1
- Update to 0.6c9
- Small fixes to URL, summary and description

* Sat Jun 21 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c8-1
- Update to 0.6c8
- Accept small tweaks from Gareth Armstrong

* Mon Sep 24 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c7-2
- Move pretty much everything back into runtime in order to avoid more
  brokenness than we're trying to address with these fixes.

* Fri Sep 14 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c7-1
- Upstream 0.6c7
- Move some things from devel into runtime, in order to not break other
  projects.

* Sat Aug 18 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c6-2
- Make license tag conform to the new Licensing Guidelines
- Move everything except pkg_resources.py into a separate -devel package
  so we avoid bundling python-devel when it's not required (#251645)
- Do not package tests

* Sun Jun 10 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c6-1
- Upstream 0.6c6
- Require python-devel (#240707)

* Sun Jan 28 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c5-1
- Upstream 0.6c5 (known bugs, but the promised 0.6c6 is taking too long)

* Tue Dec 05 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c3-1
- Upstream 0.6c3 (#218540, thanks to Michel Alexandre Salim for the patch)

* Tue Sep 12 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c2-1
- Upstream 0.6c2
- Ghostbusting

* Mon Jul 31 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c1-2
- Set perms on license files (#200768)

* Sat Jul 22 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c1-1
- Version 0.6c1

* Wed Jun 28 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6b3-1
- Taking over from Ignacio
- Version 0.6b3
- Ghost .pyo files in sitelib
- Add license files
- Remove manual python-abi, since we're building FC4 and up
- Kill .exe files

* Wed Feb 15 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6a10-1
- Upstream update

* Mon Jan 16 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6a9-1
- Upstream update

* Sat Dec 24 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6a8-1
- Initial RPM release
