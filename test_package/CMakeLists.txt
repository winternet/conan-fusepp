cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(FindPkgConfig)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

pkg_check_modules(FUSE REQUIRED fuse3)
if(FUSE_FOUND)
  message(STATUS "Found fuse (include: ${FUSE_INCLUDE_DIRS}, library: ${FUSE_LIBRARIES})")
endif()


add_executable(example hello.cpp helloFS.cpp)

target_link_libraries(example ${CONAN_LIBS} ${FUSE_LIBRARIES})
target_include_directories(example PRIVATE ${FUSE_INCLUDE_DIRS})
set_target_properties(example PROPERTIES COMPILE_FLAGS "-D_FILE_OFFSET_BITS=64 -fpermissive")
