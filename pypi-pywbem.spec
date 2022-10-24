#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pywbem
Version  : 1.5.0
Release  : 82
URL      : https://files.pythonhosted.org/packages/63/40/2dc995ef6043c3ff1de96b5fb323d031d1f14aa0d29622080b626d556664/pywbem-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/40/2dc995ef6043c3ff1de96b5fb323d031d1f14aa0d29622080b626d556664/pywbem-1.5.0.tar.gz
Summary  : pywbem - A WBEM client
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-pywbem-bin = %{version}-%{release}
Requires: pypi-pywbem-license = %{version}-%{release}
Requires: pypi-pywbem-python = %{version}-%{release}
Requires: pypi-pywbem-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(certifi)
BuildRequires : pypi(mock)
BuildRequires : pypi(nocasedict)
BuildRequires : pypi(nocaselist)
BuildRequires : pypi(ply)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(yamlloader)

%description
.. # Note: On Pypi, variable substitution with raw content is not enabled, so
.. # we have to specify the package version directly in the links.

%package bin
Summary: bin components for the pypi-pywbem package.
Group: Binaries
Requires: pypi-pywbem-license = %{version}-%{release}

%description bin
bin components for the pypi-pywbem package.


%package license
Summary: license components for the pypi-pywbem package.
Group: Default

%description license
license components for the pypi-pywbem package.


%package python
Summary: python components for the pypi-pywbem package.
Group: Default
Requires: pypi-pywbem-python3 = %{version}-%{release}

%description python
python components for the pypi-pywbem package.


%package python3
Summary: python3 components for the pypi-pywbem package.
Group: Default
Requires: python3-core
Provides: pypi(pywbem)
Requires: pypi(certifi)
Requires: pypi(mock)
Requires: pypi(nocasedict)
Requires: pypi(nocaselist)
Requires: pypi(ply)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(setuptools)
Requires: pypi(six)
Requires: pypi(urllib3)
Requires: pypi(yamlloader)

%description python3
python3 components for the pypi-pywbem package.


%prep
%setup -q -n pywbem-1.5.0
cd %{_builddir}/pywbem-1.5.0
pushd ..
cp -a pywbem-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665693037
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pywbem
cp %{_builddir}/pywbem-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pywbem/caeb68c46fa36651acf592771d09de7937926bb3 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mof_compiler
/usr/bin/mof_compiler.bat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pywbem/caeb68c46fa36651acf592771d09de7937926bb3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
