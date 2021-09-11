Name:           scid_vs_pc
Version:        4.22
Release:        1%{?dist}
Summary:        scid_vs_pc
License:        GPL
Source0:        https://downloads.sourceforge.net/project/scidvspc/source/%{name}-%{version}.tgz
Source1:        scid_vs_pc.desktop

BuildRequires:  tcl-devel tk-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Shane's Chess Information Database is a powerful Chess Toolkit, with which one
can create huge databases, run chess engines, and play casual games against the
computer or online with the Free Internet Chess Server. It was originally
written by Shane Hudson , and has received strong contribution from Pascal
Georges and others.

# find a better way
%global debug_package %{nil}

%prep
%setup -q

%build
./configure BINDIR=%{_bindir} SHAREDIR=%{_datadir}/scid
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
%{__install} images/logo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/scid-vs-pc.png

desktop-file-install \
 --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
 %{SOURCE1} 

%make_install

%files
%{_bindir}/fruit
%{_bindir}/pgnscid
%{_bindir}/phalanx
%{_bindir}/sc_remote
%{_bindir}/scid
%{_bindir}/scidlet
%{_bindir}/scidpgn
%{_bindir}/scidt
%{_bindir}/scmerge
%{_bindir}/tcscid
%{_bindir}/tkscid
%{_datadir}/scid
%{_datadir}/icons/*/*/apps/*.png
%{_datadir}/applications/scid_vs_pc.desktop
