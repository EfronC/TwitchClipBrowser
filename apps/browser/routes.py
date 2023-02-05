# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.browser import blueprint
from flask import render_template, request, jsonify, redirect
#from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.browser.views import *
import json
from apps import init_twitch

@blueprint.route('/api/game/games/', methods=('GET', ))
async def get_games_dashboard():
    twitch, auth = await init_twitch()
    games = await get_games(twitch)
    return render_template('browser/dashboard.html', data={"success":True})

@blueprint.route('/api/clip/clips/', methods=('GET', ))
async def get_clips_dashboard():
    twitch, auth = await init_twitch()
    users = await get_users(twitch)
    clips = await get_clips(twitch)
    print(clips)
    return render_template('browser/dashboard.html', data={"success":True, "clips": clips})

@blueprint.route('/api/oauth/success/', methods=('GET', ))
async def sucess_get():
    twitch, auth = await init_twitch(True)
    code = request.args.get("code", False)
    if code:
        token, refresh_token = await auth.authenticate(user_token=code)
        print("Token: ", token)
        print("Refresh: ", refresh_token)
        return render_template('browser/dashboard.html', data={"success":True, "token": token, "refresh":refresh_token})
    else:
        return render_template('browser/dashboard.html', data={"success":False})
    

@blueprint.route('/api/login/twitch/', methods=('GET',))
async def login_t():
    twitch, auth = await init_twitch(True)
    url = auth.return_auth_url()
    print(url)
    return redirect(url, code=302)
