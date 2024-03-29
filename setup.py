import pathlib
from setuptools import setup, find_packages
from version import __version__ as version


HERE = pathlib.Path(__file__).parent

long_description = (HERE / "readme.md").read_text()

setup(
    name="genqr",
    version=version,
    description="A simple QR code generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjfactor/Qr-Code-Generator",
    author="Mjfactor",
    install_requires=["qrcode[pil]"],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    package_data={'': ['readme.md']},
    include_package_data=True
)
