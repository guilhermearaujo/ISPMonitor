# ISP Monitor
_As seen on http://www.twitter.com/anethoje_

ISP Monitor monitors your Internet speeds and reports the results to your Twitter account.

# Dependencies
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* [tweepy](https://github.com/tweepy/tweepy)
* Requires a [Twitter Developer account](http://dev.twitter.com)

# Installing
1. Clone this repo: `$ git clone git@github.com:guilhermearaujo/ISPMonitor.git`
2. Install dependencies with `pip install -r requirements.txt`
3. Add your Twitter Credentials and Internet speeds to `config.py` (hint: there's a `config.py.sample`!)
4. Schedule the script using `cron`:
  `$ crontab -e`
  Add the line:
  `0 */1 * * * python /path/to/script/net.py`

# Running

You can use dinamic download/upload speeds by setting `ISP_DOWN_SPEED` and `ISP_UP_SPEED` as environment
variable or setting when calling the script, as:

`ISP_DOWN_SPEED=30 ISP_UP_SPEED=3 python net.py`

# Using
Wait and check your Twitter account periodically.

# License

Action Button is released under the WFTPL license. See LICENSE for details.
