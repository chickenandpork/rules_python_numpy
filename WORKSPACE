# based on rules_python/examples/pip_parse/WORKSPACE

workspace(name = "rules_python_numpy")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "5868e73107a8e85d8f323806e60cad7283f34b32163ea6ff1020cf27abef6036",
    strip_prefix = "rules_python-0.25.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.25.0/rules_python-0.25.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()

python_register_toolchains(
    name = "python39",
    python_version = "3.9",
)

load("@python39//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pypi",
    environment = {"HTTPS_PROXY": "http://10.0.0.9:3128/"},
    # extra_pip_args = ["-v"],
    # pip_data_exclude = ["**/* */**"],
    python_interpreter_target = interpreter,

    # (Optional) You can set quiet to False if you want to see pip output.
    #quiet = False,
    requirements_lock = "//:requirements_lock.txt",
)

load("@pypi//:requirements.bzl", "install_deps")

# Initialize repositories for all packages in requirements_lock.txt.
install_deps()
