from conans import ConanFile, CMake, tools


class FuseppConan(ConanFile):
    name = "fusepp"
    version = "3.0.0"
    license = "MIT"
    url = "https://github.com/winternet/conan-fusepp"
    description = "simple C++ wrapper for the FUSE filesystem"
    topics = ("fuse3", "wrapper", "filesystem", "fs")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/winternet/fusepp.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="fusepp")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("Fuse*.h", dst="include", src="fusepp")
        self.copy("Fuse.cpp", dst="include", src="fusepp")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fusepp"]

