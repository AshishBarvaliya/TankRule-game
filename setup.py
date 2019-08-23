import cx_Freeze

executables =[cx_Freeze.Executable("TankRule.py")]

cx_Freeze.setup(
        name="TankRule",
        version="1.0.0",
        author="Ash",
        options = {"build_exe":{"packages":["pygame"],"include_files":["t.png","Gun.wav","Explosion.wav"]}},
        description = "this is my second pygame project",
        executables=executables
)
