from setuptools import setup, find_packages

setup(
    name='pycheck',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['click', "termcolor"],
    description='flake8 + mypy + color = pycheck',
    author='Brijesh krishna',
    author_email='brijesh.krishna@gmail.com',
    long_description_content_type='text/markdown',
    long_description =open('README.md').read(),
    url='https://github.com/Brijeshkrishna/pycheck',
    keywords=['pycheck','flake8','mypy','python check','python syntax check','python','color print','color py'],
    entry_points='''
        [console_scripts]
        pycheck=pycheck.pycheck:pycheck
    ''',
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

