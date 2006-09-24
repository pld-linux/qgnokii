Summary:	QGnokii - Qt3 frontend for Gnokii
Summary(pl):	QGnokii - nak³adka Qt3 dla Gnokii
Name:		qgnokii
Version:	0.4.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qgnokii/%{name}-%{version}.tar.gz
# Source0-md5:	5626f9b41c79bdb633c76c8fd6b892d1
URL:		http://qgnokii.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	gnokii
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QGnokii is an alternative frontend for Gnokii written in QT3.

%description -l pl
QGnokii jest alternatywn± nak³adk± dla Gnokii, napisan± w QT3.

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
