from setuptools import setup

setup(
    name='rofi-clipster',
    version='0.0.1',
    description='A rofi interface for clipster',
    author='fdw',
    author_email='5821180+fdw@users.noreply.github.com',
    url='https://github.com/fdw/rofi-clipster',
    keywords='rofi clipster clipboard',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],

    packages=['clippy'],
    entry_points={
        'console_scripts': [
            'rofi-clipster = clippy.Clippy:main'
        ]
    }
)
