
# coding: utf-8

# In[1]:

#1) The data describes the SAT scores of students in each state as well as the percentage of students who take the exam. 
#2) The data seems to be complete, however there is a title list and also a list of overall scores which would interfer 
#     with our computations later on if not cleaned out.


# In[2]:

#4)loading data into list of list.
import csv
import numpy as np
all= []
with open('sat_scores.csv', 'U') as f:
    for row in csv.reader(f):
        all.append(row)
f.close


# In[3]:

#3) Putting Data into Data Dictionary
scores={}
for item in all:
    if item[0] != 'State' and item[0] != 'All':
        scores[item[0]]=[(item[1]),(item[2]),(item[3])]


# In[4]:

#5) Printing Data
for item in scores:
    print item, scores[item]


# In[5]:

#6) extracting labels from the data, and removing these items (was done previously for data dictionary as well)
#    (also removing the 'All' data point as it does not represent an idividual state)
labels=[]
clean=[]
for item in all:
    if len(item[0]) != 2:
        labels.append(item)
    else:
        clean.append(item)
print labels


# In[6]:

#7) creating list of state names
statenames=[]
for item in clean:
    statenames.append(item[0])


# In[7]:

#8) identifying column types
for item in clean[0]:
    print type(item),


# In[8]:

#9) The items in 'Rate', 'Verbal', & 'Math' should be listed as floats
for item in clean:
    item[1]=int(item[1])
    item[2]=int(item[2])
    item[3]=int(item[3])


# In[9]:

#10) creating a dictionary for each column with state as key and score as value
rate={}
verbal={}
math={}
for item in clean:
    rate[item[0]]=item[1]
    verbal[item[0]]=item[2]
    math[item[0]]=item[3]


# In[10]:

#12) identifying the max and min of each rate, math, and verbal

def maxmin(dic):
    maxstate='unassigned'
    maxvalue=0
    minstate='unassigned'
    minvalue=0
    listmin=[]
    listmax=[]
    for item in dic:
        if maxstate == 'unassigned':
            maxstate=item
            minstate=item
            maxvalue=dic[item]
            minvalue=dic[item]
        elif dic[item] > maxvalue:
            maxstate=item
            maxvalue=dic[item]
        elif dic[item]<minvalue:
            minstate=item
            minvalue=dic[item]
    for item in dic:
        if dic[item]==maxvalue:
            listmax.append(item)
        elif dic[item]==minvalue:
            listmin.append(item)         
    print listmax,maxvalue
    print listmin,minvalue

print "The Max and Min for Rate is: "
maxmin(rate)
print "The Max and Min for Math is: "
maxmin(math)
print "The Max and Min for Verbal is: "
maxmin(verbal)


# In[11]:

#13) Finding Standard Deviation using List comprehension

def standard (dic):
    mean=np.mean([dic[n] for n in dic])
    stdr=np.mean([(dic[n] - mean)**2 for n in dic])
    stdr=stdr**(0.5)
    return stdr

print "std rate: %f"% standard(rate)
print "std math: %f"% standard(math)
print "std verbal: %f" % standard(verbal)


# In[12]:

# 14) Plotting rate with matplotlib 
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
ratelist=[]
for item in rate:
    ratelist.append(rate[item])

print "Rate Mean: %f" % np.mean(ratelist)
print "Rate Median: %f" % np.median(ratelist)
plt.hist(ratelist,15)
plt.show()


# In[13]:

# 15) Plotting math with matplotlib 

mathlist=[]
for item in math:
    mathlist.append(math[item])

print "Math Mean: %f" % np.mean(mathlist)
print "Math Median: %f" % np.median(mathlist)
plt.hist(mathlist,15)
plt.show()


# In[14]:

# 16) Plotting verbal with matplotlib 

verballist=[]
for item in verbal:
    verballist.append(verbal[item])

print "Verbal Mean: %f" % np.mean(verballist)
print "Verbal Median: %f" % np.median(verballist)
plt.hist(verballist,15)
plt.show()


# In[15]:

#17 & 18) Typically you would assume that these distributions would be roughly normally ditributed. However, none of these 
#    distributions follow this trend. All three distributions appear to be scewed to the right. The  verbal distibution 
#    even appears to be slighly bimodal 


# In[16]:

#19) Scatter plots
plt.scatter(ratelist,verballist,c='b', marker= 's')
plt.scatter(ratelist,mathlist,c='r', marker= 'o')
plt.show()

plt.scatter(verballist, mathlist)
plt.show()


# In[17]:

#20) There is a notable relationship between rate and score. As the rate increases, the score for that state decreases.
#     This was consistent for both math and verbal scores. 


# In[18]:

#21) Box plots
print'Rates'
plt.boxplot(ratelist)
plt.show()
print 'Verbal'
plt.boxplot(verballist)
plt.show()
print 'Math'
plt.boxplot(mathlist)
plt.show()


# In[ ]:



