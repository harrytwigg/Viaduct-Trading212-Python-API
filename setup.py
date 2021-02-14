from distutils.core import setup

setup(
    name='viaduct',         # How you named your package folder (MyLib)
    packages=['viaduct'],   # Chose the same as "name"
    version='0.0.6',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='gpl-3.0',
    # Give a short description about your library
    description='Viaduct is a Trading212 REST API wrapper for python',
    long_description="Viaduct is a Python REST API wrapper that utilises Trading212's REST API that normally communciates exclusively with first party apps. This has not been offically released publicly but can be reverse engineered. Selenium is used to scrape required cookies and customer data from the web app but is no longer required after this point. REST network calls are used enabling greater functionallity and speed than pure web scraping. The use of a wrapper ensures any API changes in the future will not impact pre-existing Trading212 dependeant programs as the wrapper itself can be updated instead of the underlying code.",
    author='Harry Twigg',                   # Type in your name
    author_email='harrytwigg111@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/harrytwigg/Viaduct-Trading212-Python-API',
    # I explain this later on
    download_url='https://github.com/harrytwigg/Viaduct-Trading212-Python-API/archive/0.0.6.tar.gz',
    keywords=['python', 'api', 'rest', 'api-wrapper', 'viaduct', 'trading212',
              'trading212-api'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'validators',
        'beautifulsoup4',
        'selenium',
        'matplotlib',
        'selenium',
        'requests',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
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
