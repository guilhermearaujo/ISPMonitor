#encoding: UTF-8

from os import system
from re import search
from datetime import datetime

import tweepy
import config

def main():
  try:
    write('Running SpeedTest')
    run_test()

    write('Parsing Results')
    results = parse_results()

    write('Authenticating')
    twitter = authenticate()

    write('Posting on Twitter')
    twitter.update_status(mount_status(results))
  except Exception as e:
    write(e.message, True)

def run_test():
  system('speedtest-cli --simple > results.log')

def parse_results():
  log        = open('results.log')

  ping       = get_value(log.readline())
  down_speed = get_value(log.readline())
  up_speed   = get_value(log.readline())

  log.close()

  return [
    ping,
    down_speed,
    down_speed * 100 / config.down_speed,
    up_speed,
    up_speed * 100 / config.up_speed
  ]

def get_value(line):
  return float(search('(\d+\.\d+)', line).group(0))

def authenticate():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_key, config.access_secret)
  return tweepy.API(auth)

def mount_status(results):
  return config.twitter_message % (
    results[1], # Download speed
    results[2], # Download percentage
    results[3], # Upload speed
    results[4], # Upload percentage
    results[0], # Ping
    final_message(results[2], results[4])
  )

def final_message(down, up):
  if down > 105 or up > 110: return config.messages['awesome']
  elif down > 95 and up > 95: return config.messages['great']
  elif down > 90 and up > 90: return config.messages['fair']
  elif down > 85 and up > 85: return config.messages['mediocre']
  elif down > 70 and up > 70: return config.messages['bad']
  elif down > 60 and up > 60: return config.messages['terrible']
  else: return config.messages['shit']

def write(text, log = False):
  message = '%s - %s' % (timestamp(), text)
  print(message)

  if log:
    with open('error.log', 'a') as file:
      file.write(message)

def timestamp():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

main()
