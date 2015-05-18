%global pypi_name oslo.rootwrap
%global milestone a3

Name:           python-oslo-rootwrap
Version:        XXX
Release:        XXX
Summary:        Oslo Rootwrap

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-1.3.0.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr


%description
The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

Unlike other Oslo deliverables, it should **not** be used as a Python library,
but called as a separate process through the `oslo-rootwrap` command:

`sudo oslo-rootwrap ROOTWRAP_CONFIG COMMAND_LINE`

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}

#%check
#%{__python} setup.py test

%files
%doc README.rst LICENSE
%{python_sitelib}/oslo
%{python_sitelib}/oslo_rootwrap
%{python_sitelib}/*.egg-info
%{python_sitelib}/*-nspkg.pth
%{_bindir}/oslo-rootwrap
%{_bindir}/oslo-rootwrap-daemon

%changelog
