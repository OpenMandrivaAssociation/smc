%define name smc
%define version 0.99.6
%define release %mkrel 2 

Summary: Secret Maryo Chronicles is a 2D platform game Game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/smclone/music_3.1_high.zip
License: GPL
Group: Games/Arcade
Url: http://www.secretmaryo.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: CEGUI-devel SDL_ttf-devel SDL_mixer-devel SDL_image-devel boost-devel

%description
Secret Maryo Chronicles is a 2D platform game Game built upon SDL.

%prep
%setup -q
# The same file is provided twice
yes no | unzip %SOURCE1 
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/smc
%{_datadir}/smc/*

%changelog
