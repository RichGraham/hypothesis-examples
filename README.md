# Hypothesis Examples
Examples of property-based testing in python. See Pragmatic Programmer p.224

## Basic operation
Run the following to access and create some current working examples in a Jupyter notebook

	ipyth WorkingExamples.ipynb

See also the test for more extensive examples

## Tests
**Warning** do not edit Test.py directly - use the Jupyter notebook approach below
### Simple run

	./runTests.sh
### In Jupyter
Run the following to access and edit tests in a Jupyter notebook

	ipyth Tests.ipynb
Run all cells or edit/create new tests

### Export from Jupyter
To update the Test.py file from the Jupyter note book run

	./createAndRunTests.sh

**Remeber to save the notebook first** 

### Coverage tests
To generate a report on code coverage by the tests run

	./coverageTest.sh 
