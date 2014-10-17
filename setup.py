from distutils.core import setup

github_url = 'https://github.com/Tatsh/cssq'

setup(
    name='cssq',
    version='0.0.1',
    author='Andrew Udvare',
    author_email='audvare@gmail.com',
    url='https://github.com/Tatsh/cssq',
    license='LICENSE.txt',
    description='Filter HTML with a CSS query.',
    long_description='''Filter HTML with a CSS query.

See %{url} for more information.'''.format(url=github_url),
    scripts=['bin/cssq'],
    install_requires=[
        'beautifulsoup4>=4.3.2',
        'requests>=2.4.1',
        'html5lib>=0.999',
    ],
)
