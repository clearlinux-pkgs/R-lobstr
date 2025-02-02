#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-lobstr
Version  : 1.1.2
Release  : 14
URL      : https://cran.r-project.org/src/contrib/lobstr_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lobstr_1.1.2.tar.gz
Summary  : Visualize R Data Structures with Trees
Group    : Development/Tools
License  : MIT
Requires: R-lobstr-lib = %{version}-%{release}
Requires: R-cpp11
Requires: R-crayon
Requires: R-prettyunits
Requires: R-rlang
BuildRequires : R-cpp11
BuildRequires : R-crayon
BuildRequires : R-prettyunits
BuildRequires : R-rlang
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
structures inspired by str(). Includes ast() for visualizing abstract
    syntax trees, ref() for showing shared references, cst() for showing
    call stack trees, and obj_size() for computing object sizes.

%package lib
Summary: lib components for the R-lobstr package.
Group: Libraries

%description lib
lib components for the R-lobstr package.


%prep
%setup -q -n lobstr
pushd ..
cp -a lobstr buildavx2
popd
pushd ..
cp -a lobstr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737150316

%install
export SOURCE_DATE_EPOCH=1737150316
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lobstr/DESCRIPTION
/usr/lib64/R/library/lobstr/INDEX
/usr/lib64/R/library/lobstr/LICENSE
/usr/lib64/R/library/lobstr/Meta/Rd.rds
/usr/lib64/R/library/lobstr/Meta/features.rds
/usr/lib64/R/library/lobstr/Meta/hsearch.rds
/usr/lib64/R/library/lobstr/Meta/links.rds
/usr/lib64/R/library/lobstr/Meta/nsInfo.rds
/usr/lib64/R/library/lobstr/Meta/package.rds
/usr/lib64/R/library/lobstr/NAMESPACE
/usr/lib64/R/library/lobstr/NEWS.md
/usr/lib64/R/library/lobstr/R/lobstr
/usr/lib64/R/library/lobstr/R/lobstr.rdb
/usr/lib64/R/library/lobstr/R/lobstr.rdx
/usr/lib64/R/library/lobstr/help/AnIndex
/usr/lib64/R/library/lobstr/help/aliases.rds
/usr/lib64/R/library/lobstr/help/figures/logo.png
/usr/lib64/R/library/lobstr/help/lobstr.rdb
/usr/lib64/R/library/lobstr/help/lobstr.rdx
/usr/lib64/R/library/lobstr/help/paths.rds
/usr/lib64/R/library/lobstr/html/00Index.html
/usr/lib64/R/library/lobstr/html/R.css
/usr/lib64/R/library/lobstr/tests/testthat.R
/usr/lib64/R/library/lobstr/tests/testthat/_snaps/ast.md
/usr/lib64/R/library/lobstr/tests/testthat/_snaps/ref.md
/usr/lib64/R/library/lobstr/tests/testthat/_snaps/size.md
/usr/lib64/R/library/lobstr/tests/testthat/_snaps/sxp.md
/usr/lib64/R/library/lobstr/tests/testthat/_snaps/tree.md
/usr/lib64/R/library/lobstr/tests/testthat/test-address.R
/usr/lib64/R/library/lobstr/tests/testthat/test-ast.R
/usr/lib64/R/library/lobstr/tests/testthat/test-ref.R
/usr/lib64/R/library/lobstr/tests/testthat/test-size.R
/usr/lib64/R/library/lobstr/tests/testthat/test-sxp.R
/usr/lib64/R/library/lobstr/tests/testthat/test-tree.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/lobstr/libs/lobstr.so
/V4/usr/lib64/R/library/lobstr/libs/lobstr.so
/usr/lib64/R/library/lobstr/libs/lobstr.so
