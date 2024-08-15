# based on rules_python/examples/pip_parse/WORKSPACE

workspace(name = "rules_python_numpy")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    patches = [
        # https://github.com/bazelbuild/rules_python/pull/1166 not yet merged; I'd like to use:
        # (in pip_parse())
        # requirement_clusters = {
        #     "torch-triton": [
        #         "torch",
        #         "triton",
        #     ]}
        # ... but PR1166 not yet merged.  nkey0's workaround hardcoding triton and torch
        "//bzl/patches:nkey0-circulardeps.patch",  # https://github.com/bazelbuild/rules_python/pull/1166#issuecomment-1701230930
    ],
    sha256 = "be04b635c7be4604be1ef20542e9870af3c49778ce841ee2d92fcb42f9d9516a",
    strip_prefix = "rules_python-0.35.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.35.0/rules_python-0.35.0.tar.gz",
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
    #environment = {"HTTPS_PROXY": "http://10.0.0.9:3128/"},
    # extra_pip_args = ["-v"],
    # pip_data_exclude = ["**/* */**"],
    python_interpreter_target = interpreter,

    # (Optional) You can set quiet to False if you want to see pip output.
    #quiet = False,
    requirements_linux = "//:requirements_linux_lock.txt",
    requirements_lock = "//:requirements_lock.txt",
)

load("@pypi//:requirements.bzl", "install_deps")

# Initialize repositories for all packages in requirements_lock.txt.
install_deps()
