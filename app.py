from flask import Flask, jsonify, render_template,request 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route(('/home'))
def home():    
    return render_template("index.html")

@app.route(("/result"),methods = ['POST','GET'])
def result():   
    
    output = request.form.to_dict()
    name = int(output["name"])
    arg1 = int(output["arg1"])
    arg2 = int(output["arg2"])
    ans = arg1*arg2
    anss = str(ans)
    return render_template("index.html",name = anss)    

@app.route(("/equ"),methods = ['POST','GET'])
def equ():   
    import random
    import numpy as np

    output = request.form.to_dict()
    arg0 = int(output["arg0"])
    arg1 = int(output["arg1"])
    arg2 = int(output["arg2"])
    arg3 = int(output["arg3"])
    arg4 = float(output["arg4"])
    loop=0
    max_tokens_per_person = 15
    max_token = arg0
    avgW=[]
    prob_card = arg4
    metro_capacity = 200
    metro_per_hour = arg3
    refresh = arg1
    arrival_rate = 60/metro_per_hour
    

    tokens_available = max_token
    number_of_entry_gates =4
    number_of_token_counter= 2
    token_left = 0
    arrived_num = arg2
    hours=2
    num_train_in_whole_day = metro_per_hour*hours
    anss=""
    capacity=200
    time=0
    gg = capacity
    while capacity < (gg+1 ): 
        token_left = max_token
        waiting =[]
        waiting.append(0)
        widx=1
        for i in range(1,10): 
            time += arrival_rate
            if(time%refresh == 0) :
                token_left = max_token 
            cap = capacity # current train has this capacity 
            seated=0 #train empy aayi h

            prev = waiting[widx-1] # fetching the details of previous number of people waiting on platform before arrival of next train
            arrival_left = arrived_num # number of people who arrived now on platform  so total peeps are prev + arrival_left
            while (cap>0 and arrival_left>0 and seated<=arrived_num):
            
                if(prev>0 ):
                    r = random.uniform(0,1)
                    if r<prob_card: 
                        type = "card"
                        if(cap<0 or seated>arrived_num) :
                            break
                        cap-=1
                        seated+=1
                
                    else :
                        type = "token"
                    
                        token_needed = random.randint(1,10)

                        
                        if(cap<0 or seated>arrived_num) :
                            break
                        if(token_left<=0):
                            continue
                        seated+= token_needed
                        prev= max(0, prev-token_needed)
                        token_left -= token_needed
                else:
                    r = random.uniform(0,1)
                    if r<prob_card: 
                        type="card"
                        if(cap<0): 
                            break
                        cap-=1
                        arrival_left -= 1
                        seated+=1
                    else:
                        type = "token"
                        token_needed = random.randint(1,10)
                        if(cap<0) :
                            break
                        if(token_left<=0):
                            continue
                        seated+= token_needed
                        prev = max(0, prev-token_needed)
                        token_left -= token_needed
                        cap=max(0,cap-token_needed)
                # print(seated)
            wait = max(0, waiting[widx-1]+arrived_num-seated )
            
            waiting.append(wait)
            widx+=1
            
            meanWait = np.mean(waiting)
            avgW.append(meanWait)
        meanOfmeanWait = np.mean(avgW)
        ans=""
        anss+="\nmax_tokens_per_person: "+str(max_tokens_per_person)
        anss+="\nmax_token availble in both counters and machine: "+str(max_token)
        anss+="\nProbability that the person arrived is using metro card: "+str(prob_card)
        anss+="\nmetro_capacity: "+str(metro_capacity)
        anss+="\nmetro_per_hour: "+str(metro_per_hour)
        anss+="\nRefreshing time for delhi metro token: "+str(refresh)
        anss+="\nArrival rate of metro per hour: "+str(arrival_rate)
        anss+="\nAverage number of people entered after the arrival of last mertro: "+str(arrived_num)
        anss+="\nHours for which this simulation was run: "
        anss+="\n "
        anss += "Average number of people waiting for next train is: "+str(int(meanOfmeanWait))+"\nTrain capacity is: "+str(int(capacity))
        # print("number of people waiting for next train: ", meanOfmeanWait," when capacity is: ",capacity)
        # print()
        # print("loop is ",loop)
        # loop+=1
        capacity += 50
    
    return render_template("index.html",name = anss)        

# for button submit by changing capacity of metro from 50 to 500
@app.route(("/equ2"),methods = ['POST','GET'])
def equ2():   
    import random
    import numpy as np

    output = request.form.to_dict()
    arg0 = int(output["arg0"])
    arg1 = int(output["arg1"])
    arg2 = int(output["arg2"])
    arg3 = int(output["arg3"])
    arg4 = float(output["arg4"])
    loop=0
    max_tokens_per_person = 15
    max_token = arg0
    avgW=[]
    prob_card = arg4
    metro_capacity = 200
    metro_per_hour = arg3
    refresh = arg1
    arrival_rate = 60/metro_per_hour
    

    tokens_available = max_token
    number_of_entry_gates =4
    number_of_token_counter= 2
    token_left = 0
    arrived_num = arg2
    hours=2
    num_train_in_whole_day = metro_per_hour*hours
    anss=""
    capacity=200
    time=0
    while capacity < (2*arrived_num ): 
        token_left = max_token
        waiting =[]
        waiting.append(0)
        widx=1
        for i in range(1,10): 
            time += arrival_rate
            if(time%refresh == 0) :
                token_left = max_token 
            cap = capacity # current train has this capacity 
            seated=0 #train empy aayi h

            prev = waiting[widx-1] # fetching the details of previous number of people waiting on platform before arrival of next train
            arrival_left = arrived_num # number of people who arrived now on platform  so total peeps are prev + arrival_left
            while (cap>0 and arrival_left>0 and seated<=arrived_num):
            
                if(prev>0 ):
                    r = random.uniform(0,1)
                    if r<prob_card: 
                        type = "card"
                        if(cap<0 or seated>arrived_num) :
                            break
                        cap-=1
                        seated+=1
                
                    else :
                        type = "token"
                    
                        token_needed = random.randint(1,10)

                        
                        if(cap<0 or seated>arrived_num) :
                            break
                        if(token_left<=0):
                            continue
                        seated+= token_needed
                        prev= max(0, prev-token_needed)
                        token_left -= token_needed
                else:
                    r = random.uniform(0,1)
                    if r<prob_card: 
                        type="card"
                        if(cap<0): 
                            break
                        cap-=1
                        arrival_left -= 1
                        seated+=1
                    else:
                        type = "token"
                        token_needed = random.randint(1,10)
                        if(cap<0) :
                            break
                        if(token_left<=0):
                            continue
                        seated+= token_needed
                        prev = max(0, prev-token_needed)
                        token_left -= token_needed
                        cap=max(0,cap-token_needed)
                # print(seated)
            wait = max(0, waiting[widx-1]+arrived_num-seated )
            
            waiting.append(wait)
            widx+=1
            
            meanWait = np.mean(waiting)
            avgW.append(meanWait)
        meanOfmeanWait = np.mean(avgW)
        # print("number of people waiting for next train: ", meanOfmeanWait," when capacity is: ",capacity)
        # print()
        print("loop is ",loop)
        loop+=1
        anss += "\nAverage number of people waiting for next train is: "+str(int(meanOfmeanWait))+"\nTrain capacity is: "+str(int(capacity))+"\nMax_token_Available before renewal: "+str(int(max_token))+"\n"
        print(anss)
        capacity += 50
    
    return render_template("index.html",name = anss)        


if __name__ == "__main__":
    app.run(debug=True)