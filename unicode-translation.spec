Summary:	Unicode character names translation
Summary(pl.UTF-8):   Tłumaczenia nazw znaków unikodowych
Name:		unicode-translation
Version:	0.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://freedesktop.org/Software/unicode-translation/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0d927704c0a39ff0c6776b26a8db2f12
# it's not directory, don't add /
URL:		http://freedesktop.org/Software/unicode-translation
BuildRequires:	intltool >= 0.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unicode-translation project aims to translate Unicode character
names and other data into many languages using the gettext framework.
It is a subproject of project UTF-8
(http://freedesktop.org/Software/utf-8).

%description -l pl.UTF-8
Celem projektu unicode-translation jest przetłumaczenie nazw znaków
i innych danych związanych z Unikodem na wiele języków przy użyciu
szkieletu gettext. Jest to podprojekt projektu UTF-8
(http://freedesktop.org/Software/utf-8).

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%{_pkgconfigdir}/*.pc
