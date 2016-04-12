README.txt

Basic requirements and approach

Requirement 1
Given a stock and a price calculate div. yield

Test for this :-

test case i) select a valid stock and a price, call interface, validate that success is reported and correct value returned.
test case ii) select an invalid stock and a price, call interface, validate that failure is reported.

Requirement 2
Given stock and price calculate P/E ratio

Test for this :-

test case i) select a valid stock and a price, call interface, validate that success is reported and correct value returned.
test case ii) select an invalid stock and a price, call interface, validate that failure is reported.

Requirement 3
Record a trade for a given stock with timestamp, quantity, b/s and price

Test for this :-

test case i) create a trade report for a valid stock, timestamp, price etc. and call interface verify that success is reported.
test case ii) create trade for invalid stock etc. call interface, validate that failure is reported.

Requirement 4
Calculate VWAP for a stock for trades *in last 5 minutes*.

Test for this :-

test case i) submit a number of trades (req 3) ensure that VWAP is as expected.
test case ii) test for invalid stock

Requirement 5
Calculate all share index

Test for this :-

test case 1) submit a number of trades for different stocks (req 3), verify that correct index is calculated.

*** First submit with some basic tests working

*** Refactored class hierarchy slightly

*** Next, adding trade recording and starting calculation of VWSP

Was going to create a mock datetime when testing trade recording, but decided to avoid them - I think they can end up hiding bugs.

*** Added calculation of VWSP and all share index value. A little more refactoring. Still need to add some more rigorous tests.

