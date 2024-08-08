# Pyfranka
>A Python/C++ library for controlling the Franka Panda robot.

The library supports basic joint/Cartesian position control and velocity control.

Pyfranka depends on [libfranka](https://github.com/frankaemika/libfranka) to interface with the robot, [Eigen](https://eigen.tuxfamily.org) for linear algebra operations and transformations, and [pybind11](https://github.com/pybind/pybind11) for the Python bindings.

This fork deals specifically with installing pyfranka to be compatible with libfranka v0.9.0, which is required if using a Franka Emika Panda robot with controller firmware version 5.

## Installation

To install the library on Linux, first build and install the [libfranka](https://github.com/frankaemika/libfranka):

`sudo apt remove "*libfranka*"
sudo apt update
sudo apt install -y build-essential cmake git python3 python3-pip python3-venv libeigen3-dev
git clone --branch 0.9.0 https://github.com/frankaemika/libfranka.git
cd libfranka
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
sudo cmake --install .
`
A continous integration workflow is included in this repo at .github/workflows/ci.yml, which contains a working version of system dependencies (gcc/g++ versions etc).

Next, build and install the [Eigen](https://eigen.tuxfamily.org), and [pybind11](https://github.com/pybind/pybind11) libraries.  Then clone the Pyfranka repository, move to the installation root directory, activate the python environment (e.g., [Conda](https://docs.conda.io/en/latest/)) you wish to install the library in, and run the following command:

```sh
pip install -e .
```
You can also install libfranka using dpkg, described as optional [here](https://frankaemika.github.io/docs/installation_linux.html#building-libfranka), and install pybind11 using pypi with the global argument, as described [here](https://pybind11.readthedocs.io/en/latest/installing.html#include-with-pypi).

While the library has not been tested on Windows, it may still be possible to install it, assuming that the various dependencies can be installed and the toolchain adapted for the Windows environment.

## Examples

See the Franka Panda examples in the [Common Robot Interface (CRI)](https://github.com/jlloyd237/cri) library.


## Meta

John Lloyd – jlloyd237@gmail.com

Distributed under the GPL v3 license. See ``LICENSE`` for more information.

[https://github.com/jloyd237/pyfranka](https://github.com/jlloyd237/)
