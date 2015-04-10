from distutils.core import setup


setup(
    name='autopush-supervisor',
    version='1.0.0',
    description='Monitors health of instances within an ELB '
                'and adjusts a route53 resource group.',
    author='Jeremy Orem',
    author_email='oremj@mozilla.com',
    scripts=['bin/autopush-supervisor',
             'bin/pushgo-cloudwatch-metrics'],
)
