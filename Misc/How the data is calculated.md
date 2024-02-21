# Ratio Scenarios

Given we have VIX futures with these values:

Commercial Long, Short = 4000, 10000
Large Speculator Long = 20000, 5000


In general, commercial usually are the opposite of large speculators, and the direction is generally decided by the large speculators, (but not always). Hence, we can calculate the following ratios:

---

RatioComm=5000:10000=2:5
RatioLarge=20000:5000=1:4
RatioLong=4000:20000= 1:5
RatioShort=10000:5000=2:1

---
# Main Formulas

Direction Weight= (Long(large) - Short(large))/Total
Confidence factor = (Ratio of Large Spec/(Ratio large spec + ratio comms)) / Direction Weight

---

In this example, we get the direction being 20000-5000/25000 = 0.6. However, if we had another example such that the values were switched, we get 5000-15000/25000 = -0.6. Thus, we get the total values that can be achieved for the directional weight is from -1 to 1, with the extremes meaning that the direction has more weight, hence contributing to a higher confidence in the trade. 

Hence, we can calculate the confidence factor as follows:

1:41:4+2:5÷0.6

Giving 25/39 or 0.641 to 3 decimal places. 

Hence, we can get a good output from the terminal:

SYMBOL: VIX

DIRECTION: 0.6

CONFIDENCE: 0.641

