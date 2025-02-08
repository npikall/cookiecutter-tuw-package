#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dir):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dir))


if __name__ == '__main__':

    if not "{{ cookiecutter.approvaltests_geo_data_at_ci_vm }}":
        remove_file('pytest.ini')

    has_approval = "{{ cookiecutter.approvaltests_geo_data_at_ci_vm }}" and ("{{ cookiecutter.approvaltests_geo_data_at_ci_vm }}" != "{{ cookiecutter.approvaltests_geo_data_root }}")
    if not has_approval:
        remove_file('ci/setup-approval-testdata.sh')
    has_pypi = "{{ cookiecutter.external_pypis }}"
    if not has_pypi:
        remove_file('ci/add-pypi-indices.sh')
    has_docker = {{ cookiecutter.package_docker }}
    if not has_docker:
        remove_file('ci/deploy-docker-image.sh')
        remove_dir('docker')
    if not has_approval and not has_pypi and not has_docker:
        remove_dir('ci')

    if "{{ cookiecutter.vsc_repo }}" == 'gitlab':
        remove_dir(".github")
    elif "{{ cookiecutter.vsc_repo }}" == 'github':
        remove_file(".gitlab-ci.yml")
    else:
        raise NotImplementedError(
            "The repository {{ cookiecutter.vsc_repo }} specified in cookiecutter.vsc_repo, is currently not supported.\nSpecify either 'gitlab' or 'github'")
