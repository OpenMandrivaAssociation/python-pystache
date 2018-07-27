%define	module	pystache

Summary:	Mustache for Python
Name:		python-%{module}
Version:	0.5.4
Release:	1
Source0:	https://pypi.python.org/packages/source/p/pystache/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://github.com/markokr/pystache/
BuildArch:	noarch

%description
Mustache for Python

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build 

%install
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%clean

%files
%doc  LICENSE  
%{_bindir}/pystache*
%py_puresitedir/%{module}*
