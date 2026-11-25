# Telegram weather bot

An early Python bot that turns OpenWeather forecast responses into Telegram weather messages for a fixed list of locations. `Main.py` is the entry point; the other scripts are historical image/text utilities.

## Run locally

Use Python 3.12 in an isolated virtual environment, then `pip install -r requirements.txt`. Export your own `TELEGRAM_BOT_TOKEN` and `OPENWEATHER_API_KEY` before running `python Main.py`. `.env.example` documents names; the program does not automatically load a dotenv file. Starting the bot makes real provider requests, so use a dedicated test bot and provider account.

## Offline checks

`python -m unittest discover -s tests -v`

These standard-library checks validate missing/blank environment values, redacted configuration errors and accidental literal credentials. They do not start polling, call weather services or establish current provider compatibility.

## Scope and limitations

This is historical learning work, not a maintained production weather service. Forecast formatting, fixed locations and external API responses need a separate end-to-end review before reuse. The current weather request uses HTTPS and a finite timeout. No hosted bot or uptime guarantee is claimed. See [SECURITY.md](SECURITY.md) for historical credential handling.

`1.1 update` retains an older extensionless source variant. It uses the same private environment configuration; the regression scan includes it.
