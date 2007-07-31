%define name smc
%define version 1.0
%define release %mkrel 1

Summary: Secret Maryo Chronicles - a 2D platform game in classic style
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/smclone/SMC_music_4.0_high.zip
License: GPL
Group: Games/Arcade
Url: http://www.secretmaryo.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: CEGUI-devel SDL_ttf-devel SDL_mixer-devel SDL_image-devel boost-devel

%description
Secret Maryo Chronicles is an open source two-dimensional platform
game with a style designed similar to classic sidescroller games. It 
utilizes the platform independent library SDL and an OpenGL 
accelerated graphics renderer developed in C++.

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

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Secret Maryo Chronicles
Comment=A 2D platform game in the classic style
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/smc
%{_datadir}/smc
%{_datadir}/applications/mandriva-%{name}.desktop
