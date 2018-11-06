class FileOwners:

    @staticmethod
    def group_by_owners(files):
        dic1 = {}
        keys = list(files.keys())
        values = list(files.values())
        # print(values)
        for i in range(len(values)):
            if values[i] in dic1.keys():
                dic1[values[i]].append(keys[i])
            else:
                dic1[values[i]] = [keys[i]]

        # print(dic1)    

        return dic1

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))