from distutils.core import setup

setup(
    name='TVShowFile',
    version='0.1dev',
    packages=['tvshowfile',],
    long_description=open('README.md').read(),
    license='MIT',
    keywords='TV Television Parser Regex File',
    author='Adam Spann',
    author_email='baspann@gmail.com',
    url='https://github.com/Bas-Man/TVShowFile',
    scripts=['sample/BuildNewShowFileName.py', 'sample/sample1.py',
        'sample/sample2.py'
    ],
    include_package_data=True,
)
