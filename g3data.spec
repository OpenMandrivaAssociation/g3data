%define name 	g3data
%define version 1.5.1
%define release %mkrel 2 

Name:           %name
Version:        %version
Release:        %release
Group:          Graphics
License:        GPL
URL:            http://koti.welho.com/jfrantz/software/g3data.html
Summary:        Graph data extractor
Source:		http://freshmeat.net/redir/g3data/28160/url_tgz/%{name}-%{version}.tar.bz2
Source1:	g3data-icon.png
BuildRequires:	imlib-devel gtk2-devel pkgconfig
BuildRequires:	perl-SGMLSpm docbook-utils docbook-dtd41-sgml imagemagick

%description
g3data is used for extracting data from graphs. In publications graphs often
are included, but the actual data is missing. g3data makes the extracting
process much easier.

While this is a GTK2 application, it must be run from the command line as:
$ g3data <filename>
where <filename> can be in any format imlib supports.

%prep
%setup -q

%build
%make CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir/
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
cp *.1.gz $RPM_BUILD_ROOT/%_mandir/man1/

mkdir -p %{buildroot}%{_iconsdir}/hicolor/16x16/apps/
convert -geometry 16x16 %SOURCE1 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/32x32/apps/
convert -geometry 32x32 %SOURCE1 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/48x48/apps/
convert -geometry 48x48 %SOURCE1 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

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

%post
%{update_menus}
%{update_icon_cache} hicolor

%postun
%{clean_menus}
%{clean_icon_cache} hicolor

%files
%defattr(-,root,root)
%doc gpl.txt README.TEST test*
%{_bindir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%clean
rm -fr $RPM_BUILD_ROOT
