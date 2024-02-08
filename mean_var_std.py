#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


def calculate(l1):
    pro=np.array(l1).reshape((3, 3))
    me=pro.mean(axis=0)
    mec=pro.mean(axis=1)
    means=[]
    mean_r=[]
    mean_c=[]
    for i in me:
        x="{:.1f}".format(i)
        mean_r.append(x)
        x=0
    for j in mec:
        y="{:.1f}".format(j)
        mean_c.append(y)
    t=pro.flatten(order='C')
    w=t.mean()
    means.append(mean_r)
    means.append(mean_c)
    means.append(w)
    vari=pro.var(axis=0)
    varic=pro.var(axis=1)
    varis=[]
    vari_r=[]
    vari_c=[]
    for i in vari:
        x="{:.1f}".format(i)
        vari_r.append(x)
        x=0
    for j in varic:
        vari_c.append(j)
    t=pro.flatten(order='C')
    w=t.var()
    varis.append(vari_r)
    varis.append(vari_c)
    varis.append(w)
    stdi=pro.std(axis=0)
    stdc=pro.std(axis=1)
    stds=[]
    std_r=[]
    std_c=[]
    for i in stdi:
        std_r.append(i)
    for j in stdc:
        std_c.append(j)
    t=pro.flatten(order='C')
    w=t.std()
    stds.append(std_r)
    stds.append(std_c)
    stds.append(w)
    maxi=np.amax(pro,axis=0)
    maxc=np.amax(pro,axis=1)
    maxs=[]
    max_r=[]
    max_c=[]
    for i in maxi:
        max_r.append(i)
    for j in maxc:
        max_c.append(j)
    t=pro.flatten(order='C')
    w=np.amax(t)
    maxs.append(max_r)
    maxs.append(max_c)
    maxs.append(w)
    mini=np.amin(pro,axis=0)
    minc=np.amin(pro,axis=1)
    mins=[]
    min_r=[]
    min_c=[]
    for i in mini:
        min_r.append(i)
    for j in minc:
        min_c.append(j)
    t=pro.flatten(order='C')
    w=np.amin(t)
    mins.append(min_r)
    mins.append(min_c)
    mins.append(w)
    sumi=np.sum(pro,axis=0)
    sumc=np.sum(pro,axis=1)
    sums=[]
    sum_r=[]
    sum_c=[]
    for i in sumi:
        sum_r.append(i)
    for j in minc:
        sum_c.append(j)
    t=pro.flatten(order='C')
    w=np.sum(t)
    sums.append(sum_r)
    sums.append(sum_c)
    sums.append(w)
    ans={"'mean':":means,
      "'variance':":varis,
       "'standard deviation':":stds,
       "'max':":maxs,
        "'min':":mins,
         "'sum':":sums}
    for key, value in ans.items():
        print(key,value)
l1=[]
for i in range(9):
    a=input()
    l1.append(int(a))
calculate(l1)


# In[ ]:




