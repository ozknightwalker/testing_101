# Testing 101

contains total or four(4) branches that would demonstrate how to use:
* basic unittest
* testing with factory boy
* testing with mock
* testing with coverage

## instruction
1. install the requirements by
```
pip install -r requirements.txt
```
or you can just install
* django 1.8
* request
* factory_boy
* mock
2. switch to the branch that you want to explore by
```
	git checkout {name of the branch}
```
3. run the django test management command
```
	python manage.py test
```
* to run the coverage command in `step-4-coverage` branch run this command
```
	run_coverage
```



## basic unittest
a very basic tutorial on how to use/create a unittest, the setUps, and tearDowns.

## testing with factory boy
a very basic demo of how to turn a basic unittest to use factory boy

## testing with mock
a vary basic demo of how to use mock and why

## testing with coverage
just added a code how to generate coverage report based on the the command being executed


## Resources:
* [django 1.8 official testing documentation](https://docs.djangoproject.com/en/1.8/topics/testing/)
* [python httplib library](https://docs.python.org/2/library/httplib.html)
* [python requests library](http://docs.python-requests.org/en/master/)
* [mock](https://docs.python.org/3/library/unittest.mock.html)
* [Coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/)