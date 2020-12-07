# Personal-Projects
A bunch of my personal projects! 

Languages:
- Python
- C#

Each folder will represent something else, and all will contain cool readmes about them!
Also, for more significant projects. They will have there own repo, these are marked in the readme below and can be found as such.

*Projects are sorted alphabetically*

*If your here as a 'portfolio' type of viewing,* [this](https://github.com/Skelmis/DPY-Anti-Spam)* can be considered my 'go to' piece of open source code.*

---

# Websites
I have created a few sites, not all of them open source. Here are the relevant links:

- [My Site](https://koldfusion.xyz/)
- [StudySupport's Site](https://studysupport.club/)
- [Team Fossil's Site](https://teamfossil.xyz/)

All of my sites start life as templates, since lets be honest, your wasting time for no reason. After that, I completely overhaul everything in order to turn them from staticly linked html files into full dynamic sites.
Generally speaking, this involves taking the static files, templating them ([see here](https://docs.djangoproject.com/en/3.1/topics/templates/)) and then building my [Django](https://www.djangoproject.com/) site around them before hosting them on either my mail server or other more generalised server that caters to dynamic sites.

All dynamic sites are hosted through a few layers, the foremost being [Nginx](https://www.nginx.com/) as a reverse proxy to deal with incoming connections and also force https redirects if required. Next up is a [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/index.html) which talks to the [Django](https://www.djangoproject.com/) site. Everything has valid ssl certs & forced redirects to https for what should be obvious reasons


# Table Of Contents

- [Apex Legends Monitor](#apex-legends-monitor)
- [Discord.py Anti-Spam](#discord-anti-spam) - External Repo
- [Discord.py Ticket Bot](#discord-ticket-bot) - External Repo
- [PyMcBot](#pymcbot) - External Repo
- [Team Fossil Website](#team-fossil-website)
- [Traffic Management Simulator](#traffic-management-simulator) - External Repo
- [License](#license)

---

## Apex Legends Monitor
A cool project devoted to teaching myself `pyautogui` and automating aspects of Apex Legends!

**Find the project [here!](https://github.com/Skelmis/Personal-Projects/tree/master/Apex%20Legends%20Monitor)**

---

## Discord Anti Spam
An under development package for Discord.py developers to use as an anti-spam feature suite in there bots.


**Find the project [here!](https://github.com/Skelmis/DPY-Ticket-Bot)**

---

## Discord Ticket Bot
A fully featured ticket bot coded using Discord.py
This bot features, logging of ticket contents & support for reactions as well as creating tickets via the standard command line.

**Find the project [here!](https://github.com/Skelmis/DPY-Anti-Spam)**

---
## PyMcBot
A discord bot built using `Discord.py` with the sole purpose of interacting with a MineCraft server from a client point of view, without the need to create an actual plugin.

**Find the project [here!](https://github.com/Skelmis/PyMcBot)**

---

## Team Fossil Website
A short, sharp website coded using `Django`
It was built with the intention of good vibes within our Apex Legends team and mainly just for a bit of fun.

**You can find the project [here!](https://github.com/Skelmis/Personal-Projects/tree/master/Team%20Fossil%20Website)**

---

## Traffic Management Simulator
A project devoted to fun times and creating a program to handle the efficient & safe control of traffic lights at a given intersection.
View the readme on the project itself for further information!

**You can find the project [here!](https://github.com/Skelmis/Traffic-Management-Simulator)**

---

## License

Most of these projects will follow different liecense, however, as a general rule of thumb. Always quote me (Skelmis) in your usage of my projects.
I.e `Original Source Obtained From Skelmis(https://github.com/Skelmis)`
