from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='LensMotionMania',
    version='0.1',
    packages=find_packages(),
    install_requires=requirments,
    description='Hides the text in the image and decodes it',
    author='AIWizardsTeam',
    author_email='aiwizardsteam@gmail.com',
    )
