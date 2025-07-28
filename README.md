# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. We use `uv` for virtual environment management and dependency installation.

To create and activate a virtualenv using `uv`:

```
$ uv venv ./.venv
$ source ./.venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies from `pyproject.toml` and `requirements-dev.txt`:

```
$ uv pip install .
$ uv pip install -r requirements-dev.txt
```

At this point you can now synthesize the CloudFormation template for this code.
Note that `cdk.json` has been updated to use the virtual environment's python for `app.py`.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `pyproject.toml` file and rerun the `uv pip install .`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
