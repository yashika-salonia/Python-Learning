dict={'key1':1,'key2':'2','key3':[2,4,7],'key4':{1,3,4,5},('key5'):5,(0,1):6,'DOB':'20.10.2004'} #key1-int, key2-string, key3-array, key4-tuple(immutable), key5
print(dict['DOB'])
print(dict[0,1])

sampleDict={
    'Name':'abcd',
    'Roll':23,
    'Section':'D',
}
print(sampleDict.keys())
sampleDict["New"]='hii' #creating new key
print(sampleDict)

# deleting a key
del(sampleDict["New"])

print(sampleDict)

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
# print(release_year_dict.keys())
# print(release_year_dict.values())