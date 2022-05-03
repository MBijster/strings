# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer0_name= 'Ruud Gullit'
scorer1_name= 'Marco van Basten'
goal_0= 32
goal_1= 54
scorers= scorer0_name + ' ' + str(goal_0) + ', ' + scorer1_name + ' ' + str(goal_1)
print (scorers)
report=f'{scorer0_name} scored in the {goal_0}nd minute\n{scorer1_name} scored in the {goal_1}th minute'
print(report)

player= "Wim Kieft"
first_name= player[:player.find(' ')]
last_name_find= player[player.find(' '):]
last_name_len= len(last_name_find)-1
name_short= f'{first_name[0]}.{last_name_find}'
print(name_short)
chant= f'{first_name}! '* len(first_name[1:]) + f'{first_name}'+'!' 
print(chant)
good_chant = (' ' != chant)
print(good_chant)

