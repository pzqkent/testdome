class MergeNames:

    @staticmethod
    def unique_names(names1, names2):
        names1.extend(names2)
        # a = names1
        a = list(set(names1))

        return a
        # return set(names1.extend(names2))

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(MergeNames.unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia