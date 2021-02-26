#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Parallax Python 2 module - execute commands and copy files over SSH to multiple machines at once
Summary(pl.UTF-8):	Moduł Pythona 2 Parallax - wykonywanie poleceń i kopiowanie plików przez SSH na wielu maszynach jednocześnie
Name:		python-parallax
Version:	1.0.1
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/parallax
Source0:	https://files.pythonhosted.org/packages/source/p/parallax/parallax-%{version}.tar.gz
# Source0-md5:	d8fccb7c3465c19edb4b1a1836c15b75
URL:		https://pypi.python.org/pypi/parallax
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parallax SSH provides an interface to executing commands on multiple
nodes at once using SSH. It also provides commands for sending and
receiving files to multiple nodes using SCP.

%description -l pl.UTF-8
Parallax SSH udostępnia interfejs do wykonywania poleceń na wielu
maszynach jednocześnie przy użyciu SSH. Udostępnia także polecenia do
wysyłania i odbierania plików na wielu maszynach przy użyciu SCP

%package -n python3-parallax
Summary:	Parallax Python 3 module - execute commands and copy files over SSH to multiple machines at once
Summary(pl.UTF-8):	Moduł Pythona 3 Parallax - wykonywanie poleceń i kopiowanie plików przez SSH na wielu maszynach jednocześnie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-parallax
Parallax SSH provides an interface to executing commands on multiple
nodes at once using SSH. It also provides commands for sending and
receiving files to multiple nodes using SCP.

%description -n python3-parallax -l pl.UTF-8
Parallax SSH udostępnia interfejs do wykonywania poleceń na wielu
maszynach jednocześnie przy użyciu SSH. Udostępnia także polecenia do
wysyłania i odbierania plików na wielu maszynach przy użyciu SCP

%prep
%setup -q -n parallax-%{version}

%build
%if %{with python2}
%py_build
%{__sed} -i -e "s,'/usr/bin/parallax-askpass','/usr/bin/parallax-askpass-2'," build-2/lib/parallax/askpass_client.py
%endif

%if %{with python3}
%py3_build
%{__sed} -i -e "s,'/usr/bin/parallax-askpass','/usr/bin/parallax-askpass-3'," build-3/lib/parallax/askpass_client.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/parallax-askpass{,-3}
%endif

%if %{with python2}
%py_install

%py_postclean
%{__mv} $RPM_BUILD_ROOT%{_bindir}/parallax-askpass{,-2}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md
%attr(755,root,root) %{_bindir}/parallax-askpass-2
%{py_sitescriptdir}/parallax
%{py_sitescriptdir}/parallax-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-parallax
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md
%attr(755,root,root) %{_bindir}/parallax-askpass-3
%{py3_sitescriptdir}/parallax
%{py3_sitescriptdir}/parallax-%{version}-py*.egg-info
%endif
