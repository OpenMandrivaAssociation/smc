%define name smc
%define version 1.9
%define release %mkrel 5

Summary:	Secret Maryo Chronicles - a 2D platform game in classic style
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/smclone/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/smclone/SMC_Music_4.1_high.zip
# Fix build with recent boost - AdamW 2008/10
Patch0:		smc-1.6-boost.patch
License:	GPLv3+
Group:		Games/Arcade
URL:		http://www.secretmaryo.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	CEGUI0.6-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	boost-devel
BuildRequires:	libpng-devel
BuildRequires:	imagemagick

%description
Secret Maryo Chronicles is an open source two-dimensional platform
game with a style designed similar to classic sidescroller games. It 
utilizes the platform independent library SDL and an OpenGL 
accelerated graphics renderer developed in C++.

%prep
%setup -q
# The same file is provided twice
yes no | unzip -q %{SOURCE1}

%build
%configure2_5x
%make LDADD=-lpng

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -scale 48 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Secret Maryo Chronicles
Comment=A 2D platform game in the classic style
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
