from setuptools import setup, find_packages

setup(
    name='bpm',
    version='0.4.0',
    description="Build (from Source) Package Manager for build-scripts, a package manager designed to use Makefiles as a primary method of management, building, installation and uninstallation",
    author='Thanatisia',
    author_email='55834101+Thanatisia@users.noreply.github.com',
    # packages=["mkparse"] ,# Default: find_packages()
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # List your dependencies here
        "pyright",
        "mkparse @ git+https://github.com/Thanatisia/makefile-parser-python"
    ],
    url='https://github.com/Thanatisia/bpm',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    entry_points = {
        # Program Entry Point(s) and scripts
        'console_scripts' : [
            'bpm = bpm.__main__:main',
        ],
    },
)

