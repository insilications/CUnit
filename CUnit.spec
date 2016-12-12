#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CUnit
Version  : 2.1
Release  : 8
URL      : http://downloads.sourceforge.net/cunit/CUnit-2.1-3.tar.bz2
Source0  : http://downloads.sourceforge.net/cunit/CUnit-2.1-3.tar.bz2
Summary  : A unit testing framework for 'C'
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: CUnit-lib
Requires: CUnit-data
Requires: CUnit-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
CUnit is a unit testing framework for C.
This package installs the CUnit static library,
headers, and documentation files.

%package data
Summary: data components for the CUnit package.
Group: Data

%description data
data components for the CUnit package.


%package dev
Summary: dev components for the CUnit package.
Group: Development
Requires: CUnit-lib
Requires: CUnit-data
Provides: CUnit-devel

%description dev
dev components for the CUnit package.


%package dev32
Summary: dev32 components for the CUnit package.
Group: Default
Requires: CUnit-lib32
Requires: CUnit-data

%description dev32
dev32 components for the CUnit package.


%package doc
Summary: doc components for the CUnit package.
Group: Documentation

%description doc
doc components for the CUnit package.


%package lib
Summary: lib components for the CUnit package.
Group: Libraries
Requires: CUnit-data

%description lib
lib components for the CUnit package.


%package lib32
Summary: lib32 components for the CUnit package.
Group: Default
Requires: CUnit-data

%description lib32
lib32 components for the CUnit package.


%prep
%setup -q -n CUnit-2.1-3
pushd ..
cp -a CUnit-2.1-3 build32
popd

%build
export LANG=C
%reconfigure --disable-static
make V=1  %{?_smp_mflags}
pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/doc/CUnit/CUnit_doc.css
/usr/doc/CUnit/error_handling.html
/usr/doc/CUnit/fdl.html
/usr/doc/CUnit/headers/Automated.h
/usr/doc/CUnit/headers/Basic.h
/usr/doc/CUnit/headers/CUCurses.h
/usr/doc/CUnit/headers/CUError.h
/usr/doc/CUnit/headers/CUnit.h
/usr/doc/CUnit/headers/CUnit_intl.h
/usr/doc/CUnit/headers/Console.h
/usr/doc/CUnit/headers/MyMem.h
/usr/doc/CUnit/headers/TestDB.h
/usr/doc/CUnit/headers/TestRun.h
/usr/doc/CUnit/headers/Util.h
/usr/doc/CUnit/headers/Win.h
/usr/doc/CUnit/index.html
/usr/doc/CUnit/introduction.html
/usr/doc/CUnit/managing_tests.html
/usr/doc/CUnit/running_tests.html
/usr/doc/CUnit/test_registry.html
/usr/doc/CUnit/writing_tests.html

%files data
%defattr(-,root,root,-)
/usr/share/CUnit/CUnit-List.dtd
/usr/share/CUnit/CUnit-List.xsl
/usr/share/CUnit/CUnit-Run.dtd
/usr/share/CUnit/CUnit-Run.xsl
/usr/share/CUnit/Memory-Dump.dtd
/usr/share/CUnit/Memory-Dump.xsl

%files dev
%defattr(-,root,root,-)
/usr/include/CUnit/Automated.h
/usr/include/CUnit/Basic.h
/usr/include/CUnit/CUError.h
/usr/include/CUnit/CUnit.h
/usr/include/CUnit/CUnit_intl.h
/usr/include/CUnit/Console.h
/usr/include/CUnit/MyMem.h
/usr/include/CUnit/TestDB.h
/usr/include/CUnit/TestRun.h
/usr/include/CUnit/Util.h
/usr/lib64/libcunit.so
/usr/lib64/pkgconfig/cunit.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcunit.so
/usr/lib32/pkgconfig/32cunit.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcunit.so.1
/usr/lib64/libcunit.so.1.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcunit.so.1
/usr/lib32/libcunit.so.1.0.1
