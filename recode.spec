#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : recode
Version  : 3.7.14
Release  : 21
URL      : https://github.com/rrthomas/recode/releases/download/v3.7.14/recode-3.7.14.tar.gz
Source0  : https://github.com/rrthomas/recode/releases/download/v3.7.14/recode-3.7.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: recode-bin = %{version}-%{release}
Requires: recode-info = %{version}-%{release}
Requires: recode-lib = %{version}-%{release}
Requires: recode-license = %{version}-%{release}
Requires: recode-locales = %{version}-%{release}
Requires: recode-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : flex
BuildRequires : glibc-locale
BuildRequires : pypi-cython
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
#+OPTIONS: H:2 toc:2
* Introduction
** What is Recode?
The Recode library converts files between character sets and usages.
It recognises or produces over 200 different character sets (or about
300 if combined with an *iconv* library) and transliterates files
between almost any pair.  When exact transliteration are not possible,
it gets rid of offending characters or falls back on approximations.
The *recode* program is a handy front-end to the library.

%package bin
Summary: bin components for the recode package.
Group: Binaries
Requires: recode-license = %{version}-%{release}

%description bin
bin components for the recode package.


%package dev
Summary: dev components for the recode package.
Group: Development
Requires: recode-lib = %{version}-%{release}
Requires: recode-bin = %{version}-%{release}
Provides: recode-devel = %{version}-%{release}
Requires: recode = %{version}-%{release}

%description dev
dev components for the recode package.


%package info
Summary: info components for the recode package.
Group: Default

%description info
info components for the recode package.


%package lib
Summary: lib components for the recode package.
Group: Libraries
Requires: recode-license = %{version}-%{release}

%description lib
lib components for the recode package.


%package license
Summary: license components for the recode package.
Group: Default

%description license
license components for the recode package.


%package locales
Summary: locales components for the recode package.
Group: Default

%description locales
locales components for the recode package.


%package man
Summary: man components for the recode package.
Group: Default

%description man
man components for the recode package.


%prep
%setup -q -n recode-3.7.14
cd %{_builddir}/recode-3.7.14
pushd ..
cp -a recode-3.7.14 buildavx2
popd
pushd ..
cp -a recode-3.7.14 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685509815
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685509815
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/recode
cp %{_builddir}/recode-%{version}/COPYING %{buildroot}/usr/share/package-licenses/recode/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/recode-%{version}/COPYING-LIB %{buildroot}/usr/share/package-licenses/recode/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
%find_lang recode
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/recode
/V4/usr/bin/recode
/usr/bin/recode

%files dev
%defattr(-,root,root,-)
/usr/include/recode.h
/usr/include/recodext.h
/usr/lib64/librecode.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/recode.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/librecode.so.3.7.14
/V4/usr/lib64/librecode.so.3.7.14
/usr/lib64/librecode.so.3
/usr/lib64/librecode.so.3.7.14

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/recode/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/recode/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/recode.1

%files locales -f recode.lang
%defattr(-,root,root,-)

