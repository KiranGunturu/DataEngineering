
# Pyspark Project Structure

Retail Analsis

	orders.csv
	customers.csv

Problem statment is:

	Find the Number of closed orders for each state

	1. Create orders dataframe
	2. Creat customers dataframe
	3. filter the orders dataframe based on order status
	4. do a group by on state and do the aggregation

--Configs

	--Application.conf
	--pyspark.conf
--lib 

	--ConfigReader.py
	--DataReader.py
	--DataManipulation.py
	--Utils.py
	--logger.py

--Data

	--orders.csv
	--customers.csv

--files under root of the project. \n 

	--Application_main.py
	--pipfile (packages with * - meaning latest version of the package)
	--pipfile.lock (exact version installed)
	--pytest.ini
	--test_retail_proj.py
	--log4j.properties
	--conftest.py






Install pipenv

```bash
pip install pipenv
```

Install Pyspark

```bash
pipenv install Pyspark
pipenv install pyspark=3.2.1
```
Activate Virtual Env

```bash
pipenv shell
```

pipfile will contain all the packages installed and their versions.

Pyspark unit testing:
======================

Unit testing: Pytest module

Install pytest
```bash
pipenv install pytest
```
Uninstall pytest

```bash
pipenv uninstall pytest
```

Install everything inside pipfile
```bash
pipenv install
```

now we have to create a new file where we can write unit tests

the filename where we write our unit test cases should either start with test or end with test
ex: test_retail_proj.py, retail_pron_test.py

function names inside test_retail_proj.py file must starts with test.

to run the unit test cases we need

```bash
python -m pytest
python -m pytest -v (verbose mode)
```
example result:

```python
test_retail_proj.py::test_read_customers_df PASSED                                                                                                                                                                 [ 50%]
test_retail_proj.py::test_read_orders_df PASSED 
```
Fixture:

setup (like spark session ) should be done as part of fixture and should not be going inside test case file .

fixture is to write setup code

order of the items:

setup - fixture
do unit testing - define unit tests
teardown - releasing the sources (stopping the spark session)

try writing your fixtures in a file names as conftest.py

List all available fixtures
```bash
python -m pytest --fixtures //to get list of available fixtures
```

markers: 

labeling test cases:


if we have 100 test cases, out of which 40 are related transformations and remaining 60 are aggregations
```bash
@pytest.mark.transformation()
@pytest.mark.aggregation()
```

```pyhton
@pytest.mark.transformation()
def test_filter_closed_orders_df(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_count = filter_closed_orders(orders_df).count()
    assert filtered_count == 7556
```
```bash
python -m pytest -v -m transformation
```

it will help us to run only test cases related to transformation when we want instead running all 100.

we should create one file called pytest.ini and keep info about markers to avoid warning when running.

```python
[pytest]
markers = 
    transformation: test the transformations
    slow: mark a test as slow
    latest: mark the latest ones
```

when we want to run all test cases except ones which are marked as transformation
```bash
python -m pytest -m "not transformation" -v
```

skip test:

if for any test case, work is still in progress and we want to avoid running that test case, we can do below

```bash
@pytest.mark.skip("work in progress")
```

```python
@pytest.mark.skip("work in progress")
def test_read_app_config():
    config = get_app_config("LOCAL")
    assert config["orders.file.path"] == "data/orders.csv"
```

Generic or Parameterize test cases:

```python
def test_check_closed_count(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_count = filter_orders_generic(orders_df, "CLOSED").count()
    assert filtered_count == 7556


@pytest.mark.skip()
def test_check_payment_pending_count(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_count = filter_orders_generic(orders_df, "PENDING_PAYMENT").count()
    assert filtered_count == 15030


@pytest.mark.skip()
def test_check_complete_count(spark):
    orders_df = read_orders(spark, "LOCAL")
    filtered_count = filter_orders_generic(orders_df, "COMPLETE").count()
    assert filtered_count == 22900
```
Instead of writing above three test cases, we can write one Generic one like below.

```python

@pytest.mark.parametrize(
    "status, count",
    [("CLOSED",7556),
     ("PENDING_PAYMENT",15030),
     ("COMPLETE",22900)
    ]
)
def test_check_count(spark, status, count):
    orders_df = read_orders(spark, "LOCAL")
    filtered_count = filter_orders_generic(orders_df, status).count()
    assert filtered_count == count

```

logging in pyspark
==================

we have seen print statements.
issue with print statements is that -
	1. we can't set the priorities or logging level like info, warn, error, fatal etc.
	2. we have written an application, 1000 print statements..
		we will have to manually comment all of those, or remove all of those.
	3. print statements make our application slower.

best way is to solve all these problems is to implement logging framework.

log4j is a logging framework.

spark internally uses log4j for its logging so we can reuse the same for our application level logs.

so we can get an instance of log4j object from spark session.

Utils.py (adding one extra config while we creating spark session)
log4j.properties (new file)
logger.py (new file)
application_main.py

==============
logging levels
debug, info, warn, error, fatal

debug is more like an verbose
fatal is more than an error like when something is terribly wrong.

if in our log4j.properties file, if we have defined logging level as info then info, warn, error, fatal messages will be displayed


===========
target location:

console
file

=============
message format





## Acknowledgements

s








    