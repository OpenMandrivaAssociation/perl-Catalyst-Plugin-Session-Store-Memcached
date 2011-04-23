%define upstream_name    Catalyst-Plugin-Session-Store-Memcached
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Memcached storage for Catalyst sessions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-Class-Data-Inheritable
BuildRequires: perl(Cache::Memcached::Managed)
BuildRequires: perl(Catalyst::Plugin::Session)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'Catalyst::Plugin::Session::Store::Memcached' is a session storage plugin
for Catalyst that uses the the Cache::Memcached::Managed manpage module to
connect to memcached, a fast data caching server.

METHODS
    * get_session_data

    * store_session_data

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


