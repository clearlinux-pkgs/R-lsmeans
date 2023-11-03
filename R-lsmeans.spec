#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lsmeans
Version  : 2.30.0
Release  : 48
URL      : https://cran.r-project.org/src/contrib/lsmeans_2.30-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lsmeans_2.30-0.tar.gz
Summary  : Least-Squares Means
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-emmeans
BuildRequires : R-emmeans
BuildRequires : buildreq-R

%description
and mixed models. Compute contrasts or linear functions of 
    least-squares means, and comparisons of slopes. 
    Plots and compact letter displays. Least-squares means were proposed in
    Harvey, W (1960) "Least-squares analysis of data with unequal subclass numbers",
    Tech Report ARS-20-8, USDA National Agricultural Library, and discussed
    further in Searle, Speed, and Milliken (1980) "Population marginal means

%prep
%setup -q -c -n lsmeans
cd %{_builddir}/lsmeans

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641050459

%install
export SOURCE_DATE_EPOCH=1641050459
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lsmeans
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lsmeans
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lsmeans
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lsmeans || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lsmeans/CITATION
/usr/lib64/R/library/lsmeans/DESCRIPTION
/usr/lib64/R/library/lsmeans/INDEX
/usr/lib64/R/library/lsmeans/Meta/Rd.rds
/usr/lib64/R/library/lsmeans/Meta/data.rds
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
/usr/lib64/R/library/lsmeans/data/MOats.RData
/usr/lib64/R/library/lsmeans/data/autonoise.RData
/usr/lib64/R/library/lsmeans/data/feedlot.RData
/usr/lib64/R/library/lsmeans/data/fiber.RData
/usr/lib64/R/library/lsmeans/data/nutrition.RData
/usr/lib64/R/library/lsmeans/data/oranges.RData
/usr/lib64/R/library/lsmeans/help/AnIndex
/usr/lib64/R/library/lsmeans/help/aliases.rds
/usr/lib64/R/library/lsmeans/help/lsmeans.rdb
/usr/lib64/R/library/lsmeans/help/lsmeans.rdx
/usr/lib64/R/library/lsmeans/help/paths.rds
/usr/lib64/R/library/lsmeans/html/00Index.html
/usr/lib64/R/library/lsmeans/html/R.css
/usr/lib64/R/library/lsmeans/tests/lsmbasis-test.R
/usr/lib64/R/library/lsmeans/tests/lsmbasis-test.out
