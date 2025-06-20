from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

ext_modules = [
    Pybind11Extension(
        "mesh_inpaint_processor",
        ["mesh_inpaint_processor.cpp"],
        cxx_std=11,
    ),
]

setup(
    name='mesh_inpaint_processor',
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
