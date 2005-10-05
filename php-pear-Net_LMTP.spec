%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	LMTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an implementation of the RFC2033 LMTP protocol
Summary(pl):	%{_pearname} - implementacja protoko³u LMTP (RFC2033)
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	646d1c5293b069cda9b4a94011a18e20
URL:		http://pear.php.net/package/Net_LMTP/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Net_Socket
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an implementation of the RFC2033 LMTP using
PEAR's Net_Socket and Auth_SASL class.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza implementacjê protoko³u LMTP (opisanego w
RFC2033) za pomoc± klas Net_Socket oraz Auth_SASL.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
