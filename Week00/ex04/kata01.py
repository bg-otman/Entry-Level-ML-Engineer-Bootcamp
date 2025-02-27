kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
kata_keys = [key for key in kata]

for key in kata:
    print(f"{key} was created by {kata[key]}")