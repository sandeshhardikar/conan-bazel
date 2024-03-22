from conan import ConanFile
from conan.tools.google import Bazel, BazelToolchain, bazel_layout


class App(ConanFile):
    settings = "os", "arch", "build_type"
    generators = "BazelDeps"
    # layout = "bazel_layout"

    def layout(self):
         # Default generators folder will be "conan" in Conan 2.x
         self.folders.generators = "build"
         bazel_layout(self)

    def generate(self):
        tc = BazelToolchain(self)
        tc.generate()

    def requirements(self):
        self.requires("fmt/10.1.1")

    def build(self):
        bz = Bazel(self)
        # bz.build(target="//main:demo", clean=False)
        bz.build(target="//:main --platforms=@bazel_embedded//platforms:cortex_m0")
