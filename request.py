# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:22:59 2023

@author: hp
"""


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())