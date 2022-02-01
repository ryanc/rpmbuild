%global srcname  Stockfish

%global _vpath_srcdir src

Name:            stockfish
Version:         14.1 
Release:         0%{?dist}
Source0:         https://github.com/official-%{name}/%{srcname}/archive/sf_%{version}.tar.gz#/%{srcname}-sf_%{version}.tar.gz
Summary:         Powerful open source chess engine
License:         GPLv3+
URL:             http://%{name}chess.org

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  xz

%description
Stockfish is a free UCI chess engine derived from Glaurung 2.1. It is not a
complete chess program, but requires some UCI compatible GUI (like XBoard with
PolyGlot, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz) in
order to be used comfortably. Read the documentation for your GUI of choice for
information about how to use Stockfish with your GUI.

%global debug_package %{nil}

%prep
%setup -q -n %{srcname}-sf_%{version}

%build
cd src
%ifarch x86_64
make %{?_smp_mflags} build ARCH=x86-64
%endif

%install
cd src
make PREFIX=%{buildroot}%{_prefix} install

%files
%license Copying.txt
%doc AUTHORS README.md
%{_bindir}/%{name}

%changelog
