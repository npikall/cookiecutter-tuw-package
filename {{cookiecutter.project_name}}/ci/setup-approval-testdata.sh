#!/bin/bash

mkdir -p {{ cookiecutter.approvaltests_geo_data_mount }}/approved
ln -s {{ cookiecutter.approvaltests_geo_data_root }}/input {{ cookiecutter.approvaltests_geo_data_mount }}/input
cp -r {{ cookiecutter.approvaltests_geo_data_root }}/approved/{{ cookiecutter.approvaldata_timestamp }} {{ cookiecutter.approvaltests_geo_data_mount }}/approved/