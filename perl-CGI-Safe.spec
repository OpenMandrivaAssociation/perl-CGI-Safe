%define upstream_name    CGI-Safe
%define upstream_version 1.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Safe method of using CGI.pm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.bz2
Source1:	%{name}.rpmlintrc

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
The CGI-Safe module makes running the CGI environment safer
by eliminating dangerous %ENV variables and presetting
certain CGI.pm globals.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/CGI
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.250.0-2mdv2011.0
+ Revision: 680695
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.250.0-1mdv2011.0
+ Revision: 406869
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.25-5mdv2009.0
+ Revision: 255820
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-3mdv2008.1
+ Revision: 136921
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.25-2mdv2007.0
+ Revision: 73405
- import perl-CGI-Safe-1.25-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.25-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires
	- Source URL

* Fri Oct 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdk
- new version
- %%{1}mdv2007.1
- spec cleanup
- rpmbuildupdate aware
- fix directory ownership
- better summary

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.24-1mdk
- initial Mandriva package

