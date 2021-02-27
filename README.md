# Fluxo OFX Parser

Python parser that converts Open Financial Exchange (OFX) to python objects. This is a fork of [OFXParser](https://pypi.org/project/ofxparse/) with some fixes that allows handling encoding and malformed OFX.

The API is the same than forked library, with some extras:
- `OfxParserException` is a base exception for all possible OFX Errors
- `EmptyOFXException` raises an exception when trying to retreive an empty OFX
- `EmptyTransactionNameException` raises an exception when trying to retreive an OFX without transactions
- `InvalidTransactionDateException` raises an exception when trying to retreive an OFX without transaction date on its transactions
- `NoTransactionAmountException` raises an exception when trying to retreive an OFX without transaction amount on its transactions

## Original Readme from upstream


ofxparse
========

ofxparse is a parser for Open Financial Exchange (.ofx) format files.  OFX
files are available from almost any online banking site, so they work well
if you want to pull together your finances from multiple sources.  Online
trading accounts also provide account statements in OFX files.

There are three different types of OFX files, called BankAccount,
CreditAccount and InvestmentAccount files.  This library has been tested with
real-world samples of all three types.  If you find a file that does not work
with this library, please consider contributing the file so ofxparse can be
improved.  See the Help! section below for directions on how to do this.

Example Usage
=============

Here's a sample program

.. code:: python

  from ofxparse import OfxParser
  with codecs.open('file.ofx') as fileobj:
      ofx = OfxParser.parse(fileobj)
  
  # The OFX object
  
  ofx.account               # An Account object

  # AccountType
  # (Unknown, Bank, CreditCard, Investment)

  # Account
  
  account = ofx.account 
  account.account_id        # The account number
  account.number            # The account number (deprecated -- returns account_id)
  account.routing_number    # The bank routing number
  account.branch_id         # Transit ID / branch number
  account.type              # An AccountType object
  account.statement         # A Statement object
  account.institution       # An Institution object

  # InvestmentAccount(Account)

  account.brokerid          # Investment broker ID
  account.statement         # An InvestmentStatement object

  # Institution
  
  institution = account.institution
  institution.organization
  institution.fid
    
  # Statement
  
  statement = account.statement
  statement.start_date          # The start date of the transactions
  statement.end_date            # The end date of the transactions
  statement.balance             # The money in the account as of the statement date
  statement.available_balance   # The money available from the account as of the statement date
  statement.transactions        # A list of Transaction objects

  # InvestmentStatement

  statement = account.statement  
  statement.positions           # A list of Position objects
  statement.transactions        # A list of InvestmentTransaction objects

  # Transaction
  
  for transaction in statement.transactions:
    transaction.payee
    transaction.type
    transaction.date
    transaction.user_date
    transaction.amount
    transaction.id
    transaction.memo
    transaction.sic
    transaction.mcc
    transaction.checknum

  # InvestmentTransaction
  
  for transaction in statement.transactions:
    transaction.type
    transaction.tradeDate
    transaction.settleDate
    transaction.memo
    transaction.security      # A Security object
    transaction.income_type
    transaction.units
    transaction.unit_price
    transaction.comission
    transaction.fees
    transaction.total
    transaction.tferaction

  # Positions
  
  for position in statement.positions:
    position.security       # A Security object
    position.units
    position.unit_price
    position.market_value

  # Security
  
  security = transaction.security
  # or
  security = position.security
  security.uniqueid
  security.name
  security.ticker
  security.memo
  

Help!
=====

Sample ``.ofx`` and ``.qfx`` files are very useful.  If you want to help us out,
please edit all identifying information from the file and then email it to
jseutter dot ofxparse at gmail dot com.

Development
===========

Prerequisites::
  # Ubuntu
  sudo apt-get install python-beautifulsoup python-nose python-coverage-test-runner
  # Python 3 (pip)
  pip install BeautifulSoup4 six lxml nose coverage
  # Python 2 (pip)
  pip install BeautifulSoup six nose coverage

The `six` package is required for python 2.X compatibility

Tests:
Simply running the ``nosetests`` command should run the tests.

.. code:: bash

  nosetests

If you don't have nose installed, the following might also work:

.. code:: bash

  python -m unittest tests.test_parse

Test Coverage Report:

.. code:: bash

  coverage run -m unittest tests.test_parse
  
  # text report
  coverage report

  # html report
  coverage html
  firefox htmlcov/index.html


Homepage
========
| Homepage: https://sites.google.com/site/ofxparse
| Source: https://github.com/jseutter/ofxparse

License
=======

ofxparse is released under an MIT license.  See the LICENSE file for the actual
license text.  The basic idea is that if you can use Python to do what you are
doing, you can also use this library.
