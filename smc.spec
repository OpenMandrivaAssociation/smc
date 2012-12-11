Summary:	Secret Maryo Chronicles - a 2D platform game in classic style
Name:		smc
Version:	1.9
Release:	13
License:	GPLv3+
Group:		Games/Arcade
URL:		http://www.secretmaryo.org/
Source0:	http://prdownloads.sourceforge.net/smclone/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/smclone/SMC_Music_5.0_high.zip
# suggested in http://thread.gmane.org/gmane.linux.redhat.fedora.rpmfusion.devel/7651/focus=7665
Patch0:		http://repo.calcforge.org/temp/smc-1.9-fix-implicit-linking.patch
# patch from upstream forum
Patch1:		smc-fixes-for-cegui-v0-7.diff
Patch2:		smc-1.9-boostmt.patch
Patch3:		boost_filesystem3.diff
BuildRequires:	pkgconfig(CEGUI-OPENGL) >= 0.7.0
BuildRequires:	pkgconfig(sdl) >= 1.2.10
BuildRequires:	pkgconfig(x11)
BuildRequires:	SDL_ttf-devel
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	gettext-devel
BuildRequires:	imagemagick
Requires:	%{name}-data = %{version}

%description
Secret Maryo Chronicles is an open source two-dimensional platform
game with a style designed similar to classic sidescroller games. It 
utilizes the platform independent library SDL and an OpenGL 
accelerated graphics renderer developed in C++.

%package data
Summary:	Games data for the %{name} game
Group:		Games/Arcade
Conflicts:	smc < 1.9-13
Requires:	%{name} = %{version}
BuildArch:	noarch

%description data
This package contains data files for %{name} game.

%prep
%setup -q
# The same file is provided twice
unzip -qo %{SOURCE1}
%patch0 -p1 -b .patch0
%patch1 -p1 -b .cegui07
%patch2 -p0 -b .boost
%patch3 -p1 -b .boost

%build
autoreconf -fi
export CXXFLAGS="%{optflags} -fpermissive"
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}/
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{32x32,48x48,64x64,256x256}/apps
convert -scale 256 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/%{name}.png
convert -scale 64 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 48 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 data/pixmaps/maryo/small/fall_right.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Secret Maryo Chronicles
Comment=A 2D platform game in the classic style
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%files
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%files data
%{_gamesdatadir}/%{name}


%changelog
* Thu Aug 30 2012 fwang <fwang> 1.9-12.mga3
+ Revision: 285759
- build with fpermissive
- rediff patch
- build with latest boost
- rebuild for new boost

  + dams <dams>
    - clean .desktop

* Mon Jun 04 2012 dams <dams> 1.9-11.mga3
+ Revision: 254055
+ rebuild (emptylog)

* Mon Jun 04 2012 dams <dams> 1.9-10.mga3
+ Revision: 253830
- clean spec file
- use 'gamesdatadir' and 'gamesbindir' to install game
- use better size for icon

* Fri Jun 01 2012 dams <dams> 1.9-9.mga3
+ Revision: 252573
- Update music to 5.01 release
- Require on '-data' package

* Wed May 30 2012 fwang <fwang> 1.9-8.mga3
+ Revision: 249548
- rebuild for new boost

* Sun Dec 11 2011 fwang <fwang> 1.9-7.mga2
+ Revision: 180710
- fix linkage
- split data pacakge

* Mon Nov 28 2011 fwang <fwang> 1.9-6.mga2
+ Revision: 173654
- rebuild for new boost

* Sun Sep 18 2011 fwang <fwang> 1.9-5.mga2
+ Revision: 145034
- rebuid for new libpng
- br gettext
- fix build with boost-mt

  + stormi <stormi>
    - clean spec

  + zezinho <zezinho>
    - imported package smc

