# For setup.py if not you't use other build systems:
setup(
   ...,
   command_options={
      'nuitka': {
         # boolean option, e.g. if you cared for C compilation commands
         '--show-scons': True,
         # options without value, e.g. enforce using Clang
         '--clang': None,
         # options with single values, e.g. enable a plugin of Nuitka
         '--enable-plugin': "pyside2",
         # options with several values, e.g. avoiding including modules
         '--nofollow-import-to' : ["*.tests", "*.distutils"],
      }
   },
)

# For setup.py with other build systems:
# The tuple nature of the arguments is required by the dark nature of
# "setuptools" and plugins to it, that insist on full compatibility,
# e.g. "setuptools_rust"

setup(
   ...,
   command_options={
      'nuitka': {
         # boolean option, e.g. if you cared for C compilation commands
         '--show-scons': ("setup.py", True),
         # options without value, e.g. enforce using Clang
         '--clang': ("setup.py", None),
         # options with single values, e.g. enable a plugin of Nuitka
         '--enable-plugin': ("setup.py", "pyside2"),
         # options with several values, e.g. avoiding including modules
         '--nofollow-import-to' : ("setup.py", ["*.tests", "*.distutils"]),
      }
   },
)
