resources(
  name="dist_info",
  sources=["custom.dist-info/**/*"]
)

python_distribution(
    name="mypkg",
    provides=python_artifact(
        name="mypkg",
        version="1.0.0",
    ),
    entry_points={
        "console_scripts": {
            "mod1": "mod1:main",
        },
        "mygroup": {
            "myentrypoint": "mod2:b",
        }
    },
    generate_setup=True,
)
