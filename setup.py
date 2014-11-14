from distutils.core import setup


setup(
    name='pushgo-supervisor',
    version='0.0.4',
    description='Monitors health of instances within an ELB '
                'and adjusts a route53 resource group.',
    author='Jeremy Orem',
    author_email='oremj@mozilla.com',
    scripts=['bin/pushgo-supervise',
             'bin/pushgo-cloudwatch-metrics'],
)
