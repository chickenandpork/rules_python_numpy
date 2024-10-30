# rules_python_numpy
Originally created to show a specific pip_parse() issue with numpy,this repo now acts as a simple
demonstration of Munpy with Bazel and RenovateBot.

## linux requirements on Mac

I develop mostlyon a Mac, but of course nVidia needs a linux env: I've been creating the
linux-specific requirements using:
```
docker run --rm -it \
    -v ~/src/rules_python_numpy:/rules_python_numpy \
    -w /rules_python_numpy \
    ubuntu:22.04 bash -c '
        apt-get update && \
        apt-get install -y curl gcc && \
        curl -Lo /bin/bazel https://github.com/bazelbuild/bazelisk/releases/download/v1.20.0/bazelisk-linux-amd64 && \
        chmod +x /bin/bazel && \
        bazel build //...
'
```
