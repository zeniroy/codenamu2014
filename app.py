# -*- coding: utf-8 -*-

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

from home import get_names

@app.route("/")
def home():
    return render_template('home.html', id_names=get_names())

@app.route("/favicon.ico")
def favicon():
	return "";

@app.route("/<member_num>")
def member(member_num):
	f = open('19th members.json', 'r')
	datas = json.load(f)
	if len(datas) <= int(member_num):
		return "wrong member id"

	data = datas[int(member_num)]
	data['yea'] = len([vote for vote in data['votes'] if vote['option'] == 'yea'])
	data['nay'] = len([vote for vote in data['votes'] if vote['option'] == 'nay'])
	data['forfeit'] = len([vote for vote in data['votes'] if vote['option'] == 'forfeit'])
	data['attend'] = len([attend for attend in data['attendance'] if attend])
	data['absent'] = len([attend for attend in data['attendance'] if not attend])
	return render_template('person.html',data=data)

if __name__ == "__main__":
	app.run(debug=True)
