Summary:	Norwegian Nynorsk dictionary for aspell
Summary(pl):	S³ownik norweski (nynorsk) dla aspella
Name:		aspell-nn
Version:	0.50.1
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/nn/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	3711eb9df68f25262af10119579239bc
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Norwegian Nynorsk dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik norweski (nynorsk) (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
