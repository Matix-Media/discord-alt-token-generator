# discord-alt-token-generator

Alt-token generator for discord (slow)

## Info

The creator and publisher of this bot is not responsible for any kind of damage or anything else. Use of the bot is at your own risk and the creator is not responsible for bans from the Discord network.

We recommend using a VPN when using the bot.

# Usage under Windows (CMD)

First you have to active the virutal enviroment wich contains packages and a python copy. To do this, just navigate to the main folder of the scripts and type the follwing line into your command prompt

`> venv\Scripts\activate`

Now there should be a `(venv)` infront of your current folder in the command prompt.  
Someting like this: `(venv) C:\Users\user\Documents\Python\Documents\discord alt token generator>`

To run the generator now, just go to the help, for all infos you need.

`> generator.py help`

It should tell you something like this

```
:: HELP ::
$ generator.py <number of alt-tokens to generate> <your windows username> [register delay (seconds) | default: 30] [save userdata |default: false] [tokens file name (Without extension) | default: t_<timecode>] [invite to server | default: empty] [channel url | default: empty]

:: INFO ::
For this generator, you need to have Chrome installed on this machine. Then you need to go to https://chromedriver.chromium.org/downloads and download the version of chromedriver according to your installed version of Chrome and put chromedriver.exe in the same folder with this script.

You can add a invite link to a server at the end where the bot should join and write a random message. This can be used to bypass discord's bot detection.

The channel URL is the url to the channel where a message should be written to.

Your windows username is required to get your Chrome config to bypass recaptcha.

The alt-tokens get saved into the tokens folder

```

# Usage under MacOS

First you have to active the virutal enviroment wich contains packages and a python copy. To do this, just navigate to the main folder of the scripts and type the follwing line into your command prompt

`> source venv/bin/activate`

Now there should be a `(venv)` infront of your current folder in the command prompt.  
Someting like this: `(venv) macbook-user: discord alt token generator$`

To run the generator now, just go to the help, for all infos you need.

`> py generator.py help`

It should tell you something like this

```
:: HELP ::
$ generator.py <number of alt-tokens to generate> <your windows username> [register delay (seconds) | default: 30] [save userdata |default: false] [tokens file name (Without extension) | default: t_<timecode>] [invite to server | default: empty] [channel url | default: empty]

:: INFO ::
For this generator, you need to have Chrome installed on this machine. Then you need to go to https://chromedriver.chromium.org/downloads and download the version of chromedriver according to your installed version of Chrome and put chromedriver.exe in the same folder with this script.

You can add a invite link to a server at the end where the bot should join and write a random message. This can be used to bypass discord's bot detection.

The channel URL is the url to the channel where a message should be written to.

Your windows username is required to get your Chrome config to bypass recaptcha.

The alt-tokens get saved into the tokens folder
```
