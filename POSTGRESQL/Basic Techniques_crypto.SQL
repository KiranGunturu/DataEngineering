Danny Ma SQL
==============
1)

count(*) or count(1) - counts everything
count(col_name) - do not count null values

2)

!= and <> are same

3) - give quotes if we have two diff datatypes, spaces in column aliases

SELECT
  COUNT(*) AS "1record_count"
FROM trading.members
WHERE region = 'United States';

SELECT
  COUNT(*) AS "record count"
FROM trading.members
WHERE region = 'United States';

4) Date Filters

SELECT ticker as code, min(price) as min_price, max(price) as max_price
from trading.prices
--where market_date between '2020-12-31' AND '2020-01-01'
--where extract(YEAR FROM market_Date) = '2020'
where date_trunc('YEAR',market_date)='2020-01-01'
group by 1

between - small value should be left and large value should be right

==generate spread===

select 
  EXTRACT(YEAR FROM MARKET_DATE) AS CALENDER_YEAR,
  ticker,
  min(price) as min_price,
  max(price) as max_price,
  ROUND(avg(price)::Numeric,2) as avg_price,
  max(price) - min(price) as spread
  
from trading.prices
group by CALENDER_YEAR,ticker
order by CALENDER_YEAR,ticker

===MONTHLY AVG===

select DATE_TRUNC('MON',market_date) as month_start,
ticker,
ROUND(avg(price)::NUMERIC,2) as avg_monthly_price
from trading.prices
where market_date >= '2020-01-01'
group by month_start,ticker
order by ticker, month_start

===convert K and M to integers====

SELECT 
  market_date,
  price,
  volume,
  (CASE 
    WHEN RIGHT(volume,1) ='K' then LEFT(volume,length(volume)-1)::NUMERIC * 1000
    WHEN RIGHT(volume,1) ='M' then LEFT(volume,length(volume)-1)::NUMERIC * 1000000
    WHEN volume = '_' then 0
    END)::INTEGER AS adjusted_volume
FROM trading.prices
where ticker='ETH'
and market_date between '2021-08-01' and '2021-08-10'

===calculte breakout_days and non_breakout_days===

SELECT
  ticker,
  SUM(CASE WHEN price > open THEN 1 ELSE 0 END) AS breakout_days,
  SUM(CASE WHEN price <= open THEN 1 ELSE 0 END) AS non_breakout_days
FROM trading.prices
WHERE market_date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY ticker;

===calculte the quantity withheld ====

SELECT
  ticker,
  SUM(
    CASE
      WHEN txn_type = 'SELL' THEN -1 * quantity
      ELSE quantity
    END
  ) AS final_btc_holding
FROM trading.transactions
GROUP BY ticker;

=== top 5 volumes for each ticker====

with cte as (
SELECT 
  ticker,
  market_date,
  price,
  volume,
  rank() over(partition by ticker order by volume desc) as price_rank
from trading.prices
)
select *from cte
where price_rank<=5
order by ticker, price_rank


Window Functions vs Group By

To best understand what a window function is - we can compare it to the GROUP BY aggregates that we have previously used in this SQL Simplified course.

A window function is very similar to a GROUP BY aggregation - however, instead of returning just the unique values for the GROUP BY expressions in the final SQL output, a window function will return all the rows.

This is the key difference between the two - and it makes the window function particularly useful when you need to retain the original records of data, just like in this question!

Partition By and Group By
The PARTITION BY clause within the window function acts in the same way that the GROUP BY expressions work for aggregating data.

In this solution - we use PARTITION BY ticker which means that the RANK function is being applied within independent chunks of data with the same ticker value - just like a GROUP BY!

===== Calculate a 7 day rolling average for the price and volume columns in the trading.prices table for each ticker.====

WITH cte_adjusted_prices AS (
SELECT
  ticker,
  market_date,
  price,
  CASE
    WHEN RIGHT(volume, 1) = 'K' THEN LEFT(volume, LENGTH(volume)-1)::NUMERIC * 1000
    WHEN RIGHT(volume, 1) = 'M' THEN LEFT(volume, LENGTH(volume)-1)::NUMERIC * 1000000
    WHEN volume = '-' THEN 0
  END AS volume
FROM trading.prices
),
cte_moving_averages AS (
  SELECT
    ticker,
    market_date,
    price,
    AVG(price) OVER (
      PARTITION BY ticker
      ORDER BY market_date
      RANGE BETWEEN '7 DAYS' PRECEDING AND CURRENT ROW
    ) AS moving_avg_price,
    volume,
    AVG(volume) OVER (
      PARTITION BY ticker
      ORDER BY market_date
      RANGE BETWEEN '7 DAYS' PRECEDING AND CURRENT ROW
    ) AS moving_avg_volume
  FROM cte_adjusted_prices
)
-- final output
SELECT * FROM cte_moving_averages
WHERE market_date BETWEEN '2021-08-01' AND '2021-08-10'
ORDER BY ticker, market_date;


====Calculate the monthly cumulative volume traded for each ticker in 2020=====

WITH cte_monthly_volume AS (
  SELECT
    ticker,
    DATE_TRUNC('MON', market_date)::DATE AS month_start,
    SUM(
      CASE
      WHEN RIGHT(volume, 1) = 'K' THEN LEFT(volume, LENGTH(volume)-1)::NUMERIC * 1000
      WHEN RIGHT(volume, 1) = 'M' THEN LEFT(volume, LENGTH(volume)-1)::NUMERIC * 1000000
      WHEN volume = '-' THEN 0
    END
  ) AS monthly_volume
  FROM trading.prices
  WHERE market_date BETWEEN '2020-01-01' AND '2020-12-31'
  GROUP BY ticker, month_start
)
-- final output
SELECT
  ticker,
  month_start,
  SUM(monthly_volume) OVER (
    PARTITION BY ticker
    ORDER BY month_start
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_monthly_volume
FROM cte_monthly_volume
ORDER BY ticker, month_start;

==================================================================================================
Calculate the daily percentage change in volume for each ticker in the trading.prices table

Percentage change can be calculated as (current - previous) / previous
Multiply the percentage by 100 and round the value to 2 decimal places
Return data for the first 10 days of August 2021
===================================================================================================

WITH cte_adjusted_prices AS (
  SELECT
    ticker,
    market_date,
    CASE
      WHEN RIGHT(volume, 1) = 'K' THEN LEFT(volume, LENGTH(volume)-1)::NUMERIC * 1000
      WHEN RIGHT(volume, 1) = 'M' THEN LEFT(volume, LENGTH(volume)-1)::NUMERIC * 1000000
      WHEN volume = '-' THEN 0
    END AS volume
  FROM trading.prices
),
cte_previous_volume AS (
  SELECT
    ticker,
    market_date,
    volume,
    LAG(volume) OVER (
      PARTITION BY ticker
      ORDER BY market_date
    ) AS previous_volume
  FROM cte_adjusted_prices
  -- need to remove the single outlier record!
  WHERE volume != 0
)
-- final output
SELECT
  ticker,
  market_date,
  volume,
  previous_volume,
  ROUND(
    100 * (volume - previous_volume) / previous_volume,
    2
  ) AS daily_change
FROM cte_previous_volume
WHERE market_date BETWEEN '2021-08-01' AND '2021-08-10'
ORDER BY ticker, market_date;

===================================================================================================================================================
Which top 3 mentors have the most Bitcoin quantity? Return the first_name of the mentors and sort the output from highest to lowest total_quantity
====================================================================================================================================================

SELECT
  members.first_name,
  SUM(
    CASE
      WHEN transactions.txn_type = 'BUY'  THEN transactions.quantity
      WHEN transactions.txn_type = 'SELL' THEN -transactions.quantity
    END
  ) AS total_quantity
FROM trading.transactions
INNER JOIN trading.members
  ON transactions.member_id = members.member_id
WHERE transactions.ticker = 'BTC'
GROUP BY members.first_name
ORDER BY total_quantity DESC
LIMIT 3;

===============================================================================================================
Show the market_date values which have less than 5 transactions? Sort the output in reverse chronological order.
================================================================================================================

SELECT
  prices.market_date,
  COUNT(transactions.txn_id) AS transaction_count
FROM trading.prices
LEFT JOIN trading.transactions
  ON prices.market_date = transactions.txn_date
  AND prices.ticker = transactions.ticker
GROUP BY prices.market_date
HAVING COUNT(transactions.txn_id) < 5
ORDER BY prices.market_date DESC;