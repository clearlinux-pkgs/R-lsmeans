#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-lsmeans
Version  : 2.30.2
Release  : 51
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/lsmeans_2.30-2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/lsmeans_2.30-2.tar.gz
Summary  : Least-Squares Means
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-emmeans
BuildRequires : R-emmeans
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and mixed models. Compute contrasts or linear functions of 
    least-squares means, and comparisons of slopes. 
    Plots and compact letter displays. Least-squares means were proposed in
    Harvey, W (1960) "Least-squares analysis of data with unequal subclass numbers",
    Tech Report ARS-20-8, USDA National Agricultural Library, and discussed
    further in Searle, Speed, and Milliken (1980) "Population marginal means

%prep
%setup -q -n lsmeans
pushd ..
cp -a lsmeans buildavx2
popd
pushd ..
cp -a lsmeans buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742848282

%install
export SOURCE_DATE_EPOCH=1742848282
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
/usr/lib64/R/library/lsmeans/CITATION
/usr/lib64/R/library/lsmeans/DESCRIPTION
/usr/lib64/R/library/lsmeans/INDEX
/usr/lib64/R/library/lsmeans/Meta/Rd.rds
/usr/lib64/R/library/lsmeans/Meta/features.rds
/usr/lib64/R/library/lsmeans/Meta/hsearch.rds
/usr/lib64/R/library/lsmeans/Meta/links.rds
/usr/lib64/R/library/lsmeans/Meta/nsInfo.rds
/usr/lib64/R/library/lsmeans/Meta/package.rds
/usr/lib64/R/library/lsmeans/NAMESPACE
/usr/lib64/R/library/lsmeans/NEWS
/usr/lib64/R/library/lsmeans/R/lsmeans
/usr/lib64/R/library/lsmeans/R/lsmeans.rdb
/usr/lib64/R/library/lsmeans/R/lsmeans.rdx
/usr/lib64/R/library/lsmeans/help/AnIndex
/usr/lib64/R/library/lsmeans/help/aliases.rds
/usr/lib64/R/library/lsmeans/help/lsmeans.rdb
/usr/lib64/R/library/lsmeans/help/lsmeans.rdx
/usr/lib64/R/library/lsmeans/help/paths.rds
/usr/lib64/R/library/lsmeans/html/00Index.html
/usr/lib64/R/library/lsmeans/html/R.css
/usr/lib64/R/library/lsmeans/tests/lsmbasis-test.R
/usr/lib64/R/library/lsmeans/tests/lsmbasis-test.out
