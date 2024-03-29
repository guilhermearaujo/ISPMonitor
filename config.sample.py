import os

base_path = os.path.join(os.path.dirname(__file__), ".isp_monitor")

# Internet Speeds
down_speed = 100.0
up_speed = 20.0

# Twitter - Get your credentials at https://developer.twitter.com
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Tweet
provider = "@ClaroBrasil"
# provider = '@vivobr'
twitter_message = (
    "A {provider} está a ⬇ {down:.2f} Mbps e ⬆ {up:.2f} Mbps. {ping:.2f} ms "
    "de latência e estou conectado há {uptime}. "
    "Isso é {ratio:.2f}% do contratado. {reaction} {url}"
)

messages = dict(
    awesome="Mandou bem! 🏅🎉",
    great="Tá ótimo 🙂",
    fair="Tá justo",
    mediocre="Vamos melhorar isso, pessoal? 🙁",
    bad="Estou pagando por mais, viu? 💸",
    terrible="Tá de brincadeira? 👎",
    illegal="💩 Pode isso, @anatel_oficial?",
)

anatel = {
    "down_ratio": 0.4,
    "up_ratio": 0.4,
    "ping": 80,
    "online": 0.995,
}
