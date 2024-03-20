import setuptools

import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_requirements():
    """parses requirements from requirements.txt"""
    reqs_path = os.path.join(__location__, 'requirements.txt')
    with open(reqs_path, encoding='utf8') as f:
        reqs = [line.strip() for line in f if not line.strip().startswith('#')]

    names = []
    links = []
    for req in reqs:
        if '://' in req:
            links.append(req)
        else:
            names.append(req)
    return {'install_requires': names, 'dependency_links': links}


setuptools.setup(
    name='mn_agent',
    version='1.0.0',
    include_package_data=True,
    description='An open source agent for business purposes',
    long_description='An open source agent for business purposes contains NLP',
    keywords=['chatbots', 'microservices', 'dialog systems', 'NLP'],
    packages=setuptools.find_packages(exclude=('docs',)),
    python_requires='>=3.7',
    data_files=[('.', ['mn_agent/settings.yaml'])],
    url="https://github.com/MadShift/mn-agent",
    **read_requirements()
)
