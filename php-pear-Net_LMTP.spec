%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	LMTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an implementation of the RFC2033 LMTP protocol
Summary(pl):	%{_pearname} - implementacja protoko³u LMTP (RFC2033)
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2d757ad4eb8f8d8ef3f69f8b1c63df4d
URL:		http://pear.php.net/package/Net_LMTP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test_lmtp.php
%{php_pear_dir}/%{_class}/*.php
