%define module CGI-Safe
%define name	perl-%{module}
%define version 1.25
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Safe method of using CGI.pm
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(CGI)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The CGI-Safe module makes running the CGI environment safer
by eliminating dangerous %ENV variables and presetting
certain CGI.pm globals.

%prep
%setup -q -n %{module}-%{version} 

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




