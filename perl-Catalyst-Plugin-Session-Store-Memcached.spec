%define upstream_name    Catalyst-Plugin-Session-Store-Memcached
Name:		perl-%{upstream_name}
Version:	0.05
Release:	5

Summary:	Memcached storage for Catalyst sessions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://dev.catalyst.perl.org/repos/Catalyst/Catalyst-Plugin-Session-Store-Memcached
Source0:	https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Plugin-Session-Store-Memcached-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Cache::Memcached::Managed)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch

%description
'Catalyst::Plugin::Session::Store::Memcached' is a session storage plugin
for Catalyst that uses the the Cache::Memcached::Managed manpage module to
connect to memcached, a fast data caching server.

METHODS
    * get_session_data

    * store_session_data

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


