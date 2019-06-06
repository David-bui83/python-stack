def reverseList(p_list):
  i=0
  j=len(p_list)-1
  while i < len(p_list):
    temp=p_list[i]
    p_list[i] = p_list[j]
    p_list[j] = temp
    i+=1
    j-=1

