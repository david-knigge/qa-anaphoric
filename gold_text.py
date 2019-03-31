tfirst = ["uk","""Nearly three years since the United Kingdom voted to leave the European Union, British politicians are still arguing over how, when or even if the world's fifth largest economy should leave the bloc it first joined1973. When May set the March 29 exit date two years ago by serving the formal Article 50 divorce papers, she declared there would be "no turning back" but parliament's refusal to ratify the withdrawal deal she agreed with the EU has thrust her government into crisis. Now, just nine days before the exit date, May is to write to European Council President Donald Tusk to ask for a short delay. May "won't be asking for a long extension, said a source in her Downing Street office, who spoke on condition of anonymity. May had warned lawmakers that she could seek an extension beyond June 30 if they voted down her treaty a third time. While the United Kingdom remains divided over Brexit, most agree that it will shape the prosperity of generations to come and, if it goes badly, could undermine the West and threaten London's position as the dominant global financial capital. The loss of Britain for the EU is the biggest blow yet to more than 60 years of effort to forge European unity in the wake of two world wars, though the 27 other members of the bloc have shown surprising unity during the tortuous negotiations. Britain's almost three-year crisis over Brexit has left allies and investors puzzled by a country that for decades seemed a confident pillar of Western economic and political stability."""]
gfirst = [('it','the United Kingdom'),('she','May'),('she','May'),('her','May'),
('her','May'),('she','May'),('they','lawmakers'),('her','May'),
('it','Brexit'),('it','Brexit')]

gtsecond = ["musk","""Mr. Musk declined to discuss what profit margin the company expected on sales of the $35,000 Model 3 but said Tesla would not make money in the first quarter. "Given that a lot is happening in Q1, we do not expect to be profitable in the first quarter," he said. But he added that the company expected to return to profitability in the second quarter. The company"s stock fell more than 5 percent in early trading on Friday. Mr. Musk also said the company was now only taking orders online, and would close some showrooms and reduce its work force. "There"s no other way for us the achieve the savings for this car to be financially sustainable," he said. He declined to say how many reservations the company still had from customers who had expressed interest in buying a Model 3. Last summer, Tesla had more than 400,000 orders for the car. "The reservation list doesn"t matter," Mr. Musk said. Mr. Musk also expressed little certainty about how much demand the company is seeing for the Model 3. "My gut feel is 500,000 a year," he said. But he added: "I don"t know what demand is. We"ll see." To put buyers at ease about making such big-ticket purchases on the internet, he said, customers will be allowed to return cars for a full refund within seven days as long as the cars have not been driven more than 1,000 miles. "It"s going to be super easy to get a refund," he said. "People should not have concerns about placing an order." """]
gsecond = [('he','Musk'),('he','Musk'),('its','Tesla'),('he','Musk'),('he','Musk'),('he','Musk'),
('he','Musk'),('i','Musk'),('he','Musk')]

tthirth = ["shooting","""In the gunmans self-made video of the killings he had posted to Facebook, a man can be seen trying to tackle him as he began firing in Al Noor mosque. That man was Naeem Rashid, according to witnesses. His family described him as an intelligent, ambitious and devout father of three. His eldest son, Talha Naeem, was also killed. Mr. Rashid was in his 40s, according to Stuff and Radio New Zealand. His brothers, interviewed in Pakistan, said he had left a senior position at Citibank in the city of Lahore in 2010 to pursue a doctorate in Christchurch and raise his children in a peaceful country. Starting over proved more difficult than he had expected. "Like everybody who leaves this country, he left Pakistan because of lack of opportunities here," said Dr. Khurshid Alam, one of Mr. Rashid his brothers. "He went there to do his Ph.D. Because of the financial situation, he couldnt complete it, so he was teaching part-time." He became much more devout during his time in New Zealand, according to his brothers. They said he talked about wanting to die a martyr, which he felt was the most honorable way for a Muslim to die."""]
gthirth = [('he','the gunman'),('him','the gunamn'),('his','Rashid'),('him','Rashid'),
('his','Rashid'),('he','Rashid'),('his','Rashid'),('he','Rashid'),
('he','Rashid'),('he','Rashid'),('his','Rashid'),('he','Rashid'),
('he','Rashid'),('he','Rashid'),('his','Rashid'),('his','Rashid'),
('he','Rashid'),('he','Rashid'),('here','Pakistan'),('there','New Zealand'),('it','Ph.D.')]

tfourth = ["pogba", """Manchester United interim boss Ole Gunnar Solskjaer has restored the confidence and freedom they lacked towards the end of Jose Mourinho"s tenure and the Norwegian deserves to take over full time, midfielder Paul Pogba has said. Former United striker Solskjaer has rejuvenated the team since replacing the sacked Mourinho in December, helping them win 10 out of the 13 Premier League games since his appointment and reaching the Champions League quarter-finals. "We want him to stay. The results have been great. I have a great relationship with him, he has a great relationship with the players," Pogba told Sky Sports. "When a player is happy, he wants to keep being happy. Solskjaer deserves it. He knows the club, he knows everything about the club. He is a really happy coach that gave confidence back to the players. "This gave us the freedom to play and enjoy football again because maybe we lost that with the results that we had before." Despite winning the World Cup with France last year, Pogba struggled for form under Mourinho who benched him, but the 26-year-old is back to his best under Solskjaer with nine goals and seven assists in all competitions. "Maybe we lost confidence, maybe things went wrong. A lot of talking outside that we weren"t used to," Pogba said, reflecting on the final part of Mourinho"s tenure. "I don"t like to talk about the past. I like to talk about the future because that"s what matters. We"re better now and the results have been brilliant." """]
gfourth = [('they','Manchester United'),('them','Manchester United'),('his','Solskjaer'),
('him','Solskjaer'),('I','Pogba'),('him','Solskjaer'),('he','Solskjaer'),('he','Solskjaer'),
('he','Solskjaer'),('he','Solskjaer'),('we','Manchester United'),('we','Manchester United'),
('him','Pogba'),('his','Pogba'),('we','Manchester United'),('we','Manchester United'),
('i','Pogba'),('we','Manchester United')]

class Checker:

    def __init__(self):
        pass

    gold_lists = {
        "0": gfirst,
        "1": gsecond,
        "2": gthirth,
        "3": gfourth
    }

    def calc_occ(self, check_list,list_nr):
        true_pos, false_pos, true_neg, false_neg = 0,0,0,0

        gold_list = self.gold_lists.get(list_nr)

        tot_ana = len(gold_list)
        for pair in check_list:
            if pair in gold_list:
                true_pos+=1
                gold_list.remove(pair)
            else:
                false_pos+=1

        false_neg = len(gold_list)
        precision = (true_pos/(true_pos+false_pos))
        recall = (true_pos/(true_pos+false_neg))
        #accuracy = ((true_pos+true_neg)/(true_pos+false_pos+true_neg+false_neg))
        return "Total anaphora: {}\n True positives: {} \n False positive: {} \n True negatives: {} \n False negatives: {} \n Recall: {}\n Precision: {}\
".format(tot_ana,true_pos,false_pos,true_neg,false_neg,recall,precision)
