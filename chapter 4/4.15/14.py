# Write a program that solves the following problem. Three missionaries and three cannibals come to a river and
# find a boat that holds two people. Everyone must get across the river to continue on the journey.
# However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten.
# Find a series of crossings that will get everyone safely to the other side of the river.


people_per_group = 1

boat(people_per_group, people_per_group)

# how do i:
# control state of the boat (which side is it on at any given moment?)
# control shores -> probably just use two lists


# i think u just try combinations and if at any point someone dies, put that in memo and keep iterating


# 000 ### _____   # input
# 000 # _____ ##  # move cannibal bruddas over
# 000 ## _____ #  # move cannibal bruddas over
# 000  _____ ###  # move cannibal bruddas over -> # swap bruddas
# 000 # _____ ##  # swap bruddas
# 0 # _____ 00 ##  # swap bruddas
# 00 ## _____ 0 #  # swap bruddas
# ## _____ 000 #  # swap bruddas
# ### _____ 000  # swap bruddas -> # move cannibal bruddas over
# # _____ 000 ##  # move cannibal bruddas over
# ## _____ 000 #  # move cannibal bruddas over
#  _____ 000 ###  # move cannibal bruddas over


# 00 ## _____  # input
# 00 _____ ##  # move cannibal bruddas over -> # swap bruddas
# 00 # _____ #  # swap bruddas
# # _____ # 00  # swap bruddas
# ## _____ 00  # swap bruddas -> # move cannibal bruddas over
# _____ 00 ##  # move cannibal bruddas over

# 0 # _____  # input
# _____ 0 #  # move both  (special case ???)
