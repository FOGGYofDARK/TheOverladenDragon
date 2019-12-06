# -*- coding:utf-8 -*-


import os
files = os.listdir()
old_text = "authoritarianis = 12"
new_text = "authoritarianism = 12"
while d < len(files):
    '''if (files[d])[-3:] == 'txt':
        with open(files[d],'r',encoding = 'utf-8-sig') as f1:
            text = f1.read()
            i = 0
            while i < len(text):
                if text[i:i+12] == "set_politics":
                    break
                i = i+1
            if i == len(text):
                d = d + 1
                continue
            while i < len(text):
                if text[i] == '{':
                    break
                i = i+1
            start = i+2
            while i < len(text):
                if text[i] == '}':
                    break
                i = i+1
            end = i

            part1 = text[0:start]
            part2 = text[end:]
            pop = "\truling_party = socialism\n\tlast_election = \"1888.15.6\"\n\telection_frequency = 48\n\telections_allowed = no\n"
        with open(files[d],'w',encoding = 'utf-8-sig') as f1:
            f1.write(part1+pop+part2)'''
    if (files[d])[-3:] == 'txt':
        with open(files[d],'r',encoding = 'utf-8-sig') as f1:
            text = f1.read()
        with open(files[d],'a',encoding = 'utf-8-sig') as f1:
            f1.write(text.replace(old_text,new_text))
    d = d + 1
