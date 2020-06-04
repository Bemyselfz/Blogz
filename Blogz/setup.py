from setuptools import setup, find_packages


setup(
    name='Blogz',
    version = '0.1',
    description = 'Blog System base on Django',
    author = 'Free',
    author_eamil = '645548322@qq.com',
    url = "https://www.Ineed520.cn",
    license = "MIT",
    packages = find_packages('Blogz'),
    package_dir = {'','Blogz'},
    include_package_data = True,
    install_requires = [
        'django ~=2.0.3',
    ],
    extras_require={
        'ipython':['ipython==6.2.1']
    },
    scripts = [
        'Blogz/manage.py',
    ],
    entry_points = {
        'console_scripts':[
            'Blogz_manage = manage:main',
        ]
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Adudience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ]

)