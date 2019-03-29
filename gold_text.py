gfirst = ["uk","""Nearly three years since the United Kingdom voted to leave the
European Union, British politicians are still arguing over how, when or even if
the world's fifth largest economy should leave the bloc ---the United Kindom---
first joined 1973. When May set the March 29 exit date two years ago by serving
the formal Article 50 divorce papers, ---May--- declared there would be "no turning
back" but parliament's refusal to ratify the withdrawal deal ---May--- agreed with
the EU has thrust ---May--- government into crisis. Now, just nine days before the
exit date, May is to write to European Council President Donald Tusk to ask for a
short delay. May "won't be asking for a long extension, said a source in ---May---
Downing Street office, who spoke on condition of anonymity. May had warned lawmakers
that ---May--- could seek an extension beyond June 30 if ---lawmakers--- voted down
---May--- treaty a third time. While the United Kingdom remains divided over Brexit,
most agree that ---Brexit--- will shape the prosperity of generations to come and,
if ---Brexit--- goes badly, could undermine the West and threaten London's position
as the dominant global financial capital. The loss of Britain for the EU is the
biggest blow yet to more than 60 years of effort to forge European unity in the wake
of two world wars, though the 27 other members of the bloc have shown surprising
unity during the tortuous negotiations. Britain's almost three-year crisis over
Brexit has left allies and investors puzzled by a country that for decades seemed
a confident pillar of Western economic and political stability."""]
dfirst = [('it','the United Kingdom'),('she','May'),('she','May'),('her','May'),
('her','May'),('she','May'),('they','lawmakers'),('her','May'),
('it','Brexit'),('it','Brexit')]

gsecond = ["musk","""Mr. Musk declined to discuss what profit margin the company expected on sales of the $35,000 Model 3 but said Tesla would not make money in the first quarter. "Given that a lot is happening in Q1, we do not expect to be profitable in the first quarter," ---Musk--- said. But ---Musk--- added that the company expected to return to profitability in the second quarter. The company"s stock fell more than 5 percent in early trading on Friday. Mr. Musk also said the company was now only taking orders online, and would close some showrooms and reduce ---Tesla--- work force. "There"s no other way for ---Musk & Tesla--- the achieve the savings for this car to be financially sustainable," ---Musk--- said. ---Musk--- declined to say how many reservations the company still had from customers who had expressed interest in buying a Model 3. Last summer, Tesla had more than 400,000 orders for the car. "The reservation list doesn"t matter," Mr. Musk said. Mr. Musk also expressed little certainty about how much demand the company is seeing for the Model 3. "---Musk--- gut feel is 500,000 a year," ---Musk--- said. But ---Musk--- added: "---Musk--- don"t know what demand is. ---Musk & Tesla---"ll see." To put buyers at ease about making such big-ticket purchases on the internet, ---Musk--- said, customers will be allowed to return cars for a full refund within seven days as long as the cars have not been driven more than 1,000 miles. "It"s going to be super easy to get a refund," ---Musk--- said. "People should not have concerns about placing an order." """]
dsecond = [('he','Musk'),('he','Musk'),('its','Tesla'),('he','Musk'),('he','Musk'),('he','Musk'),
('he','Musk'),('i','Musk'),('he','Musk')]

gthirth = ["shooting","""In the gunman's self-made video of the killings ---the gunman--- had posted to Facebook, a man can be seen trying to tackle ---the gunman--- as ---the gunman--- began firing in Al Noor mosque. That man was Naeem Rashid, according to witnesses. ---Naeem Rashid--- family described ---Naeem Rashid--- as an intelligent, ambitious and devout father of three. ---Naeem Rashid--- eldest son, Talha Naeem, was also killed. Mr. Rashid was in ---Mr. Rashid--- 40s, according to Stuff and Radio New Zealand. His brothers, interviewed in Pakistan, said ---Naeem Rashid--- had left a senior position at Citibank in the city of Lahore in 2010 to pursue a doctorate in Christchurch and raise ---Naeem Rashid--- children in a peaceful country. Starting over proved more difficult than ---Naeem Rashid--- had expected. "Like everybody who leaves this country, ---Naeem Rashid--- left Pakistan because of lack of opportunities here," said Dr. Khurshid Alam, one of Mr. Rashid"s brothers. "---Naeem Rashid--- went there to do his Ph.D. Because of the financial situation, ---Naeem Rashid--- couldn"t complete it, so ---Naeem Rashid--- was teaching part-time." ---Naeem Rashid--- became much more devout during ---Naeem Rashid--- time in New Zealand, according to ---Naeem Rashid--- brothers. They said ---Naeem Rashid--- talked about wanting to die a martyr, which ---Naeem Rashid--- felt was the most honorable way for a Muslim to die."""]

gfourth = ["pogba", """Manchester United interim boss Ole Gunnar Solskjaer has restored the confidence and freedom ---Manchester United--- lacked towards the end of Jose Mourinho"s tenure and the Norwegian deserves to take over full time, midfielder Paul Pogba has said. Former United striker Solskjaer has rejuvenated the team since replacing the sacked Mourinho in December, helping ---Manchester United--- win 10 out of the 13 Premier League games since ---Ole Gunnar Solskjaer--- appointment and reaching the Champions League quarter-finals. "---Manchester United--- want ---Ole Gunnar Solskjaer--- to stay. The results have been great. ---Pogba--- have a great relationship with ---Ole Gunnar Solskjaer---, ---Ole Gunnar Solskjaer--- has a great relationship with the players," Pogba told Sky Sports. "When a player is happy, ---a player--- wants to keep being happy. Solskjaer deserves ---being happy---. ---Ole Gunnar Solskjaer--- knows the club, ---Ole Gunnar Solskjaer--- knows everything about the club. ---Ole Gunnar Solskjaer--- is a really happy coach that gave confidence back to the players. "This gave ---Manchester United--- the freedom to play and enjoy football again because maybe ---Manchester United--- lost that with the results that ---Manchester United--- had before." Despite winning the World Cup with France last year, Pogba struggled for form under Mourinho who benched ---Pogba---, but the 26-year-old is back to ---Pogba--- best under Solskjaer with nine goals and seven assists in all competitions. "Maybe ---Manchester United--- lost confidence, maybe things went wrong. A lot of talking outside that ---Manchester United--- weren"t used to," Pogba said, reflecting on the final part of Mourinho"s tenure. "---Pogba--- don"t like to talk about the past. ---Pogba--- like to talk about the future because that"s what matters. ---Manchester United---'re better now and the results have been brilliant." """]

class Checker:

    def __init__(self):
        pass

    def calc_occ(self, check_list,list_nr):
        true_pos, false_pos, true_neg, false_neg = 0,0,0,0
        gold_list = []
        if list_nr == "0":
            gold_list = dfirst
        elif list_nr == "1":
            gold_list = dsecond
        listl = len(gold_list)
        for pair in check_list:
            if pair in gold_list:
                true_pos+=1
                gold_list.remove(pair)
            else:
                false_pos+=1
        false_neg = len(gold_list)
        precision = (true_pos/(true_pos+false_pos))
        recall = (true_pos/(true_pos+false_neg))
        accuracy = ((true_pos+true_neg)/(true_pos+false_pos+true_neg+false_neg))
        return "Total anaphora: {}\n True positives: {} \n False positive: {} \n True negatives: {} \n False negatives: {} \n Recall: {}\n Precision: {}\n Accuracy: {}.\
".format(listl,true_pos,false_pos,true_neg,false_neg,recall,precision,accuracy)
