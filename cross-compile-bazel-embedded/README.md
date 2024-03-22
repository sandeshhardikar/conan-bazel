# Cross compilation using bazel as build tool and conan as wrapper

Reference implementation is taken over from https://github.com/bazelembedded/bazel-embedded/tree/master . Breifly the steps are as follows

- Install a  cross compile profile by using `conan config install ../conan-config`
- Download bazel-embedded repository
- Download dependency bazel_embedded_deps() like some platforms , rule set to compile.
- Register platforms which are  defined in bazel_embedded/platforms/BUILD
- Download the customer compiler
- Register the toolchain
- Compile the target main using `bazel build //:main --platforms=@bazel_embedded//platforms:cortex_m0 --subcommands` or using the wrapper `./build.sh`