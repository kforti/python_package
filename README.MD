# python_package
## Create python packages from the commandline

Install Instructions:
```commandline
git clone git@github.com:kforti/python_package.git
pip install python_package/

```

Basic Usage:
```commandline
python_package create --name <name of python package> --author <author of python package>
```

Example:
```commandline
python_package create --name test_package --author 'first_name last_name'
pip install test_package/
test_package some_command --option some_option
```