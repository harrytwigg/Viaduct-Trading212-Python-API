from distutils.core import setup

setup(
    name='viaduct',         # How you named your package folder (MyLib)
    packages=['viaduct'],   # Chose the same as "name"
    version='0.0.2',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='	gpl-3.0',
    # Give a short description about your library
    description='Viaduct is a Trading212 REST API wrapper for python',
    author='Harry Twigg',                   # Type in your name
    author_email='harrytwigg111@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/harrytwigg/Viaduct-Trading212-Python-API',
    # I explain this later on
    download_url='https://github.com/harrytwigg/Viaduct-Trading212-Python-API/archive/0.0.2.tar.gz',
    keywords=['python', 'api', 'rest', 'api-wrapper', 'viaduct', 'trading212',
              'trading212-api'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'validators',
        'beautifulsoup4',
        'selenium',
        'logging',
        'matplotlib',
        'selenium',
        'json',
        'requests',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL-3 License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
