%define upstream_name    CGI-Safe
%define upstream_version 1.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Safe method of using CGI.pm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(CGI)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The CGI-Safe module makes running the CGI environment safer
by eliminating dangerous %ENV variables and presetting
certain CGI.pm globals.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CGI
%{_mandir}/*/*
