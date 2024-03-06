#!/bin/bash

TOKEN=$1

if [ -f ~/.config/pip/pip.conf ]; then
	echo "pip.conf already exists, you've to add python indices manually."
else
	echo "creating pip.conf..."
	mkdir -p ~/.config/pip
	cat <<- EOF > ~/.config/pip/pip.conf
	[global]
	extra-index-url =
{%- for pypi_id in cookiecutter.external_pypis.split(',') %}
	    https://gitlab-ci-token:${TOKEN}@git.eodc.eu/api/v4/groups/{{ pypi_id }}/-/packages/pypi/simple/
{%- endfor %}
	EOF
fi
