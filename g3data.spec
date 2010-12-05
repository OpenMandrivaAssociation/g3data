%define name 	g3data
%define version 1.5.3
%define release %mkrel 2

Name:           %name
Version:        %version
Release:        %release
Group:          Graphics
License:        GPLv2+
URL:            http://www.frantz.fi/software/g3data.php
Summary:        Graph data extractor
Source:		http://www.frantz.fi/software/%{name}-%{version}.tar.gz
Source1:	g3data-icon.png
Patch0:		g3data-1.5.3-mdv-fix-makefile.patch	
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	imlib-devel
BuildRequires:	gtk2-devel >= 2.12.0
BuildRequires:	pkgconfig
BuildRequires:	perl-SGMLSpm 
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	imagemagick

%description
g3data is used for extracting data from graphs. In publications graphs often
are included, but the actual data is missing. g3data makes the extracting
process much easier.

While this is a GTK2 application, it must be run from the command line as:
$ g3data <filename>
where <filename> can be in any format imlib supports.

%prep
%setup -q
%patch0 -p1

%build
export CPPFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
cp %name %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1
cp *.1.gz %{buildroot}/%{_mandir}/man1/

mkdir -p %{buildroot}%{_iconsdir}/hicolor/16x16/apps/
convert -geometry 16x16 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/32x32/apps/
convert -geometry 32x32 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/48x48/apps/
convert -geometry 48x48 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=g3data
Comment=Data Extraction Tool
Exec=g3data
Icon=g3data
Terminal=false
Type=Application
Categories=GNOME;Science;Graphics;
StartupNotify=true
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache} hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache} hicolor
%endif

%files
%defattr(-,root,root)
%doc gpl.txt README.TEST test*
%{_bindir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%clean
rm -fr %{buildroot}
