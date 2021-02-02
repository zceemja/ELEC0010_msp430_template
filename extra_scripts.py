Import("env", "projenv")

EMULATOR_LINK = "https://github.com/zceemja/msp430emu/archive/master.zip"

try:
    import msp430emu
except ImportError:
    env.Execute('pip install "%s"' % EMULATOR_LINK)

def on_upload(source, target, env):
    firmware_path = str(source[0])[:-4]
    # Check for update
    env.Execute('pip install "%s"' % EMULATOR_LINK)
    msp430emu.run(firmware_path + ".bin")

env.Replace(UPLOADCMD=on_upload)
env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction(" ".join([
        "$OBJCOPY", "-I", "elf32-little", "-O", "binary",
        '"$BUILD_DIR/${PROGNAME}.elf"', '"$BUILD_DIR/${PROGNAME}.bin"'
    ]), "Building $BUILD_DIR/${PROGNAME}.bin")
)