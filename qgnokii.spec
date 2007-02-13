Summary:	QGnokii - Qt3 frontend for Gnokii
Summary(pl.UTF-8):	QGnokii - nakładka Qt3 dla Gnokii
Name:		qgnokii
Version:	0.4.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qgnokii/%{name}-%{version}.tar.gz
# Source0-md5:	6eadde2786620cf9d2f9ec251553a04b
URL:		http://qgnokii.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	gnokii
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QGnokii is an alternative frontend for Gnokii written in QT3.

%description -l pl.UTF-8
QGnokii jest alternatywną nakładką dla Gnokii, napisaną w QT3.

%prep
%setup -q

%build
export QTDIR=%{_prefix}
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install qgnokii $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qgnokii
