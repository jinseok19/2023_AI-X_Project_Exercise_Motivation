from gtts import gTTS
def Before_tts(text, situation):
    tts = gTTS(
        text = text,
        lang='en',
        slow = False
    )
    if situation == 1:

        tts.save('Before/B_1_{0}.mp3'.format(text))
    else:
        tts.save('Before/B_2_{0}.mp3'.format(text))

def After_tts(text, index):
    tts = gTTS(
        text = text,
        lang='en',
        slow = False
    )
    
    tts.save('After/A_{0}_{1}.mp3'.format(index, text))

def During_tts(text, situation):
    tts = gTTS(
        text = text,
        lang='en',#
        slow = False
    )
    if situation == 1:

        tts.save('Progress/P_1_{0}.mp3'.format(text))
    else:
        tts.save('Progress/P_2_{0}.mp3.'.format(text))

#Before
#/1 / Input : I don’t want to workout now!
#/2 / Input : I don't think it's okay not to go to the gym today.
# Before_tts('Just start with one exercise, and I promise you’ll feel more energized and motivated to continue.', 1)
# Before_tts('Just get started by doing one small thing, like a five-minute warm-up or stretch, and see how you feel. Sometimes taking the first step is the hardest part.',1)
# Before_tts('Just start with a few minutes of exercise. Once you get going, you’ll likely find that you have more energy and motivation to continue. Give it a try!',1)
# Before_tts('Get up and move your body, even a little bit. You’ll feel better once you get started, I promise.',1)
# Before_tts('Just try to start with a 10-minute workout. You will feel great once you get started!',1)

# Before_tts("I don't think it's okay not to go to the gym today.", 2)
# Before_tts("Just remember, every workout adds up. Even if it's just a short one.",2)
# Before_tts('You got this! Go and smash your workout! 💪',2)
# Before_tts("Just remember, every workout brings you one step closer to being the best version of yourself. Don't skip it and keep pushing!",2)
# Before_tts("Just remember that every little bit counts. Even if you can't make it to the gym, there are still other ways to stay active and lead a healthy lifestyle.",2)

#During
#/1 / Input : Please make me motivative to reach my goals.
#/2 / Input : I want to stop now and go home.
'''
Push yourself a little harder, always remember why you started. You got this!
Keep going, you got this!
No! Keep pushing yourself and finish your workout strong. You'll feel better afterward!
Just one more set and you'll be closer to achieving your fitness goal. You got this!
Think about the feeling of accomplishment you will have once you finish your workout. Push through and remember how good it will feel to have completed it.
'''

# During_tts("You got this! Don’t give up, keep pushing yourself to reach your goals and remember why you started in the first place!",1)
# During_tts("You got this! Keep pushing and never give up on your goals. Remember every little step you take towards your goal is progress. Stay motivated and keep striving towards greatness!",1)
# #During_tts("You’ve got this! Every small step you take towards your goal is progress. Remember, success isn’t about perfection, it’s about effort, Keep pushing forward and don’t give up, you will get there!",1)
# During_tts("Remember, every step you take towards your goal is progress. It my not be easy, but with consistency and effort, you will see results. Keep pushing yourself and believe in your ability to reach your goals. You can do this!",1)
# During_tts("You got this! Keep pushing yourself, one day at a time. Remember, each small step you take towards your goal is progress. Focus on your why and let it drive you to succeed. Keep up the good work!",1)

# During_tts("Push yourself a little harder, always remember why you started. You got this!",2)
# During_tts("Keep going, you got this!",1)
During_tts("No!!!!!!!!! Keep pushing yourself and finish your workout strong. You'll feel better afterward!",2)
# During_tts("Just one more set and you'll be closer to achieving your fitness goal. You got this!",2)
# During_tts("Think about the feeling of accomplishment you will have once you finish your workout. Push through and remember how good it will feel to have completed it.",2)


#/1 / Input :  I'm done!
#/2 / Input :  Let me know how many times I worked out this week.
#/3 / Input :  Input : I feel like a zombie.
#/4 / Input :  Wow, I'm so tired that I'm going to faint when I get home.
#/5 / Input :  Please add a day of the week to the day I worked out and make a list.
#/6 / Input :  I probably won't be able to exercise tomorrow.
#/7 / Input :  It was so hard today. Can I keep doing this?
#/8 / Input :  How many times did I work out this week?
#/9 / Input :  I’m very satisfied.
#/10 / Input :  Feel recharged and refreshed, better than yesterday!
#/11 / Input :  I feel like shit but can take on the world!
#/12 / Input :  so satisfied!
#/13 / Input :  so tired!
#/14/ Input :  dead tired!

After_tts('Congratulations on finidhing your workout! Rest and recover, you earned it!',1)
After_tts('So far this week, Youjin, you have worked out 5 times. Great job!',2)
After_tts('Rest is important, take a break.',3)
#After_tts("Make sure you take some time to rest and properly recover, Youjin. Getting enough rest is just as important as pushing yourself during your workouts. Don't worry about having an off day, just focus on getting back to it when you're feeling better. You got this!",4)
#After_tts("Sure thing, Youjin! Here's a list of the days you worked out, along with their corresponding days of the week:1. January 1, 2023 (Sunday)2. January 2, 2023 (Monday)3. January 5, 2023 (Thursday)Keep up the good work!",5)
#After_tts("That's okay, Youjin. Taking a day off from exercise can actually be beneficial to allow your muscles to rest and recover. Just be sure to get back into your routine as soon as you're able and stay motivated!",6)
After_tts('Absolutely! Remember, progress takes time, but as long as you keep up your motivation, you can reach your goals. Keep pushing and stay motivated!',7)
After_tts('You have worked out for 4 days this week, Youjin. Keep up the good work and continue to make progress towards your fitness goals. 💪',8)
#After_tts("That's great to hear, Youjin! Taking care of your body by exercising and making progress towards your fitness goals is definitely something to be proud of. Keep up the good work and stay satisfied with what you're accomplishing! 💪Great job, Sehee! Keep up the good work! 💪",9)
#After_tts("Great work, Youjin! It sounds like your workout was exactly what you needed to recharge and refresh. Keep up the good work and keep challenging yourself to reach new levels of fitness. Your hard work is paying off!Great job, Youjin! Remember that taking care of your body is important for both your physical health and mental well-being. Keep up the good work!",10)
#After_tts("Way to push through your workout, Youjin! Feeling like shit is temporary and soon you’ll feel the energy that comes from exercise. Keep up the hard work and keep crushing those workouts!Great attitude, Youjin! Even on the days when you don't feel your best, remember that any effort you put towards your goals is better than doing nothing at all. Keep pushing yourself and you'll be amazed at what you can accomplish!",11)
After_tts('Awesome work, Youjin! Keep that satisfaction and use it as motivation for your next workout. Remember, every workout is a step towards your goal.',12)
After_tts('Great job on finishing your workout, Youjin! Keep pushing through and remember that the results will be worth it.',13)
After_tts('You’ve done a fantastic job, be proud of yourself! Now, take a nice, deep breath, and let the feeling of accomplishment wash over you.',14)


