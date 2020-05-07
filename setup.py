from distutils.core import setup

setup(
    name='flisk',
    packages=['flisk'],
    version='0.1',
    license='MIT',
    description='A lightweight wrapper for flask to make cleaner url routes.',  # Give a short description about your library
    author='Harrison Burt',
    author_email='hburt2003@gmail.com',
    url='https://github.com/ChillFish8/flisk',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    keywords=['web', 'flask', 'webserver'],
    install_requires=[
        'flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
