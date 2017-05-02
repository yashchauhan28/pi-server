set_alram = ['wake','set','alert','put','establish','adjust','schedule','activate','create','arrange','assign','put','publish','make']
del_alarm = ['delete','cancel','remove','unpublish','eradicate','cut','erase','kill','wipe','off','shut']
sessions = {'morning':'after 12 am',
            'noon':'12 pm',
            'evening':'after 12 pm',
            'midnight':'12 am',
            'night':'after 7 pm'}
phrases = ['minutes','half','quater','past','to','minute']

def getMessage():
    #return str(raw_input().replace(":"," ").split())
    _message = []
    _message.append("wake me up at 6:35 am")
    _message.append("make alarm for 8 past 3")
    _message.append("set alram for 6 in the morning")
    return _message

def extractAlarmWord(sentence):
    for word in sentence:
        word = word.strip()
        if word in set_alram:
            return str("set_alram_requested")
        if word in del_alarm:
            return str("del_alarm_requested")

def adjust_sentence(sentence):
    for i in range(len(sentence)):
        if(sentence[i]=="past"):
            if sentence[i-1]!="minutes":
                sentence.insert(i,"minutes")
        if sentence[i]=="to" :
            if sentence[i-1]!="minutes":
                sentence.insert(i,"minutes")

def extractTime(sentence):
    adjust = 0
    adjust_sentence(sentence)
    print "adjusted sentence" , sentence
    _time_true = False
    _time_time = ""
    for word in sentence:
        word = word.strip()
        #print "word is ",word
        if word == "am":
            _time_time="am"
            _time_true = True
        elif word == "pm":
            _time_time="pm"
            _time_true = True
        elif word == "morning" or word == "midnight":
            _time_time="am"
            _time_true = True
        elif word == "evening" or word == "night" or word =="noon":
            _time_time="pm"
            _time_true = True
    if _time_true == False:
        with open("memory.txt","w") as fs:
            fs.write(' '.join(sentence))
        return "am or pm ??"
    for i in range(len(sentence)):
        word = sentence[i].strip()
        try:
            _time = int(word.strip())
            if _time >=0 and _time<=9 and i+1<len(sentence):
                try:
                    _time_minute = int(sentence[i+1])
                    return str(_time) + ":" +str(_time_minute) + _time_time
                except Exception as e:
                    return str(_time) + ":00" + _time_time
        except Exception as e:
            pass
        if word in phrases:
            _time_minute = 0
            _time_hour = 0
            next_word = sentence[i+1].strip()
            forward_word = sentence[i+2].strip()
            if next_word == "to":
                adjsut = -1
            if next_word == "past":
                adjust = 1
            if word == "half":
                _time_minute = "30"
            if word == "quater":
                _time_minute = "15"
            if word == "minutes" or word == "minute":
                _time_minute = sentence[i-1].strip()
                if adjust == -1:
                    _time_minute = str(60-int(_time_minute))
            _time_hour = forward_word
            if adjust == -1:
                _time_hour = str(int(_time_hour)-1)
            return str(_time_hour) + ":" + str(_time_minute) + _time_time

def executeParser(text):
    #_message=getMessage()
    # for message in _message:
    #     st = message.replace(":"," ").split()
    #     requested_command = extractAlarmWord(st)
    #     requested_time = extractTime(st)
    #     if requested_time == "am or pm ??":
    #         send(requested_time)
    #     print requested_command
    #     print requested_time
    st = text.replace(":"," ").split()
    requested_command = extractAlarmWord(st)
    requested_time = extractTime(st)
    if requested_time == "am or pm ??":
        return "am or pm ??"
    return "alram set for time " + requested_time
