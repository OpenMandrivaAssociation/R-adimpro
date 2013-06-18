%global packname  adimpro
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.7.8
Release:          2
Summary:          Adaptive Smoothing of Digital Images
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/adimpro_0.7.8.tar.gz
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
%{rlibdir}/%{packname}/adjust

%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.6-1
+ Revision: 775041
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.5-1
+ Revision: 774843
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-9mdv2011.0
+ Revision: 616446
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.4.4-8mdv2010.0
+ Revision: 433149
- BuildRequires lapack-devel
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.4.4-7mdv2009.0
+ Revision: 260121
- rebuild
- rebuild

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-4mdv2008.1
+ Revision: 182146
- remove requires on libRlapack.so

* Mon Mar 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-3mdv2008.1
+ Revision: 177972
- remove requires on libRblas.so

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-2mdv2008.1
+ Revision: 176961
- remove requires on libR.so

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-1mdv2008.1
+ Revision: 170017
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-adimpro.


