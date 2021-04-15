# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_1 = 'Gullit'
scorer_2 = 'Van Basten'
goal_0 = 32
goal_1 = 54


scorers = scorer_1 + str(goal_0), scorer_2+ str(goal_1)
print (scorers)

report = f'{scorer_1} scored in the {goal_0}nd minute"\n"{scorer_2} scored in the {goal_1}th minute'
print (report)



player = 'Ronald Koeman'
end_first_name = player.find(" ")
first_name = player[:end_first_name]
print (first_name)

last_name = player[end_first_name+1:]
last_name_len = len(last_name)
print (last_name_len)

name_short = f'{player[0]}. {last_name}'
print (name_short)

x = 5
single_chant = f'{first_name}! '
chant = (single_chant * 5) [:-1]
print (chant)

good_chant = chant[-1] !=' '
print (good_chant)


