%global packname  adimpro
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.7.5
Release:          1
Summary:          Adaptive Smoothing of Digital Images
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/%{packname}/%{packname}_%{version}.tar.gz
Requires:         R-grDevices 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-grDevices
BuildRequires:    blas-devel
BuildRequires:    lapack-devel
%rename R-cran-adimpro

%description
This package implements tools for manipulationg digital images and the
Propagation Separation approach by Polzehl and Spokoiny (2006) for
smoothing digital images.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/libs
