t=int(input())
for _ in range(t):
	        n=int(input())
	        f=input().split()
	        s=input().split()
	        t=input().split()
	        l=[]
	        a=0
	        b=0
	        c=0
	        ff=set(f)
	        ss=set(s)
	        tt=set(t)
	        for i in ff:
	        	if (i in ss) and (i in tt):
	        		a+=0
	        	elif (i in ss) and (i not in tt):
	        		a+=1
	        	elif (i not in ss) and (i not in tt):
	        		a+=3
	        	else:
	        		a+=1
	        l.append(a)
	        for i in ss:
	        	if (i in ff) and (i in tt):
	        		b+=0
	        	elif (i in ff) and (i not in tt):
	        		b+=1
	        	elif (i not in ff) and (i not in tt):
	        		b+=3
	        	else:
	        		b+=1
	        l.append(b)
	        for i in tt:
	        	if (i in ss) and (i in ff):
	        		c+=0
	        	elif (i in ss) and (i not in ff):
	        		c+=1
	        	elif (i not in ss) and (i not in ff):
	        		c+=3
	        	else:
	        		c+=1
	        l.append(c)
	        print(*l)
	        		
	        	
	        
	     
	        	
	        
	     
