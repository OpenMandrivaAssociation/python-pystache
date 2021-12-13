%define	module	pystache

Summary:	Mustache for Python
Name:		python-%{module}
Version:	0.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/3f/e7/8750ba6c6101d6aa5ceeb20c013adf2c6f3554a12c71d75654b468404bfa/pystache-0.6.0.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://github.com/markokr/pystache/
BuildRequires:	python-setuptools
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
