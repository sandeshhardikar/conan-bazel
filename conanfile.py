from conan import ConanFile
from conan.tools.google import Bazel, BazelToolchain


class ConsumerConan(ConanFile):

    name = "demo"
    version = "1.0.0"
    settings = "os", "arch", "build_type"

    def generate(self):
        tc = BazelToolchain(self)
        tc.generate()

    def build(self):
        bazel = Bazel(self)
        bazel.build(target="//main:demo", clean=False)
