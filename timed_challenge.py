# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#2. Running Total with Reset
#Track a running total of values. If a negative number is added, reset the total to 0.
#Input: [5, 7, -1, 3, 2]
#Output: [5, 12, 0, 3, 5]

def running_total(nums):
    total = 0
    for num in nums:
        if num < 0:
            total = 0
        else:
            total = total + num
        print(total)
    


running_total([5,7,-1,3,2])

#Completed in 12 minutes
'''
Reflection:
I found this assignment to be stressful but also a great learning experience. I was able to complete my question in just 12 minutes. This was my first time looking at the question 
and I had no time to prepare prior. Being timed is something that is challenging for me because it stresses me out and makes me freeze up, even the simplest coding question could get 
messed up or done inefficiently because it is harder to think clearly when I know there is a timer ticking down. This is a new learned weakness of mine because this is a skill that I 
have not personally tried to improve upon in myself. I want to be able to complete more coding challenges within a limited timeframe and see how I do. The more I can do this the better 
I will become a problem solver. I think this challenge was something that I needed to learn new things about myself, and I am sure many people in the class would agree with me on that.
It is important to identify weaknesses within yourself so you can improve yourself and become better at working and expand your searches when it comes to looking for new jobs.
'''