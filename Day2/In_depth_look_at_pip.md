## Some common useful features while working with pip 

- provides all the useful commands:
```
pip help
```


- To find a package:
```
pip search Pandas # provides description of the package
```


- To find all the installed packages:
```
pip list
```


- To find if our package is the latest version of itself:
```
pip list -o
```


- To update a package 
```
pip install -U pandas
```


- To provide a set packages for a specific requirements:
```
pip freeze > requirements.txt
```


- To install packages from a specific file:
```
pip install -r r_test.txt
```
here -r stands for requirements and r_test.txt is the provide file with packages.


- Provides the outdated list of packages:
```
pip list --outdated
```


- To update the outdated versions:
```
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```

