# Created by pyp2rpm-3.3.5
%global pypi_name django-htmlmin

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        1
Summary:        HTML minifier for Python frameworks (not only Django, despite the name)
Group:          Development/Python
License:        None
URL:            None
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(html5lib)
BuildRequires:  python3dist(setuptools)

%description
++++++++++++++ django-htmlmin ++++++++++++++ django-html is an HTML minifier
for Python, with full support for HTML 5. It supports Django, Flask and many
other Python web frameworks. It also provides a command line tool, that can be
used for static websites or deployment scripts.Why minify HTML code? One of the
important points on client side optimization is to minify HTML. With minified
HTML...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%doc README.rst
%{_bindir}/pyminify
%{python3_sitelib}/htmlmin
%{python3_sitelib}/django_htmlmin-%{version}-py%{python3_version}.egg-info
