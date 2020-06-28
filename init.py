#!/usr/bin/env python
# -*- coding: utf-8 -*-
import request 
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

doc = [{
    'level':'★★★★★',
    'title':'neck',
    'body':'목 타투의 고통비유는 그냥 죽었다고 생각하면 편하다 굳이 목에 타투를 하고싶다면 제갈을 물고 손을 결박시킨다음에 시술를 진행하자!'},
    {
    'level':'★★★★★',
    'title':'frontneck',
    'body':'목 타투의 고통비유는 그냥 죽었다고 생각하면 편하다(목앞, 목뒤, 목옆 다똑같다) 굳이 목에 타투를 하고싶다면 제갈을 물고 손을 결박시킨다음에 시술를 진행하자!'},

    {
    'level':'★★',
    'title':'Shoulder',
    'body':'어꺠 타투의 경우 대중적인 부위중에 하나이며, 성별을 떠나서 많은 분들이 시술을 하는부위다'},
    
    {
    'level':'★★★★★',
    'title':'Rip',
    'body':'갈비뼈 타투의 고통비유는 타투이스트에게 죽여달라고 애원을 한다는 소문이있다 은밀하다고 생각하는 부이에 타투를 하고싶은 분들이 많이 선호하시는 부위이며, 수술및 흉터가 있으신 분들이 커버업으로 많이 시술하는 부위다'},    
     {
    'level':'★★★★★',
    'title':'Stomach',
    'body':'갈비뼈 타투보다는 덜 아프다고하지만 아픈건 매한가지 복부타투는 개인적으로 생각하기엔 흉터나 수술자국 커버업용으로 많이 작업하며, 단점은 복무에 살이찌거나 빠졌을때 타투의 형대가 무조건 변한다'},   
     {
    'level':'★★',
    'title':'Arm',
    'body':'바깥팔 타투는 그나마 참을만하지만, 팔꿈치나 팔이 접히는부위는 진짜 굉장히 아프다 진짜 또한, 바깥팔 타투의 경우 대중적인 부위중에 하나이며, 성벼을 떠나서 많은분들이 시술을 하는부위다'},   
     {
    'level':'★★★★★',
    'title':'Hip',
    'body':'엉덩이 타투도 최고 아픈부위로 손꼽힌다 왜하는지 잘모르겠다 서양에서는 여성분들이 그나마 많이하는거같다'},   
     {
    'level':'★★★★',
    'title':'Wrist',
    'body':'설명하는 부위중에 가장대중적으로 많이하는 곳 하지만 손목안쪽!! 주름은 진짜 면탈로 상처를 계속 내는 느낌이라 많이 아프다'},   
     {
    'level':'★★★★',
    'title':'Finger',
    'body':'시술시 손가락 마디마디모다가 아프다 손목타투와 마찬가지로 많이하는 부위중 한곳 간혹, 안아프다고 하는사람이있다'},   
     {
    'level':'★★★★★',
    'title':'back to the knee',
    'body':'무릎뒤 타투 고통은 신경이 있는 부위를 계속 카롤 긋는 느낌이다 진짜아프다 무릎앞뒤로 굉장히 아파서 울었다고하는 사람을 들었다'},   
     {
    'level':'★★',
    'title':'Calf',
    'body':'종아리 타투의 고통비유는 토치ㅔ 그을리는 정도 어꺠와 마찬가지로 그나마 참을만하다 부위가 크다보니 타투매니아들이 많이 하는 부위'}
]

db.tattoos.insert_many (doc)





    
    