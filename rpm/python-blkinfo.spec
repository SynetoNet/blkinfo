#### NOTE: if building locally you may need to do the following:
####
#### yum install rpmdevtools -y
#### spectool -g -R blkinfo.spec
####
#### At this point you can use rpmbuild -ba blkinfo.spec
#### (this is because our Source0 is a remote source)
%global pypi_name blkinfo
%if 0%{?fedora} || 0%{?rhel} >= 8
%global build_py3   1
%endif

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Python library to enumerate and filter block devices

License:        GPLv3
URL:            https://github.com/grinrag/blkinfo
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?build_py3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%else
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%endif



%description
blkinfo is a python library to list information
about all available or the specified block devices. It is based on lsblk command
line tool, provided by util-linux, in addition, it collects information about
block devices, using /sys/block, /sys/devices, /proc directories.

%if 0%{?build_py3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:  util-linux
%description -n python3-%{pypi_name}
blkinfo is a python library to list information
about all available or the specified block devices. It is based on lsblk command
line tool, provided by util-linux, in addition, it collects information about
block devices, using /sys/block, /sys/devices, /proc directories.
%else
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:  util-linux
%description -n python2-%{pypi_name}
blkinfo is a python library to list information
about all available or the specified block devices. It is based on lsblk command
line tool, provided by util-linux, in addition, it collects information about
block devices, using /sys/block, /sys/devices, /proc directories.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?build_py3}
%py3_build
%else
%py2_build
%endif

%if 0%{?build_py3}
%py3_install
%else
%py2_install
%endif

%if 0%{?build_py3}
%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%else
%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Jul 11 2019 Gennadii Altukhov <grinrag@gmail.com> - 0.1.2-1
- Initial RPM release

