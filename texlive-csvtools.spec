# revision 15878
# category Package
# catalog-ctan /obsolete/macros/latex/contrib/csvtools
# catalog-date 2008-10-15 11:51:27 +0200
# catalog-license lppl
# catalog-version 1.24
Name:		texlive-csvtools
Version:	1.24
Release:	3
Summary:	Reading data from CSV files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/macros/latex/contrib/csvtools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvtools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvtools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvtools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The csvtools package allows you to repeatedly perform a set of
LaTeX commands on data in each row of a comma separated
variable (CSV) file (though substitution of the 'comma' is
permitted). Such files may be used as source for mail merging,
generating tables etc. Examples are given in the documentation.
The distribution also provides packages: csvsort, that provides
analagous commands to those in the main package, having first
sorted the data (using the xfor and compare packages); and
csvpie, for creating a pie-chart from a CSV file. The bundle
has now been superseded by the datatool bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/csvtools/csvpie.sty
%{_texmfdistdir}/tex/latex/csvtools/csvsort.sty
%{_texmfdistdir}/tex/latex/csvtools/csvtools.sty
%doc %{_texmfdistdir}/doc/latex/csvtools/CHANGES
%doc %{_texmfdistdir}/doc/latex/csvtools/README
%doc %{_texmfdistdir}/doc/latex/csvtools/csvtools.pdf
%doc %{_texmfdistdir}/doc/latex/csvtools/csvtools.pl
%doc %{_texmfdistdir}/doc/latex/csvtools/manual.html
#- source
%doc %{_texmfdistdir}/source/latex/csvtools/csvtools.dtx
%doc %{_texmfdistdir}/source/latex/csvtools/csvtools.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.24-2
+ Revision: 750661
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.24-1
+ Revision: 718176
- texlive-csvtools
- texlive-csvtools
- texlive-csvtools
- texlive-csvtools

