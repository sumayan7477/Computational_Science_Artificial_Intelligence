# leap year is a year that is divisible by 4, except for years that are divisible by 100, unless they are also divisible by 400. For example, the year 2000 is a leap year because it is divisible by 400, but the year 1900 is not a leap year because it is divisible by 100 but not by 400.
def is_leap(year):
    # YOUR CODE HERE
    return (year % 400 ==0) or ( year % 4 == 0 and year % 100 != 0 )



def get_sentence(year):
    if is_leap(year):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

#  even number is a number that is divisible by 2. For example, the number 4 is even because it is divisible by 2, but the number 5 is not even because it is not divisible by 2.
def is_even(num):
    # YOUR CODE HERE...
    if num%2==0 : 
        return True
    else : 
        return False
        


def get_sentence(num):
    
    if is_even(num):
        return str(num) + " is even"
    else:
        return str(num) + " is odd"


#   tictok like, comment, share engagement score calculator

# Calculate engagement based on likes, comments and shares, which are int
def calc_engagement_score(likes, comments, shares):
    return(likes + (comments * 2) + (shares * 3))


# Classify the video's popularity level based on score
def popularity_level(score):
    if score > 100:
        return "viral"
    elif score > 50:
        return "trending"
    else:
        return "low"

video_likes = 20
video_comments = 15
video_shares = 10

score = calc_engagement_score(video_likes , video_comments, video_shares)
level = popularity_level(score)

print("Score:", score)
print("Status:",level)



# grade calculator
def calc_exam_grade(score):

    if   score >= 18 :
        return 5
    elif score >= 16 :
        return 4
    elif score >= 14 :
        return 3
    elif score >= 12 :
        return 2
    elif score >= 10 :
        return 1
    else :
        return 0
   
def calc_avg(exercises , project , exam_score)   :
    exam_grade = calc_exam_grade(exam_score)

    if exam_grade>=1 and exercises>=1 and project >=1:
        return ((exercises * 0.25)+(project * 0.25) +(exam_grade * 0.5))
    else :
        return 0

def print_report(name , grade):
    print("Student:" , name)
    print("score:" , round(grade,2))