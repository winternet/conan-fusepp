
#!/bin/bash

set -e
set -x

conan remote add ${CONAN_REMOTE} "https://api.bintray.com/conan/winternet/${CONAN_REMOTE}"
conan user -p ${CONAN_API_KEY} -r ${CONAN_REMOTE} ${CONAN_USER}
conan create . fusepp/3.0.0@winternet/testing
conan upload fusepp/3.0.0@winternet/testing -r ${CONAN_REMOTE}
