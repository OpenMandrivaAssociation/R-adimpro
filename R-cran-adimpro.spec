%define modulename adimpro
%define realver 0.4.4
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so\\|libRblas.so\\|libRlapack.so

Summary:	Adaptive smoothing of digital images for R
Name:		R-cran-%{modulename}
Version:	%realver
Release:	%mkrel 9
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	gcc-gfortran
BuildRequires:	lapack-devel
Requires:	imagemagick
Requires:	dcraw
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package implements the Propagation Separation approach by 
Polzehl and Spokoiny (2006) for smoothing digital images.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
