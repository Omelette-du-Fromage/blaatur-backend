dest_blacklist = ['Bergen', 'Asker']
# destination_candidates = ['Bergen']
#
# x = all(dest in dest_blacklist for dest in destination_candidates)
# print(x)

x = any(dest in 'Bergen stasjon' for dest in dest_blacklist)
print(x)