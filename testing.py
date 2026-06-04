import pandas as pd

reg_no = [230301,230302,230303,230304,230305]
roll_no = [1,2,3,4,5]
name = ['ade','ade','aim','anek','az']
mark = [91,90,None,97,93]

my_dict = {
    'names': name,
    "roll_no":roll_no,
    'marks  ':mark
}

my_df = pd.DataFrame(my_dict,index= reg_no)
print(my_df)
print("\n")

marks_mean = my_df['marks  '].mean()
my_df['marks  '] = my_df['marks  '].fillna(marks_mean)

my_df['bonus_new_marks'] = my_df['marks  '].apply(lambda x : x+2 if x>91 else x)
print(my_df)

roll_no_map = {
    1:301,
    2:302,
    3:303,
    4:304,
    5:305
}

print('-----')
my_df['roll_no'] = my_df['roll_no'].map(roll_no_map)
print(my_df)
print('-----')
my_df = my_df.assign(new_marks=lambda x :x['marks  ']+1)
print(my_df)

print('-----')
my_df = my_df.rename(columns={'names':'NAMES'})
print(my_df)

my_df = my_df.rename(columns= lambda x: x.strip())
print(my_df)

my_df = my_df.sort_values('marks')
print(my_df)
my_df = my_df.reset_index()
print(my_df)
my_df = my_df.rename(columns={'index':'reg_no'})


new_order = ['roll_no','reg_no','NAMES','marks','bonus_new_marks','new_marks']
my_df = my_df[new_order]
print(my_df)

print("----")

my_df.rename(columns=lambda x: x.capitalize(),inplace=True)
print(my_df)