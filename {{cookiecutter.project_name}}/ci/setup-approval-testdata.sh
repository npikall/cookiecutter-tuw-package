#!/bin/bash

mkdir -p {{ cookiecutter.approvaltests_geo_data_root }}/approved
ln -s {{ cookiecutter.approvaltests_geo_data_at_ci_vm }}/input {{ cookiecutter.approvaltests_geo_data_root }}/input
cp -r {{ cookiecutter.approvaltests_geo_data_at_ci_vm }}/approved/{{ cookiecutter.approvaldata_timestamp }} {{ cookiecutter.approvaltests_geo_data_root }}/approved/