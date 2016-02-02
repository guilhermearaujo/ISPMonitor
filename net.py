#encoding: UTF-8

import os
import re
import tweepy
import config

def main():
  run_test()
  results = parse_results()
  twitter = authenticate()
  twitter.update_status(mount_status(results))

def run_test():
  os.system('speedtest-cli --simple > net.log')

def parse_results():
  log        = open('net.log')

  ping       = get_value(log.readline())
  down_speed = get_value(log.readline())
  up_speed   = get_value(log.readline())

  return [ping, down_speed, down_speed * 100 / config.down_speed, up_speed, up_speed * 100 / config.up_speed]

def get_value(line):
  return float(re.search('(\d+\.\d+)', line).group(0))

def authenticate():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_key, config.access_secret)
  return tweepy.API(auth)

def mount_status(results):
  return 'A @NEToficial está funcionando a %.2f Mbps (%.2f%%) de download e %.2f Mbps (%.2f%%) de upload. A latência é de %.2f ms\n%s' % (
    results[1], results[2], results[3], results[4], results[0], final_message(results[2], results[4])
  )

def final_message(down, up):
  if down > 105 or up > 110:
    return 'Mandou bem!'

  elif down > 95 and up > 95:
    return 'Tá ótimo :)'

  elif down > 90 and up > 90:
    return 'Tá justo'

  elif down > 85 and up > 85:
    return 'Vamos melhorar isso, pessoal?'

  elif down > 70 and up > 70:
    return 'Estou pagando por mais, viu?'

  elif down > 60 and up > 60:
    return 'Tá de brincadeira?'

  else:
    return 'Pode isso, @Anatel_Informa?'

main()
