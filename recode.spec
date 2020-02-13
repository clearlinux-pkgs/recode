#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : recode
Version  : 3.7.6
Release  : 1
URL      : https://github.com/rrthomas/recode/releases/download/v3.7.6/recode-3.7.6.tar.gz
Source0  : https://github.com/rrthomas/recode/releases/download/v3.7.6/recode-3.7.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: recode-bin = %{version}-%{release}
Requires: recode-info = %{version}-%{release}
Requires: recode-lib = %{version}-%{release}
Requires: recode-license = %{version}-%{release}
Requires: recode-locales = %{version}-%{release}
Requires: recode-man = %{version}-%{release}
BuildRequires : Cython
BuildRequires : flex
BuildRequires : glibc-locale
BuildRequires : python3-dev

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
%setup -q -n recode-3.7.6
cd %{_builddir}/recode-3.7.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581554927
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1581554927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/recode
cp %{_builddir}/recode-3.7.6/COPYING %{buildroot}/usr/share/package-licenses/recode/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/recode-3.7.6/COPYING-LIB %{buildroot}/usr/share/package-licenses/recode/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install
%find_lang recode

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/lib64/librecode.so.3
/usr/lib64/librecode.so.3.7.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/recode/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/recode/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/recode.1

%files locales -f recode.lang
%defattr(-,root,root,-)

