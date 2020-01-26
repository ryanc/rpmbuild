Name:           spiped
Version:        1.6.0
Release:        1%{?dist}
Summary:        Spiped is a utility for creating symmetrically encrypted and authenticated pipes between socket addresses.

License:        BSD
URL: https://www.tarsnap.com/spiped.html
Source0: https://www.tarsnap.com/%{name}/%{name}-%{version}.tgz

BuildRequires: gcc
BuildRequires: make
BuildRequires: openssl-devel
Requires: openssl-libs

%global debug_package %{nil}

%description


%prep
%autosetup

%build
%set_build_flags
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install \
    BINDIR=%{buildroot}/%{_bindir} \
    MAN1DIR=%{buildroot}/%{_mandir}/man1


%files
%{_bindir}/spiped
%{_bindir}/spipe
%{_mandir}/man1/spiped.1*
%{_mandir}/man1/spipe.1*
%license COPYRIGHT
%doc README.md


%changelog
* Mon Jan 13 2020 Ryan Cavicchioni <ryan@cavi.cc>
- spiped 1.6.0
