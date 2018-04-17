# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

def minOps(request):
	context={}
	template='Minimum_Operations/main.html'
	string_1=request.GET.get('string_1',None)
	string_2=request.GET.get('string_2',None)
	# We check if both string_1 and string_2 are not None
	# If they are we just load the site awaiting for the strings to be input
	if not (string_1 and string_2):
		context['flag']=False
		return render(request,template,context)
	else:
		s1=len(string_1)
		s2=len(string_2)

		# This part checks whether conversion is possible or not
		# by comparing the length of both strings
		if s2!=s1:
			context['flag']=True
			context['res']=-1
			return render(request,template,context)

		count={}
		# count characters in string_1
		for i in string_1:
			if i in count:
				count[i]+=1
			else:
				count[i]=1
		# subtract count for every char in string_2
		for i in string_2:
			if i in count:
				count[i]-=1
		# Check if all  values of count become 0
		# If not we return -2 which means that the strings
		# don't have the same characters even though they are the same length
		if sum(count.values())!=0:
			context['flag']=True
			context['res']=-2
			return render(request,template,context)

		# Calculate the number of operations required
		res=0
		i=s2-1
		j=s2-1
		while i>=0:
			# if there is a mismatch, then keep incrementing
			# result 'res' until string_2[j] is not found in string_1[0..i]
			while i>=0 and string_1[i]!=string_2[j]:
				i-=1
				res+=1
			# if string_1[i] and string_2[j] match
			if i>=0:
				i-=1
				j-=1
		context['flag']=True
		context['res']=res
		return render(request,template,context)