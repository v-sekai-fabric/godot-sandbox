def can_build(env, platform):
    if platform == "android":
        return False
    if platform == "ios":
        return False
    print("Building with ", env)
    if env.get("use_asan", False):
        print("Sandbox module cannot be built with ASAN enabled.")
        return False
    if env.get("module_mono_enabled", False):
        print("Sandbox module cannot be built with Mono enabled.")
        return False
    if env["platform"] == "web" and env.get("disable_exceptions", True):
        print("Sandbox module cannot be built for web with exceptions disabled.")
        return False
    # All platforms minus windows without mingw
    # Windows needs a compiler with the GNU extensions libriscv uses. MinGW and
    # clang-cl both have them; MSVC does not.
    if env["platform"] == "windows":
        return env.get("use_mingw", False) or env.get("use_llvm", False)
    return True


def configure(env):
    # Sandbox module now uses exceptions on all platforms including web
    # The platform has been configured to use emscripten exception handling
    if env["platform"] == "web":
        env["disable_exceptions"] = False
        print("Sandbox module configured with exceptions enabled for web platform")
    else:
        print("Sandbox module configured with exceptions enabled")


def get_doc_classes():
    return [
        "Sandbox",
        "ELFScript",
        "ELFScriptLanguage",
        "CPPScript",
        "CPPScriptLanguage",
        "ResourceFormatLoaderCPP",
        "ResourceFormatLoaderELF",
        "ResourceFormatSaverCPP",
        "ResourceFormatSaverELF",
    ]


def get_doc_path():
    return "doc_classes"
