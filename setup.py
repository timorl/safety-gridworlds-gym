from setuptools import setup, find_packages

setup(
    name="safety_gridworlds_gym",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["numpy", "gym"],
    license="",
    package_data={"safety_gridworlds_gym.envs.common": ["*.ttf"]}
)
