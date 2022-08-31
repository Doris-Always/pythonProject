users = [
    {'name': 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'username': 'dezaah',
     'is verified': True,
     'tweets': [
         {'content': 'PO for president', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is a mad man', 'likes': 4, 'retweets': 2}
     ]

     },
    {
        'name': 'Ibrahim',
        'age': 21,
        'gender': 'Male',
        'username': 'ibrahah',
        'is verified': True,
        'tweets': [
            {'content': 'PO for president', 'likes': 450, 'retweets': 233},
            {'content': 'Atiku is a mad man', 'likes': 4, 'retweets': 2}
        ]
    },
    {
        'name': 'Racheal',
        'age': 21,
        'gender': 'Female',
        'username': 'betty',
        'is verified': False,
        'tweets': [
            {'content': 'PO for president', 'likes': 450, 'retweets': 233},
            {'content': 'Atiku is a mad man', 'likes': 4, 'retweets': 2},
            {'content': 'Amazing grace', 'likes': 2000, 'retweets': 2}
        ]
    }
]

no_of_users = len(users)
usernames = {user['username'] for user in users}
female_users = [user['name'] for user in users if user['gender'] == 'Female']
user_age = [{'name': user['name'], 'age': user['age']}for user in users]
avg_age_of_users = round(sum(user['age'] for user in users1) / len(users))
print(avg_age_of_users)